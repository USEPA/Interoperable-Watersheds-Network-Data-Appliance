from crontab import CronTab
from sys import argv

CMD = '/app/ingest/run.sh {} >>/var/log/cron.log 2>&1'

def add_to_schedule(sensor):
    cmd = CMD.format(str(sensor.sensor_id))
    ingest_cron = CronTab(user=True)
    job  = ingest_cron.new(command=cmd)
    if int(sensor.ingest_frequency) > 0 and int(sensor.ingest_frequency) <= 59:
        job.minute.every(sensor.ingest_frequency)
    elif int(sensor.ingest_frequency) == 60:
        job.every(1).hours()
    else:
        return None
    job.enable()
    ingest_cron.write()

def disable(sensor):
    ingest_cron = CronTab(user=True)
    jobs = ingest_cron.find_command(CMD.format(str(sensor.sensor_id)))
    for job in jobs:
        job.enable(False)
    ingest_cron.write()
    
def enable(sensor):
    ingest_cron = CronTab(user=True)
    jobs = ingest_cron.find_command(CMD.format(str(sensor.sensor_id)))
    for job in jobs:
        job.enable(True)
    ingest_cron.write()
    
def update_frequency(sensor):
    ingest_cron = CronTab(user=True)
    jobs = ingest_cron.find_command(CMD.format(str(sensor.sensor_id)))
    for job in jobs:
        if int(sensor.ingest_frequency) > 0 and int(sensor.ingest_frequency) <= 59:
            job.minute.every(sensor.ingest_frequency)
        elif int(sensor.ingest_frequency) == 60:
            job.every(1).hours()
        else:
            return None
    ingest_cron.write()    

def update(sensor):
    ingest_cron = CronTab(user=True)
    jobs = ingest_cron.find_command(CMD.format(str(sensor.sensor_id)))
    for job in jobs:
        update_frequency(sensor)
        if str(sensor.active) == 'true':
            enable(sensor)
        else:
            disable(sensor)
    ingest_cron.write()
    
def remove_from_schedule(sensor):
    ingest_cron = CronTab(user=True)
    jobs = ingest_cron.find_command(CMD.format(str(sensor.sensor_id)))
    for job in jobs:
        ingest_cron.remove(job)
    ingest_cron.write()

class Sensor:
    def __init__(self, id, freq):
        self.sensor_id = id
        self.ingest_frequency = freq
        
if __name__ == "__main__":
    s  = Sensor(argv[1], argv[2])
    add_to_schedule(s)
