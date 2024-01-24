from paho.mqtt import client as mqtt_client

broker = "192.168.86.216"
port = 1883
topic = "LV10/Python"

def connect_mqtt():
    client = mqtt_client.Client("PythonPubMarkoA")
    client.connect(broker, port)
    return client

def run():
    client = connect_mqtt()
    client.loop_start()
    client.publish(topic, "Marko je najbolji!")
    client.loop_stop()

run()