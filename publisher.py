import paho.mqtt.client as mqtt
import time

#Interface Manager
MQTT_HOST= "100.100.1.254"
MQTT_PORT = 3000
MQTT_KEEPALIVE_INTERVAL = 5
MQTT_TOPIC = "webapp/get"
MQTT_MSG = "Hello MQTT"

#Define on_connect event handler
def on_connect(mosq, obj, rc):
	print("Connected to the MQTT broker")

#Define publish events
def on_publish(client, user,mid):
	print "Message published"

#Initiate MQTT client
mqttc = mqtt.Client()

#Register event handlers
mqttc.on_publish = on_publish
mqttc.on_connect = on_connect

#connect with MQTT broker
mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)

#publish message to MQTT topic
mqttc.publish(MQTT_TOPIC, MQTT_MSG)

#disconnect from the mqtt broker
mqttc.disconnect()


