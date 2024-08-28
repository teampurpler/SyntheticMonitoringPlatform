import yaml
import time
import pingparsing
import os

# Function to load the configuration file
def load_config(file_path):
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

# Function to ping the servers and print the metrics
def ping_servers(servers, interval):
    pinger = pingparsing.PingParsing()
    transmitter = pingparsing.PingTransmitter()

    while True:
        for server in servers:
            transmitter.destination = server
            result = transmitter.ping()
            metrics = pinger.parse(result).as_dict()

            print(f"Metrics for {server}:")
            for key, value in metrics.items():
                print(f"{key}: {value}")
            print("-" * 40)

        time.sleep(interval)

if __name__ == "__main__":
    print("Current working directory:", os.getcwd())
    config_path = os.path.abspath('config.yaml')
    print("Config path:", config_path)
    config = load_config(config_path)
    servers = config['servers']
    interval = config['interval']

    ping_servers(servers, interval)

