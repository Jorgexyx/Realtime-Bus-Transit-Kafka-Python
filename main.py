import time
import json
import sys
from TransitKafkaClient import TransitKafkaClient
from MetroAPI import MetroAPI

def main():

    if len(sys.argv) != 2:
        raise Exception('Please pass in only one argument. the route id')

    client = TransitKafkaClient()
    BusStream = MetroAPI()
    while True:
        transit_data = BusStream.get_vehicle_location()
        message = json.dumps(transit_data)
        client.produce_message(message.encode('ascii'))
        time.sleep(.5)

main()    
