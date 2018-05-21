import csv
import json
import operator as op


CSVCHUNK = 1000

add=op.add
subtract=op.sub
multiply=op.mul
divide=op.truediv

def parse(conf_file,data_file):
    with open(conf_file,'r') as fi:
        conf_str = fi.read()
    config_f = json.loads(conf_str)
    if config_f['type']==1:
        parse1(conf_file,data_file,config_f)

def parse1(conf_file,data_file,config, param=None, maxval=9999999999999):
    with open(data_file,'r') as fi:
        with open('temp/all_data.csv','w', newline="") as fo:
            r = csv.reader(fi)
            w = csv.writer(fo)
            w.writerow(["station","date","time","parameter","value"])
            columns = config['columns']
            station = config['station']
            datetimecol = columns.index("datetime")
            header = config['header']

            for i,ncol in enumerate(columns):
                #print(ncol)
                #if ncol=="ph":
                    #print('hihihi')
                if ncol == "datetime":
                    #print("datesdfsdf")
                    continue
                elif ncol == "id":
                    #print("timelkjsdf")
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
                            if param and param[0] == ncol[0]:
                                new_value = oper(nrow[i],val) # modified value
                                newrow.append(new_value)
                            else:
                                newrow.append(nrow[i]) # raw value
                            w.writerow(newrow)
                    fi.seek(0)
    with open('temp/all_data.csv','r') as fi:
        r = csv.reader(fi)
        filecount = 1
        counter = 1
        eof = False
        next(fi)
        while eof == False:
            eof = True    
            filename = "temp/PART_{}.csv".format(filecount)
            filecount += 1
            with open(filename,'w',newline="") as fo:
                w = csv.writer(fo)
                w.writerow(["station","date","time","parameter","value"])
                
                for i,line in enumerate(r):
                    # if i < counter:
                    #     continue
                    # else:
                        #print(counter)
                    counter += 1
                    w.writerow(line)
                    eof = False
                    if counter % CSVCHUNK == 0:
                        early_break = True
                        break

                


if __name__ == "__main__":
    parse("input/crbuoy.json","refs/crbuoy.csv")           

