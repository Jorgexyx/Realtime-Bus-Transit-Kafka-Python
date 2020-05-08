from TransitKafkaClient import TransitKafkaClient


def main():
    client = TransitKafkaClient()
    print(client.get_clients())

main()    
