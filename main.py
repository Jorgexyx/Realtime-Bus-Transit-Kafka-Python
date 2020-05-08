from TransitKafkaClient import TransitKafkaClient


def main():
    client = TransitKafkaClient()
    client.produce_message("Hello Live Bus Stream!".encode('ascii'))

main()    
