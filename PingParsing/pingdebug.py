import pingparsing

def ping_server(server, count):
    ping_parser = pingparsing.PingParsing()
    transmitter = pingparsing.PingTransmitter()
    transmitter.destination = server
    transmitter.count = count  # Number of ping attempts

    try:
        result = transmitter.ping()
        metrics = ping_parser.parse(result).as_dict()
        # Display the results
        display_results(metrics)
    except Exception as e:
        print(f"Error: {e}")

def display_results(metrics):
    print("\nPing Results:")
    print(f"Packets Transmitted: {metrics['packet_transmit']}")
    print(f"Packets Received: {metrics['packet_receive']}")
    print(f"Packet Loss Rate: {metrics['packet_loss_rate']:.2f}%")
    print(f"RTT Min: {metrics['rtt_min']} ms")
    print(f"RTT Avg: {metrics['rtt_avg']} ms")
    print(f"RTT Max: {metrics['rtt_max']} ms")
    print(f"RTT Mdev: {metrics['rtt_mdev']} ms")

def main():
    server = "www.hi-bryan.com"  # Replace with the server you want to test
    count = 4
    ping_server(server, count)

if __name__ == "__main__":
    main()
