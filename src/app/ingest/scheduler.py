from crontab import CronTab
from sys import argv

def add_to_schedule(sensorid, interval):
    cmd = '/app/ingest/run.sh ' + sensorid + ' >>/var/log/cron.log 2>&1'
    ingest_cron = CronTab(user=True)
    job  = ingest_cron.new(command=cmd)
    job.minute.every(interval)
    job.enable()
    ingest_cron.write()

if __name__ == "__main__":
    add_to_schedule(argv[1], argv[2])
