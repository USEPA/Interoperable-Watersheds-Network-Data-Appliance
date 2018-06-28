#Imports
from datetime import datetime
from glob import glob
import argparse
import csv
import dateutil.parser
import json
import logging
import os
import records
import urllib.request as ur
import urllib.parse
import xml.etree.ElementTree as ET

#Global variables
CSVCHUNKSIZE = 1000
connstring = 'postgres://sos:sensors@ingest_data:5432/ingest'
db = records.Database(connstring)
url = None
station_meta_template="templates/station_template.txt"
sensor_meta_template="templates/sensor_template.txt"
result_meta_template="templates/result_template.txt"
data_template="templates/data_template.txt"

metadata_headers=[
    'stationid',
    'shortName',
    'longName',
    'easting',
    'northing',
    'altitude',
    'organizationName',
    'organizationURL',
    'contact',
    'waterbodyType',
    'urn-org',
    'suborg']

parameter_headers=[
    'parameter',
    'parameterName',
    'parameterUnit',
    'fieldName',
    'status']

offerkey = [
    ['id', "./ns5:identifier", 1],
    ['name',"./ns5:name", 1],
    ['procedure',"./ns5:procedure",1],
    ['proc_fmt',"./ns5:procedureDescriptionFormat",5],
    ['obsprop',"./ns5:observableProperty",5],
    ['respfmt',"./ns0:responseFormat",7],
    ['obstype',"./ns0:observationType",1],
    ['featureofinttype',"./ns0:featureOfInterestType",1],
    ['phenombegin',"./ns0:phenomenonTime/ns6:TimePeriod/ns6:beginPosition",1],
    ['phenomend',"./ns0:phenomenonTime/ns6:TimePeriod/ns6:endPosition",1],
    ['resultbegin',"./ns0:resultTime/ns6:TimePeriod/ns6:beginPosition",1],
    ['resultend',"./ns0:resultTime/ns6:TimePeriod/ns6:endPosition",1]]

namespaces = {
    'ns0':"http://www.opengis.net/sos/2.0",
    'ns2':"http://www.opengis.net/ows/1.1",
    'ns3':"http://www.w3.org/1999/xlink",
    'ns4':"http://www.opengis.net/fes/2.0",
    'ns5':"http://www.opengis.net/swes/2.0",
    'ns6':"http://www.opengis.net/gml/3.2",
    'xsi':"http://www.w3.org/2001/XMLSchema-instance",
    'gda':"http://www.opengis.net/sosgda/1.0",
    'gml':"http://www.opengis.net/gml/3.2"}

#Functions
def create_offer_dict(noff):
    off_d = {}
    for field in offerkey:
        for i in range(field[2]):
            off_d[field[0]] = [j.text for j in noff.findall(field[1],namespaces)]
    return off_d

def parse_capabilities(url):
    r = ur.urlopen(url + "?service=SOS&request=GetCapabilities")
    tree = ET.parse(r)
    with open('debug/capabilities.xml','wb') as of:
        tree.write(of)
    root = tree.getroot()
    offerings_l = root.findall('./ns0:contents/ns0:Contents/ns5:offering/ns0:ObservationOffering',namespaces)
    offer_list = []
    for noffer in offerings_l:
        offer_dict = create_offer_dict(noffer)
        offer_list.append(offer_dict)
    return offer_list

def pull_capability_data(offer_list):
    with open('debug/offer.csv','w') as fo:
        fo.write("id,org,suborg,stationid,status,parameter,phenombegin,phenomend,resbegin,resend\n")
        unique_offers = []
        for i in offer_list:
            try:
                resbegin = i['resultbegin'][0]
            except IndexError:
                resbegin = ""
            try:
                resend = i['resultend'][0]
            except IndexError:
                resend = ""
            try:
                phenombegin = i['phenombegin'][0]
            except IndexError:
                phenombegin = ""
            try:
                phenomend = i['phenomend'][0]
            except IndexError:
                phenomend = ""
            nid = i['id'][0]
            nid_sp = nid.split(":")
            org=nid_sp[3]
            suborg=nid_sp[4]
            stationid=nid_sp[5]
            status=nid_sp[6]
            try:
                parameter=nid_sp[7]
            except IndexError:
                parameter=""
            fo.write("{},{},{},{},{},{},{},{},{},{}\n".format(
                nid,org,suborg,stationid,status,parameter,phenombegin,phenomend,resbegin,resend))
            try:
                unique_offers.append((stationid,parameter,status,dateutil.parser.parse(phenomend,default=datetime(1950,1,1))))
            except ValueError:
                unique_offers.append((stationid,parameter,status,datetime(1950,1,1).isoformat()))
    return unique_offers

def get_url(sensor_id):
    global url
    if url == None:
        rows = db.query('''
            select o.sos_url from sensors s, organizations o
            where s.organization_id = o.organization_id
            and sensor_id = :id''', id=sensor_id)
        url = rows[0].sos_url

def get_data(sensor_id):
    q = db.query('select org_sensor_id, data_url from sensors where sensor_id = :id', id=sensor_id)
    url = q[0].data_url
    r = urllib.request.urlopen(url)
    open("data/{}.csv".format(sensor_id), 'wb').write(r.read())
    org_sensor_id = q[0].org_sensor_id
    return org_sensor_id

def qa_rules(sensor_id):
    qa = []
    q = db.query('select * from all_sensor_quality_checks where sensor_id = :id', id=sensor_id)
    for r in q:
        qa.append(r.as_dict())
    return qa

def is_qa_applied(sensor_id):
    q = db.query('select qc_rules_apply from sensors where sensor_id = :id', id=sensor_id)
    return q[0].qc_rules_apply

def get_header(sensor_id):
    fieldnames = None
    with open('data/' + str(sensor_id) + '.csv') as csvfile:
        f = csv.DictReader(csvfile)
        fieldnames = f.fieldnames
    return fieldnames

def write_config(sensor_id, org_sensor_id, fields):
    json = '{"type":1,"columns":['
    for n in fields:
        json = json + '"' + n + '",'
    json = json[:-1] + '],"station":"' + org_sensor_id + '","header":1}'
    open('config/' + str(sensor_id) + '.json', 'w').write(json)

def get_station_metadata(sensor_id):
    station = db.query('''
        select stationid, "shortName", "longName", easting, northing, altitude,
        "organizationName", "organizationURL",
	contact, "waterbodyType", "urn-org", suborg
        from sos.all_sensors s where sensor_id = :id''', id=sensor_id)
    return station.as_dict()

def get_parameter_metadata(sensor_id, fields):
    params = []
    parameter = db.query('''
        select parameter_name, unit_name, parameter_column_id,
        lower(data_qualifier_name) as status from all_sensor_parameters where sensor_id = :id''', id=sensor_id)
    for r in parameter:
        d = {'parameter':r.parameter_name,'parameterName':r.parameter_name,'parameterUnit':r.unit_name,'fieldName':fields[r.parameter_column_id - 1],'status':r.status}
        params.append(d.copy())
    return params

def create_station_request(template, stationmeta, parammeta):
    """
    Purpose: Create the text of the xml for a station/sensor
    Input: station meta data (as list of dictionaries)
    Output: text file used for station push
    """
    lookup={
            #'Sequence':stationmeta['Sequence'].lower(),
            'suborg':stationmeta['suborg'].lower(),
            'stationid':stationmeta['stationid'].lower(),
            'shortName':stationmeta['shortName'].lower(),
            'longName':stationmeta['longName'],
            'easting':stationmeta['easting'].lower(),
            'northing':stationmeta['northing'].lower(),
            'altitude':stationmeta['altitude'].lower(),
            'parameter':parammeta['fieldName'].lower(),
            'parameterName':parammeta['parameterName'],
            'parameterUnit':parammeta['parameterUnit'],
            'fieldName':parammeta['fieldName'],
            'organizationName':stationmeta['organizationName'],
            'organizationURL':stationmeta['organizationURL'],
            'contact':stationmeta['contact'],
            'waterbodyType':stationmeta['waterbodyType'],
            'publisher':stationmeta['urn-org'].lower(),
            'status':parammeta['status'].lower(),
            'urn-org':stationmeta['urn-org'].lower()}
    #open the station template file and read the template as a string
    with open(template,'r') as fi:
        station_meta_str = fi.read()

    #the template is coded with lookups for the KEYS from each list element in stationmeta.
    #Create the lookup dictionary for the template LookupError
    #lookup = {k:stationmeta[k].lower() for k in metadata_headers}

    #replace the placeholders with corresponding information from the metadata
    new_station_meta_str = station_meta_str.format(**lookup)
    return new_station_meta_str

def push_template(station_str, url):
    """
    Purpose: Push station or sensor to server
    Input: Station xml, url
    Output: None
    """
    station_bytes = station_str.encode('utf-8')
    req = ur.Request(url)
    req.add_header('Content-Type','application/xml')
    req.add_header('charset','UTF-8')
    r = ur.urlopen(req,data=station_bytes)
    return r

def check_data(data_file,unique_offers,station_status):
    last_record = []
    station_list = [s[0] for s in unique_offers]
    station_match_flag = False
    station_sensor_flag = False

    with open(data_file,'r') as fr:
        r = csv.reader(fr)
        for i, row in enumerate(r):
            if i == 0:
                continue #skip header row
            else:
                station = row[0]
                parameter = row[3]
                #logging.debug("{} - Station: {} Parameter {}".format(i,station,parameter))
                #check if station is in offering
                #stops when it finds a match, because offering should be unique
                if station in station_list:
                    append_value = ("sensor",(station,parameter))
                    for st, par, status, date in unique_offers:
                        if station == st:
                            if parameter == par:
                                if status == station_status:
                                    append_value = ("ok",date)
                                    break
                else:
                    append_value = ("station_sensor",(station,parameter))
                last_record.append(append_value)
    return last_record

def get_unique_station_sensor(data_file,date_filter):
    """
    Input: data_file:csv file
    Output:
    """
    with open(data_file,'r') as fi:
        r = csv.reader(fi)
        # new_csv_list=[]
        # new_csv_list.append(["StationID", "Parameter","NumberOfObs","TimeObsString"])
        station_sensor_list = []
        for i, row in enumerate(r):
            #Do we want to process it?
            if i == 0:
                continue
            else:
                j = i-1
                stationid = row[0]
                parameter = row[3]
                if not date_filter[j]:
                    continue #or do something with it
                else:
                    station_sensor_list.append((stationid,parameter))
        unique_station_sensor = set(station_sensor_list)
    return unique_station_sensor

def check_dates(data_file,last_record):
    date_filter=[]
    with open(data_file,'r') as fi:
        r = csv.reader(fi)
        for i, row in enumerate(r):
            #index offset 1 for last_record list
            j = i-1
            if i == 0:
                continue
            elif last_record[j][0] != 'ok':
                date_filter.append(True)
            else:
                date=row[1]
                time=row[2]
                date_time = dateutil.parser.parse("{} {}".format(date,time))
                #process the date filter
                if date_time > last_record[j][1]:
                    date_filter.append(True)
                else:
                    date_filter.append(False)

    return date_filter

def accumulate_data(unique_station_sensor,data,date_filter):
    rolled_up_data = {}
    last_date = None
    with open(data,'r') as fi:
        r = csv.reader(fi)
        for i, row in enumerate(r):
            j = i-1
            if i == 0:
                continue
            else:
                if date_filter[j] and row[4] != "": #only process row if date_filter is true and value is not missing
                    data_id = (row[0],row[3])  #(stationid,parameter)
                    date_time = dateutil.parser.parse("{} {}".format(row[1],row[2]))
                    data_value = (datetime.isoformat(date_time),row[4])
                    if last_date != date_time:
                        last_date = date_time
                        rolled_up_data.setdefault(data_id, {}).setdefault('values',[]).append(data_value)
    for k,v in rolled_up_data.items():
        count = len(v['values'])
        rolled_up_data[k]['count']=count
    return rolled_up_data

def create_data_request(data_template, k,v,status,urnorg,suborg):
    stationid = k[0]
    parameter = k[1]
    count = str(v['count'])
    values_str = ""
    for item in v['values']:
        values_str += item[0]
        values_str +=","
        values_str += item[1]
        values_str += ";"
    data = count + ";" + values_str


    with open(data_template,'r') as fi:
        data_meta_str = fi.read()
        #replace the placeholders with corresponding information from the metadata
        new_data_meta_str = data_meta_str.format(
                                            stationid=stationid,
                                            parameter=parameter,
                                            status=status,
                                            suborg=suborg,
                                            urnorg=urnorg,
                                            data=data)
    return new_data_meta_str

def push_new_templates(data,last_record,date_filter,stationmeta,parammeta):
    alreadyprocessed = []
    with open(data,'r') as fi:
        for i,row in enumerate(fi):
            j = i-1
            if i == 0:
                continue
            elif not date_filter[j]:
                continue  #skip data that is already in the database (OR DO SOMETHING WITH IT?)
            elif last_record[j] in alreadyprocessed:
                continue
            else:
                #check templates that need to be uploaded
                status = last_record[j][0]
                if status == 'station_sensor':
                    # Get pertinent info
                    station = last_record[j][1][0]
                    parameter = last_record[j][1][1]
                    station_record = None
                    for record in stationmeta:
                        if record['stationid'] == station:
                            station_record = record
                            break
                    if station_record == None:                        
                        continue #OR DO SOMETHING else
                    #Create STATION template
                    station_str = create_station_request(station_meta_template,station_record,parammeta[0])
                    response = push_template(station_str, url)
                    #logger.debug("Station {} template pushed with response {}".format(station,response.readlines()))
                    # PROCESS SENSOR TEMPLATE
                    sensor_record = None
                    sensor_param_record=None
                    for record in stationmeta:
                        if record['stationid'] == station:
                                sensor_record = record
                                break
                    for record in parammeta:
                        if record['fieldName'] == parameter:
                                sensor_param_record = record
                                break
                    if sensor_record == None:
                        continue #OR DO SOMETHING else
                    if sensor_param_record == None:
                        continue
                    #Create sensor str
                    sensor_str = create_station_request(sensor_meta_template,sensor_record,sensor_param_record)
                    response = push_template(sensor_str, url)
                    #logging.debug("Sensor {} template pushed with response {}".format(parameter, response.readlines()))
                    # PROCESS RECORD TEMPLATE
                    result_record = None
                    result_param_record=None
                    for record in stationmeta:
                        if record['stationid'] == station:
                                result_record = record
                                break
                    for record in parammeta:
                        if record['fieldName'] == parameter:
                                result_param_record = record
                                break
                    if result_record == None:
                         continue #OR DO SOMETHING else
                    if result_param_record == None:
                         continue
                    #Create sensor str
                    result_str = create_station_request(result_meta_template,result_record,result_param_record)
                    response = push_template(result_str, url)
                    #logging.debug("Result {} {} template pushed with response {}".format(station, parameter,response.readlines()))
                    alreadyprocessed.append(last_record[j])
                elif status == 'sensor':
                    station = last_record[j][1][0]
                    parameter = last_record[j][1][1]
                    #lookup station parameter in metadata_headers
                    # PROCESS SENSOR TEMPLATE
                    sensor_record = None
                    sensor_param_record=None
                    for record in stationmeta:
                        if record['stationid'] == station:
                                sensor_record = record
                                break
                    for record in parammeta:                       
                        if record['fieldName'] == parameter:
                                sensor_param_record = record
                                break
                    if sensor_record == None:                        
                        continue #OR DO SOMETHING else
                    if sensor_param_record == None:
                        continue
                    #Create sensor str
                    sensor_str = create_station_request(sensor_meta_template,sensor_record,sensor_param_record)
                    response = push_template(sensor_str, url)
                    #logging.debug("Sensor {} template pushed with response {}".format(parameter, response.readlines()))
                    # PROCESS RECORD TEMPLATE
                    result_record = None
                    result_param_record=None
                    for record in stationmeta:
                        if record['stationid'] == station:
                                result_record = record
                                break
                    for record in parammeta:
                        if record['fieldName'] == parameter:
                                result_param_record = record
                                break
                    if result_record == None:
                         continue #OR DO SOMETHING else
                    if result_param_record == None:
                         continue
                    #Create sensor str
                    result_str = create_station_request(result_meta_template,result_record,result_param_record)
                    response = push_template(result_str, url)
                    #logging.debug("Result {} {} template pushed with response {}".format(station, parameter, response.readlines()))
                    alreadyprocessed.append(last_record[j])

def chunk(sensorid,alldatafile):
    with open(alldatafile,'r') as fi:
        num_lines = sum(1 for line in fi)
        if num_lines <= 1:
            logging.error("No data to ingest for sensor Id:{}".format(sensorid))
            exit()
        fi.seek(0)
        r = csv.reader(fi)
        filecount = 0
        counter = 1 #account for header
        eof = False
        next(fi)
        while eof == False:
            filecount += 1
            filename = "{}.{}".format(alldatafile, filecount)
            with open(filename,'w',newline="") as fo:
                w = csv.writer(fo)
                w.writerow(["station","date","time","parameter","value"])
                for i,line in enumerate(r):
                    counter += 1
                    w.writerow(line)
                    if counter == num_lines:
                        eof = True
                    if counter % CSVCHUNKSIZE == 0:
                        break
    
def pivot(sensorid,qa):
    conf_file='config/{}.json'.format(sensorid)
    data_file='data/{}.csv'.format(sensorid)
    if qa != None:
        logging.debug("QA Applied for sensor Id:{}".format(sensorid))
        alldatafile="data/{}.qa.csv".format(sensorid)
    else:
        alldatafile="data/{}.raw.csv".format(sensorid)
        
    with open(conf_file,'r') as fi:
        conf_str = fi.read()
        config = json.loads(conf_str)
        
    with open(data_file,'r') as fi:
        with open(alldatafile,'w', newline="") as fo:
            r = csv.reader(fi)
            w = csv.writer(fo)
            w.writerow(["station","date","time","parameter","value"])
            columns = config['columns']
            station = config['station']
            datetimecol = columns.index("datetime")
            header = config['header']

            for i,ncol in enumerate(columns):
                if ncol == "datetime":
                    continue
                elif ncol == "id":
                    continue
                else:
                    for j,nrow in enumerate(r):
                        if j < header:
                            continue
                        else:
                            newrow = []
                            dateX, timeX = nrow[datetimecol].split(' ',1)
                            newrow.append(station) #station
                            newrow.append(dateX) #date
                            newrow.append(timeX) #time
                            newrow.append(ncol) #parameter
                            discard=False
                            if qa != None:
                                for q in qa:
                                    if q["parameter_column_id"] == i+1:
                                        if eval(nrow[i] + q["quality_check_operand_name"]+str(q["threshold"])):
                                            logging.debug("Discarding sensor id {} value {} for {}".format(sensorid, nrow[i],ncol))
                                            discard=True
                            if discard == False:
                                newrow.append(nrow[i])
                                w.writerow(newrow)
                    fi.seek(0)
    chunk(sensorid,alldatafile)

def update_status(sensorid, status):
    if status == 'complete':
        db.query("update sensors set ingest_status = 'ingested' where sensor_id = :id", id=sensorid)
    if status == 'error':
        db.query("update sensors set ingest_status = :st where sensor_id = :id", st=status, id=sensorid)
    if status == 'ingested':
        db.query("update sensors set ingest_status = :st, last_ingest = now(), next_ingest = now() + (20 * interval '1 minute') where sensor_id = :id", st = status, id=sensorid)

def submit(filelist, parammeta, stationmeta, unique_offers, station_status):
    total_files = len(filelist)
    new_records = 0
    for i,nfile in enumerate(filelist):
        #logging.debug("Processing file {} of {}".format(i+1,total_files))
        # Check data for missing templates
        #loop through the data file and determine what has to be done for each data point
        last_record = check_data(nfile,unique_offers,station_status)        
        #create a list of which dates are before the offering date
        date_filter = check_dates(nfile, last_record) # could clean this up a bit
        #push any new templates that are needed
        push_new_templates(nfile,last_record,date_filter,stationmeta,parammeta)
        #process data, format data and push
        unique_station_sensor = get_unique_station_sensor(nfile,date_filter)
        #logging.debug('unique_station_sensor:{}'.format(unique_station_sensor))
        rolled_up_data = accumulate_data(unique_station_sensor,nfile,date_filter)
        new_records - new_records + len(rolled_up_data)
        if len(rolled_up_data) == 0:
            logging.debug('No NEW data to ingest')
        for k,v in rolled_up_data.items():
            for i in parammeta:
                if k[1] == i['fieldName']:
                    status = i['status'].lower()
                    break
            for i in stationmeta:
                if k[0] == i['stationid']:
                    urnorg = i['urn-org'].lower()
                    suborg = i['suborg'].lower()
                    break
            data_meta_str = create_data_request(data_template, k,v,status,urnorg,suborg)
            response = push_template(data_meta_str,url)
            #logging.debug("-","Results for {} pushed with response {}".format(k,response.readlines()))
    return new_records

def remove_old_files(sensorid):
    filelist = glob("data/{}.*".format(sensorid))
    for nfile in filelist:
        os.remove(nfile)
    
def process(sensorid):
    logging.debug("Ingesting Sensor Id: {}".format(sensorid))
    update_status(sensorid,'running')
    get_url(sensorid)
    remove_old_files(sensorid)
    station = get_data(sensorid)
    #TODO:only if already doesn't exist
    write_config(sensorid, station, get_header(sensorid))

    #Request offering from server. Parse into a list of offerings.
    offer_dict = parse_capabilities(url)

    #Create a list of unique offerings (station, parameter, last measurement date/time)
    unique_offers = pull_capability_data(offer_dict)

    #Read station metadata csv file
    stationmeta = get_station_metadata(sensorid)

    #Read parameter metadata csv file
    parammeta = get_parameter_metadata(sensorid, get_header(sensorid))

    #Process original data
    pivot(sensorid, None)
    filelist = glob("data/{}.raw.csv.*".format(sensorid))
    new_records = submit(filelist, parammeta, stationmeta, unique_offers, parammeta[0]["status"])

    if is_qa_applied(sensorid):
        prelimparammeta = parammeta
        for param in prelimparammeta:
            param["status"] = "preliminary"
        pivot(sensorid, qa_rules(sensorid))
        prelimfilelist = glob("data/{}.qa.csv.*".format(sensorid))
        submit(prelimfilelist, prelimparammeta, stationmeta, unique_offers, "preliminary")
    logging.debug('{} records ingested for {}'.format(new_records,sensorid))
    if new_records > 0:
        update_status(args.sensorid, 'ingested')
    else:
        update_status(args.sensorid, 'complete')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("sensorid", help="system sensor id")
    args = parser.parse_args()
    logging.basicConfig(filename="log/{}.log".format(args.sensorid), level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(message)s")
    try:
        process(args.sensorid)
    except Exception as e:
       update_status(args.sensorid, 'error')
       logging.critical(str(e)) 
       raise       
