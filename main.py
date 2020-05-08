import time
import json
from TransitKafkaClient import TransitKafkaClient
from MetroAPI import MetroAPI

def main():
    client = TransitKafkaClient()
    BusStream = MetroAPI()
    while True:
        transit_data = BusStream.get_vehicle_location()
        message = json.dumps(transit_data)
        client.produce_message(message.encode('ascii'))
        time.sleep(.5)

main()    
