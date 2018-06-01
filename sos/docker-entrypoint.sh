#!/bin/bash
python /tmp/updateconfig.py
cp /tmp/configuration.db /usr/local/tomcat/webapps/52n-sos-webapp/configuration.db
cp /tmp/datasource.properties /usr/local/tomcat/webapps/52n-sos-webapp/WEB-INF/datasource.properties
$CATALINA_HOME/bin/catalina.sh run
