# Interoperable Watershed Network Data Appliance

The IWN data appliance is a collection of open source software components for managing the conversion of sensor data from plain text output to an implementation of the OGC Sensor Observation Service (SOS) specification.  The data appliance owner interacts with a web-based interface to supply attributes related to one or more sensors.  The system polls the sensor’s data periodically based on the period supplied by the user and convert the data values into a format acceptable to the SOS server and submit the data using the web services provided by the SOS server.  All of the components of the data appliance can either be installed separately as necessary or conveniently in one package using Docker containers.

## Components
* Web interface - The web interface is the primary component used by the owner of the data appliance.  It is written using JavaScript.
* Service layer - The web interface interacts with rest web services written using Python and the Flask framework.
* Database - The database that stores the sensor attributes is PostgreSQL.
* Sensor Observation Service (SOS) - The SOS server implementation used is 52North, a java application deployed to Tomcat.
* Conversion/Ingestion - The process of retrieving the sensor data, converting it and submitting it to the SOS server is done using a program written in Python called ingest.py.  The program accepts as an argument the identifier assigned to the sensor at the time of its registration in the system and downloads the sensor data, converts it using templates and submits it using the SOS provided SOAP services.
* Cron scheduling - The conversion and ingestion occur periodically based on the supplied frequency by the user.  This should overlap somewhat with the sensors data being uploaded to the supplied URL.  For example, if the sensors data is uploaded from the sensor every 15 minutes, the frequency supplied for ingestion should occur at least slight more frequent such as 10 minutes to prevent missing any data should the sensors uploaded data be replaced completely instead of appended to.  At sensor registration time, a cron job is submitted for the desired frequency which executes the ingest.py program.
* Containerization - All the components of the data appliance can be started using docker-compose up.

![System Diagram](ingest.png)

## Installation
* Modify configuration as needed:
	* sos/configuration.csv for organization details loaded into SOS application. localhost should be changed to the deployment FQDN.
	* sos/datasource.properties for database connection if not using included PostgreSQL container (such as AWS RDS).
	* src/app/ingest/ingest.py as above.
	* web/scripts/config.js for http link to deployed services API.
* Run docker-compose up

