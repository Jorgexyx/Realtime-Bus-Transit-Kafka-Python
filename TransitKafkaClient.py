from pykafka import KafkaClient

class TransitKafkaClient:
    def __init__(self):
        self.hosts  = 'localhost:9092'
        self.client = KafkaClient(hosts=self.hosts)

    def get_clients(self):
        return self.client.topics

            
