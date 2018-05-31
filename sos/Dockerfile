FROM 52north/sos:4.3.8
COPY ./configuration.db /tmp/configuration.db
COPY ./datasource.properties /tmp/datasource.properties
COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh
ENTRYPOINT ["docker-entrypoint.sh"] 
