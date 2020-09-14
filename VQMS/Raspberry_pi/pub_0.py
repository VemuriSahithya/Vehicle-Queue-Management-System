# MQTT Publish Demo
# Publish two messages, to two different topics

import paho.mqtt.publish as publish

publish.single("test", "0", hostname="192.168.137.220")
print("Done")
