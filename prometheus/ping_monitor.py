import os
import time
from prometheus_client import start_http_server, Gauge
import subprocess

# Create a Prometheus Gauge metric to track the ping response time
ping_latency = Gauge('ping_latency_seconds', 'Ping latency in seconds', ['host'])

def ping_host(host):
    """
    Pings a host and returns the latency in seconds.
    """
    try:
        # Ping command for different OS
        if os.name == 'nt':  # Windows
            output = subprocess.check_output(['ping', '-n', '1', host], stderr=subprocess.STDOUT, universal_newlines=True)
            latency = float(output.split('Average = ')[1].split('ms')[0]) / 1000.0
        else:  # Linux and Mac
            output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, universal_newlines=True)
            latency = float(output.split('time=')[1].split(' ')[0]) / 1000.0
        return latency
    except subprocess.CalledProcessError:
        return None

def monitor():
    # Start the Prometheus HTTP server on port 8000
    start_http_server(8000)
    host = 'github.com'  # Replace with the host you want to ping

    while True:
        latency = ping_host(host)
        if latency is not None:
            ping_latency.labels(host=host).set(latency)
        else:
            # If the ping fails, set the latency to -1
            ping_latency.labels(host=host).set(-1)
        
        time.sleep(5)  # Wait for 5 seconds before the next ping

if __name__ == '__main__':
    monitor()
