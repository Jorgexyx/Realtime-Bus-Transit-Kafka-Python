from pykafka import KafkaClient

"""
@description: 
    A Kafka Client to manage the producer and consumer
    for the transit data.

@required
    Have a kafka topic called: liveBusData (look at README for creaing kafka topic)
    
@todo
    - Add producer
    - Add consumer
"""
class TransitKafkaClient:
    def __init__(self):
        self.topic_name = 'liveBusData'
        self.hosts      = 'localhost:9092'
        self.client     = KafkaClient(hosts=self.hosts)
        self.topic      = self.client.topics[self.topic_name] 
        self.producer   = self.topic.get_sync_producer()

    def get_clients(self):
        return self.client.topics

    def produce_message(self, message):
        self.producer.produce(message)

