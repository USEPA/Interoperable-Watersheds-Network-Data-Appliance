from crontab import CronTab
from sys import argv

CMD = '/app/ingest/run.sh {} >>/var/log/cron.log 2>&1'

def add_to_schedule(sensor):
    ingest_cron = CronTab(user=True)
    cmd = CMD.format(str(sensor.sensor_id))
    job  = ingest_cron.new(command=cmd)
    if int(sensor.ingest_frequency) > 0 and int(sensor.ingest_frequency) <= 59:
        job.minute.every(sensor.ingest_frequency)
    elif int(sensor.ingest_frequency) == 60:
        job.every(1).hours()
    else:
        return None
    if str(sensor.active) == 'true':
        job.enable(True)
    else:
        job.enable(False)
    ingest_cron.write()

def remove_from_schedule(sensor):
    ingest_cron = CronTab(user=True)
    jobs = ingest_cron.find_command(CMD.format(str(sensor.sensor_id)))
    for job in jobs:
        ingest_cron.remove(job)
    ingest_cron.write()

def update(sensor):
    remove_from_schedule(sensor)
    add_to_schedule(sensor)

class Sensor:
    def __init__(self, id, freq, act):
        self.sensor_id = id
        self.ingest_frequency = freq
        self.active = act
        
if __name__ == "__main__":
    s  = Sensor(argv[1], argv[2], argv[3])
    add_to_schedule(s)
    update(s)