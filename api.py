from flask import Flask, Response
from pykafka import KafkaClient
from TransitKafkaClient import TransitKafkaClient
app = Flask(__name__)
    
@app.route('/api/transit')
def getTransit():
    client = TransitKafkaClient()
    def getMessage():
        for message in client.consume_message():
            yield message.value.decode()
    return Response(getMessage(), mimetype="text/event-stream")

app.run(debug=True, port=3005)


