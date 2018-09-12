from __future__ import print_function
from threading import Timer
import requests
from flask import Flask

app = Flask(__name__)

def timeout():
    print("Alarm!")

@app.route('/')
@app.route('/index')
def index():
    return "Hello, world!"

@app.route('/stream-heartbeat', methods=['PUT'])
def get_heartbeat():
    if request.method=='PUT':
        t.cancel()
        t.start()
    
t = Timer(120.0, timeout)
t.start()

# url = "http://127.0.0.1:5000/stream-heartbeat"
# response = requests.put(url, data={'stream': 'thisStream'})
# print(response)
