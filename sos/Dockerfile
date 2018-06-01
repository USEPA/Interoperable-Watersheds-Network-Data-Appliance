FROM 52north/sos:4.3.8
COPY ./updateconfig.sh /tmp/updateconfig.sh
COPY ./configuration.db /tmp/configuration.db
COPY ./configuration.csv /tmp/configuration.csv
COPY ./datasource.properties /tmp/datasource.properties
COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh
ENTRYPOINT ["docker-entrypoint.sh"] 
