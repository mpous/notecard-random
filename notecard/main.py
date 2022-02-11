import os

import requests
from flask import Flask, render_template, Response, request, jsonify
from flask_socketio import SocketIO, emit
from flask_cors import CORS,cross_origin
import threading

import json
import notecard
import notecard_pseudo_sensor
from periphery import I2C
import time


async_mode = None
runner = None
sysusername = os.environ['USERNAME']
syspassword = os.environ['PASSWORD']


NOTE_FILE = os.environ['noteFile']
PRODUCT_UID = os.environ['productUID']

productUID = "com.blues.tvantoll:weather" #os.environ['productUID']
noteFile = "sensors.qo" #os.environ['noteFile']
card = 0

print(productUID)
print(noteFile)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

CORS(app, resources={ r'/*': {'origins': '*'}}, supports_credentials=True)
socketio = SocketIO(app, async_mode=async_mode,cors_allowed_origins="*")

print("Initializing blues...")

port = I2C("/dev/i2c-1")
card = notecard.OpenI2C(port, 0, 0)
sensor = notecard_pseudo_sensor.NotecardPseudoSensor(card)

req = {"req": "hub.set"}
req["product"] = productUID
req["mode"] = "continuous"

print(json.dumps(req))

rsp = card.Transaction(req)
print(rsp)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/send', methods=['POST'])
def send():

    
    return 


@socketio.on('connect')
def socket_connect():
    token = request.args.get('token')
    print("socket token ", token)
    if is_authenticated(token):
        print("auth succcess")
        return True
    else:
        print("auth NOT success")
        return False
    

@socketio.on('disconnect')
def socket_disconnect():
    print('Client disconnected')

def is_authenticated(token):
    s = base64.b64decode(token).decode('utf-8').split(':')
    username=s[0]
    password=s[1]
    print(username, password)
    if username == sysusername and password == syspassword:
        return True
    else:
        return False



def sendMessage(message):
  global noteFile
  global card

  req = {"req": "note.add"}
  req["file"] = noteFile
  req["sync"] = True
  req["body"] = message

  rsp = card.Transaction(req)
  print(rsp)

 

def main():
  global productUID
  global card

  


if __name__ == "__main__":
    t = threading.Thread(target=main, args=())
    t.daemon = True
    t.start()

    print("Starting blues notecard thread...")
    threading.Thread(target=main,daemon=True).start()

    #app.run(host='0.0.0.0', port='8080', debug=False)
    socketio.run(app,host='0.0.0.0', port='8080', debug=False)


    
    
    #main()