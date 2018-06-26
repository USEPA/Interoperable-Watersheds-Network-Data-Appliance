from crontab import CronTab
from sys import argv
from utils.exception import CronException

def add_to_schedule(sensor):
    cmd = '/app/ingest/run.sh ' + str(sensor.sensor_id) + ' >>/var/log/cron.log 2>&1'
    ingest_cron = CronTab(user=True)
    job  = ingest_cron.new(command=cmd)
    job.minute.every(sensor.ingest_frequency)
    job.enable()
    try:
        ingest_cron.write()
    except CronException as err:
        raise CronException('Error adding to cron', sensor)

if __name__ == "__main__":
    add_to_schedule(argv[1], argv[2])
