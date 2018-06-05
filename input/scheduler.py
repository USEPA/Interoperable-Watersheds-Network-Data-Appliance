from crontab import CronTab

ingest_cron = CronTab(user=True)
job  = ingest_cron.new(command='/app/ingest/run.sh')
job.minute.every(15)
job.enable()
ingest_cron.write()
