import json
import pingparsing

ping_parser = pingparsing.PingParsing()
transmitter = pingparsing.PingTransmitter()
transmitter.destination = "google.com"
transmitter.count = 10
result = transmitter.ping()

print(json.dumps(ping_parser.parse(result).as_dict(), indent=4))