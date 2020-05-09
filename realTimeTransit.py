import time
import json
import sys
from TransitKafkaClient import TransitKafkaClient
from MetroAPI import MetroAPI


def fetchRouteLocation(stream, route_number):
    transit_data = stream.get_vehicle_location(route_number)
    if len(transit_data) == 0:
        print("Transit is not operating. Exiting \n Available routes are: ")
        print(stream.get_all_vehicle_locations())
        exit()
    return transit_data, [ transit_data["longitude"], transit_data["latitude"]]


def produce_route_location(transit_data, client):
    message = json.dumps(transit_data)
    client.produce_message(message.encode('ascii'))
    print("Produced Message  🌾 ")


def main():
    if len(sys.argv) != 2:
        raise Exception('Please pass in only one argument. the route id')
    route_number = sys.argv[1]

    client    = TransitKafkaClient()
    BusStream = MetroAPI()
    transit_data, current_location = fetchRouteLocation(BusStream, route_number)
    produce_route_location(transit_data, client)

    while True:
        transit_data, location = fetchRouteLocation(BusStream, route_number)       
        if location[0] != current_location[0] or location[1] != current_location[1]:
            current_location - location
            produce_route_location(transit_data, client)
main()    
