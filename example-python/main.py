import os
import random
import requests
import time

prodID = os.environ['productID']
fileID = os.environ['fileID']

req = {"req": "hub.set"}
req["product"] = prodID
req["mode"] = "continuous"

url = "http://notecard:3434"
headers = {"Content-Type": "application/json"}
result = requests.post(url, json=req, headers=headers)
print(result.text)

while True:
  random1 = round(random.uniform(0, 100), 4)
  
  req = {"req": "note.add"}
  req["file"] = fileID
  req["sync"] = True
  req["body"] = {"random": random1}

  result = requests.post(url, json=req, headers=headers)
  print(result.text)
 
  time.sleep(15)
