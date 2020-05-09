import time
import json
import sys
from TransitKafkaClient import TransitKafkaClient
from MetroAPI import MetroAPI

def main():

    if len(sys.argv) != 2:
        raise Exception('Please pass in only one argument. the route id')
    route_number = sys.argv[1]
    client = TransitKafkaClient()
    BusStream = MetroAPI()
    while True:
        transit_data = BusStream.get_vehicle_location(route_number)
        if len(transit_data) == 0:
            print("Transit is not operating. Exiting \n Available routes are: ")
            print(BusStream.get_all_vehicle_locations())
            return

        message = json.dumps(transit_data)
        client.produce_message(message.encode('ascii'))
        print("Produced Message  🌾 ")

main()    
