import yaml
import time
import pingparsing
import os
from prometheus_client import start_http_server, Gauge

# Function to load the configuration file
def load_config(file_path):
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

# Function to initialize Prometheus metrics
def setup_prometheus_metrics(servers):
    metrics = {
        'packet_loss': Gauge('ping_packet_loss_percentage', 'Packet loss percentage', ['server']),
        'avg_rtt': Gauge('ping_rtt_avg_ms', 'Average round-trip time in ms', ['server']),
        'min_rtt': Gauge('ping_rtt_min_ms', 'Minimum round-trip time in ms', ['server']),
        'max_rtt': Gauge('ping_rtt_max_ms', 'Maximum round-trip time in ms', ['server']),
        'stddev_rtt': Gauge('ping_rtt_stddev_ms', 'Standard deviation of round-trip time in ms', ['server']),
    }
    # Initialize metrics with default values
    for metric in metrics.values():
        for server in servers:
            metric.labels(server=server).set(0)
    return metrics

# Function to ping the servers and update Prometheus metrics
def ping_servers(servers, interval, metrics):
    pinger = pingparsing.PingParsing()
    transmitter = pingparsing.PingTransmitter()

    while True:
        for server in servers:
            transmitter.destination = server
            result = transmitter.ping()
            if result is not None:
                parsed = pinger.parse(result).as_dict()
                # Update Prometheus metrics
                metrics['packet_loss'].labels(server=server).set(parsed.get('packet_loss', 100))
                metrics['avg_rtt'].labels(server=server).set(parsed.get('rtt_avg', 0))
                metrics['min_rtt'].labels(server=server).set(parsed.get('rtt_min', 0))
                metrics['max_rtt'].labels(server=server).set(parsed.get('rtt_max', 0))
                metrics['stddev_rtt'].labels(server=server).set(parsed.get('rtt_stddev', 0))

                # Optional: Print metrics to console for debugging
                print(f"Metrics for {server}:")
                for key, value in parsed.items():
                    print(f"{key}: {value}")
                print("-" * 40)
            else:
                # If ping fails, set packet loss to 100%
                metrics['packet_loss'].labels(server=server).set(100)
                metrics['avg_rtt'].labels(server=server).set(0)
                metrics['min_rtt'].labels(server=server).set(0)
                metrics['max_rtt'].labels(server=server).set(0)
                metrics['stddev_rtt'].labels(server=server).set(0)
                print(f"Failed to ping {server}")
        time.sleep(interval)

if __name__ == "__main__":
    # Debugging: Print current directory and files
    print("Current working directory:", os.getcwd())
    print("Files in current directory:", os.listdir('.'))

    # Load configuration
    config_path = 'config.yaml'  # Ensure this file is in the same directory
    config = load_config(config_path)
    servers = config['servers']
    interval = config['interval']

    # Setup Prometheus metrics
    metrics = setup_prometheus_metrics(servers)

    # Start Prometheus metrics server on port 8000
    start_http_server(8000)
    print("Prometheus metrics server started on port 8000")

    # Start pinging servers and updating metrics
    ping_servers(servers, interval, metrics)

