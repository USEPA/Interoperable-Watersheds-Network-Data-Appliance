import csv
import datetime
import os
from glob import glob
from random import randrange, uniform
from sys import argv

def create_test_data(sensor_id):
    filelist = glob("/opt/testdata/" + sensor_id + ".csv")
    for nfile in filelist:
        os.remove(nfile)
    with open('/opt/testdata/' + sensor_id + '.csv','w', newline="") as fo:
        w = csv.writer(fo)
        w.writerow(['id','datetime','e_coli','nitrate','oil','tss'])
        for n in range(15,-1,-1):
            id = abs(n-16)
            d = datetime.datetime.now() - datetime.timedelta(minutes=n*10)
            e = uniform(0,5000)
            n = uniform(0,1)
            o = uniform(0,5)
            t = uniform(1,10)

            #row = str(id) + ',' + str(d) + ',' + str(e) + ',' + str(n) + ',' + str(o) + ',' + str(t)
            w.writerow((id,d,e,n,o,t))

if __name__ == "__main__":
    create_test_data(argv[1])
