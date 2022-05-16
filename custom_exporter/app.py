import http.server
from prometheus_client import start_http_server,Gauge,Counter,Histogram
from flask import Flask
from time import time,sleep
from random import uniform


app = Flask(__name__)

REQUEST_IN_PROGRESS = Gauge("app_requests_in_progress","number of application requests in progress")
REQUEST_LAST_SERVED = Gauge("app_request_last_served","Time the application was last served. ")
REQUEST_COUNT = Counter("app_http_requests_recieved","total all http request count",["app_name","endpoint"])
REQUEST_RESPONSE_TIME = Histogram("app_response_latency_seconds","Response latency in seconds")


@app.route("/")
def hello_world():
    REQUEST_COUNT.labels("my_prom_app","/").inc()
    return "<h1>Hello, World!</h1>"


@app.route("/deployment")
def deployment():
    REQUEST_IN_PROGRESS.inc()
    sleep(10)
    REQUEST_LAST_SERVED.set_to_current_time()
    REQUEST_LAST_SERVED.set(time())
    REQUEST_IN_PROGRESS.dec()
    return "<h1>Deployment Completed !</h1>"

@app.route("/response-test")
def request_test():
        start_time = time()
        sleep(uniform(0,11))
        time_taken = time() - start_time
        REQUEST_RESPONSE_TIME.observe(time_taken)
        return "<h1>Response successful"





if __name__ == "__main__":
    start_http_server(5001)
    app.run(debug=True,use_reloader=False,host="0.0.0.0")
    