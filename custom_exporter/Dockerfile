FROM python:3.8-slim-buster

WORKDIR /usr/local/bin

RUN pip3 install prometheus-client

RUN pip3 install flask

COPY docker-entrypoint /usr/local/bin/

RUN chmod 777 /usr/local/bin/docker-entrypoint

COPY app.py /usr/local/bin/

EXPOSE 5000 5001

#ENTRYPOINT ["/bin/sh","-c","sleep infinity"]

ENTRYPOINT ["python3","app.py"]

#CMD ["-s"]