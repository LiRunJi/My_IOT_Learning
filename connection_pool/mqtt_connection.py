from paho.mqtt import client as mqtt
from configs.read_yaml import conf

client = mqtt.Client(client_id=conf['mqtt_client_id'],clean_session=False)

def connect(client):
    client.connect(conf['mqtt_url'],conf['mqtt_port'])
    return client

def loop_forever(client):
    client.loop_forever()

def get_new_client():
    return mqtt.Client(clean_session=False)
