import pingparsing

def ping_server(server):
    ping_parser = pingparsing.PingParsing()
    transmitter = pingparsing.PingTransmitter()
    transmitter.destination = server
    transmitter.count = 4  # Number of ping attempts (common practice)

    result = transmitter.ping()
    metrics = ping_parser.parse(result).as_dict()

    # Display the results
    display_results(metrics)

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
    server = input("Enter the server to ping: ")
    # Call the function to ping the server and display results
    ping_server(server)

if __name__ == "__main__":
    main()
