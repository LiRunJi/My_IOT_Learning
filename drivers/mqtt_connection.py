'''
这个部分用来获得mqtt客户端初始化后的对象
把网址封装进去了,这样就不用到处输入网址
给固定的id是为了后续mqtt权限管理啥的.
'''
import paho.mqtt.client as mqtt
from config_files.load_total_project_configs import conf

def get_client(client_id:str=conf['mqtt_client_id']):
    client = mqtt.Client(clean_session=False, client_id=client_id)
    return client

def connect(client):
    client.connect(conf['mqtt_url'],int(conf['mqtt_port']))
    return client

#下面这个应该是没什么用,好像是用来搞一堆mqtt测试并发的,不过现在太菜了,怕是没机会测了
import random
def get_a_new_client(client_id:str="py"+str(random.randint(0,65535))):
    client=mqtt.Client(clean_session=False,client_id=client_id)
    return client
