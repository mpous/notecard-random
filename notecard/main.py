
from lzma import MODE_FAST
import os

from flask import Flask, render_template, Response, request, jsonify
from flask_cors import CORS,cross_origin
import threading

import json
import notecard
import notecard_pseudo_sensor
from periphery import I2C
import time


NOTE_FILE = os.getenv('noteFile')
PRODUCT_UID = os.getenv('productUID')
NOTE_MODE = os.getenv('noteMode')

#productUID = "com.blues.tvantoll:weather" #os.environ['productUID']
#noteFile = "sensors.qo" #os.environ['noteFile']

app = Flask(__name__)

CORS(app, resources={ r'/*': {'origins': '*'}}, supports_credentials=True)

print("Initializing blues...")

port = I2C("/dev/i2c-1")
card = notecard.OpenI2C(port, 0, 0)
sensor = notecard_pseudo_sensor.NotecardPseudoSensor(card)

req = {"req": "hub.set"}
req["product"] = PRODUCT_UID
req["mode"] = NOTE_MODE

print(json.dumps(req))

rsp = card.Transaction(req)
print(rsp)



@app.route('/send', methods=['POST'])
def send():
  print("POST!!!!")
  sendMessage(message)

  return "success"

def sendMessage(message):
  req = {"req": "note.add"}
  req["file"] = NOTE_FILE
  req["sync"] = True
  req["body"] = message

  rsp = card.Transaction(req)
  print(rsp)

def main():
  global card

if __name__ == "__main__":
    t = threading.Thread(target=main, args=())
    t.daemon = True
    t.start()

    print("Starting blues notecard thread...")
    threading.Thread(target=main,daemon=True).start()

    app.run(host='0.0.0.0', port='8080', debug=False)
