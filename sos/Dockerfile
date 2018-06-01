FROM 52north/sos:4.3.8
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip
COPY ./updateconfig.py /tmp/updateconfig.py
COPY ./configuration.db /tmp/configuration.db
COPY ./configuration.csv /tmp/configuration.csv
COPY ./datasource.properties /tmp/datasource.properties
COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh
ENTRYPOINT ["docker-entrypoint.sh"] 
