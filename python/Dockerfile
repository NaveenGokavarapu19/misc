FROM  python:alpine3.14

WORKDIR /usr/local/bin

RUN pip3 install prometheus-client

COPY docker-entrypoint /usr/local/bin/

RUN chmod 777 /usr/local/bin/docker-entrypoint

COPY gauge.py /usr/local/bin/

COPY histogram.py /usr/local/bin/

COPY counter.py /usr/local/bin/

COPY summary.py /usr/local/bin/

EXPOSE 8000 8081

ENTRYPOINT ["docker-entrypoint"]

CMD ["-s"]