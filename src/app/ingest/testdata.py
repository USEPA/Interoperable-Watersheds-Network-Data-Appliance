import csv
import datetime
import os
from glob import glob
from random import randrange, uniform
from sys import argv

def create_test_data(sensor_id):
    filelist = glob("/app/logs/" + sensor_id + ".csv")
    for nfile in filelist:
        os.remove(nfile)
    with open('/app/logs/' + sensor_id + '.csv','w', newline="") as fo:
        w = csv.writer(fo)
        w.writerow(['id','datetime','e_coli','nitrate','oil','tss'])
        for n in range(59,-1,-1):
            id = abs(n-60)
            d = str(datetime.datetime.now() - datetime.timedelta(minutes=n*1)) + '+00'
            e = uniform(3500,5500)
            n = uniform(0,1)
            o = uniform(0,5)
            t = uniform(1,10)
            w.writerow((id,d,e,n,o,t))

if __name__ == "__main__":
    create_test_data(argv[1])
