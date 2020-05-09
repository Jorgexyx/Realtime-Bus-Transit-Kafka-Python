import time
from flask import Flask, Response, render_template
from pykafka import KafkaClient
from TransitKafkaClient import TransitKafkaClient
app = Flask(__name__)
 
@app.after_request
def add_header(r):
    r.headers['Cache-Control'] = 'no-transform'
    return r
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/api/transit')
def getTransitEventStream():
    render_template('index.html')
    client = TransitKafkaClient()
    def event():
        for message in client.consume_message():
            print("sending message: ", message)
            #print(message.value.decode())
            yield 'data:{0}\n\n'.format(message.value.decode())
    return Response(event(), mimetype="text/event-stream")

app.run(debug=True, port=3005)


