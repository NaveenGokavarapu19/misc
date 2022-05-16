FROM  python:alpine3.14

WORKDIR /home/alertmanager

ADD  https://github.com/prometheus/alertmanager/releases/download/v0.24.0/alertmanager-0.24.0.linux-amd64.tar.gz /home/alertmanager

RUN set -eux; \
  tar -xvf *.tar.gz && rm *.tar.gz
 
RUN mv alert* alertmanager-extracted

RUN cp  /home/alertmanager/alertmanager-extracted/alertmanager /usr/local/bin

RUN cp  /home/alertmanager/alertmanager-extracted/alertmanager.yml /usr/local/bin

# COPY docker-entrypoint /usr/local/bin/

# RUN chmod 777 /usr/local/bin/docker-entrypoint

# RUN mkdir /home/prometheus/persistent

EXPOSE 9093

ENTRYPOINT ["alertmanager","--config.file=/usr/local/bin/alertmanager.yml"]



