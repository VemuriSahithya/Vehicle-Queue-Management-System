# MQTT Client demo
# Continuously monitor two different MQTT topics for data,
# check if the received data matches two predefined 'commands'
 
import paho.mqtt.client as mqtt
 
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
 
    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("test")
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    info=msg.payload.decode()
    if str(info) == '1':
        print("1")
        client.disconnect()
    else:
        print("0")
        client.disconnect()
        # Do somethinng

 
# Create an MQTT client and attach our routines to it.
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect("192.168.137.220", 1883, 60)
 
# Process network traffic and dispatch callbacks. This will also handle
# reconnecting. Check the documentation at
# https://github.com/eclipse/paho.mqtt.python

# for information on how to use other loop*() functions
client.loop_forever()