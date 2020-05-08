from pykafka import KafkaClient

class Client:
    def __init__(self):
        self.hosts  = ''
        self.client = KafkaClient(hosts=self.hosts)
