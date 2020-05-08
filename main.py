from TransitKafkaClient import TransitKafkaClient
from MetroAPI import MetroAPI

def main():
    client = TransitKafkaClient()
    client.produce_message("Hello Live Bus Stream!".encode('ascii'))
    BusStream = MetroAPI()
    BusStream.get_vehicle_locations()

main()    
