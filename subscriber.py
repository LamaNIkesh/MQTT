import paho.mqtt.client as mqtt
import time




#Interface Manager
#Your broker IP
MQTT_HOST= "100.100.1.254"
MQTT_PORT = 3000
MQTT_KEEPALIVE_INTERVAL = 5
MQTT_TOPIC = "webapp/get"


#Define on_connect event handler
def on_connect(mosq, obj,flags, rc):
	#subscribe to the topic
	mqttc.subscribe(MQTT_TOPIC, 0)


#Define on_subscribe event handler
def on_subscribe(mosq, obj, mid, granted_qos):
	print "Subscribed to MQTT Topic"

#define on_message event Handler
def on_message(mosq, obj, msg):
	print msg.payload

#Initiate MQTT client
mqttc = mqtt.Client()

#Register event handlers
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe


#connect with MQTT broker
mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)

#continue the network loop
mqttc.loop_forever()


