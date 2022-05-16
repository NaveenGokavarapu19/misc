import http.server
from telnetlib import GA
from prometheus_client import start_http_server,Gauge
from time import sleep
from time import time



APP_PORT = 8000
METRICS_PORT = 8001
REQUEST_IN_PROGRESS = Gauge("app_requests_in_progress","number of application requests in progress")
REQUEST_LAST_SERVED = Gauge("app_request_last_served","Time the application was last served. ")

class HandleRequests(http.server.BaseHTTPRequestHandler):
    @REQUEST_IN_PROGRESS.track_inprogress()
    def do_GET(self):
        #REQUEST_IN_PROGRESS.inc()
        sleep(5)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>First Application</title></head><body style='color: #333; margin-top: 30px;'><center><h2>Welcome to our first Prometheus-Python application.</center></h2></body></html>", "utf-8"))
        self.wfile.close()
        REQUEST_LAST_SERVED.set_to_current_time()
        REQUEST_LAST_SERVED.set(time())
        REQUEST_IN_PROGRESS.dec()

if __name__ == "__main__":
    start_http_server(METRICS_PORT)
    server = http.server.HTTPServer(('localhost', APP_PORT), HandleRequests)
    server.serve_forever()