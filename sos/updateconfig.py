import csv
import sqlite3

conn = sqlite3.connect('/tmp/configuration.db')
c = conn.cursor()

with open('/tmp/configuration.csv') as csvfile:
	configreader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in configreader:
		if row[0] == 'service.sosUrl' or row[0] == 'serviceProvider.site':
			c.execute('update uri_settings set value = ? where identifier = ?', (row[1],row[0]))
		else:
			c.execute('update string_settings set value = ? where identifier = ?', (row[1],row[0]))
conn.commit()
conn.close()

