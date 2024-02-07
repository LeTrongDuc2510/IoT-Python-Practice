import sys
import random
import time
from Adafruit_IO import MQTTClient

from private_Info import *
# this file stores the private info
# 1. AIO_FEED_ID
# 2. AIO_USERNAME 
# 3. AIO_KEY



def connected(client):
    print("Ket noi thanh cong...")
    client.subscribe(AIO_FEED_ID)

def subscribe(client, userdata, mid, granted_qos):
    print("Subcribe thanh cong...")

def disconnected(client):
    print("Ngat ket noi...")
    sys.exit(1)

def message(client, feed_id, payload):
    print("Nhan du lieu " + payload)

client = MQTTClient ( AIO_USERNAME , AIO_KEY )
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

while True :
    temp = random.randint(0,50)
    print("Update temp : ", temp)
    client.publish(AIO_FEED_ID, value = temp)
    time.sleep(2)