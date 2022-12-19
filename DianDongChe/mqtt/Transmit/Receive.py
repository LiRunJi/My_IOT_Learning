'''
思前想后,决定把这个写成独立运行的小脚本,
这样拆开了不容易挂掉,找bug比较快
有两个想法,一个是不依赖app,直接在这里给写进去,
另一个是用request把包post转发给app
还是用app的好,那个入库自动orm,不用手写一堆列表的索引,
这样这个的作用基本上就是路由了,在这里指定订阅的主题,还要存主题的业务
'''
import time
import json
# from config_files.printing_config import print_debugger as print
from drivers.mqtt_connection import get_client,connect
from config_files.load_total_project_configs import conf
import requests

def print(str):
    pass

'''加载驱动'''
client = get_client()   #拿一个client
'''
从配置文件中加载配置
'''
test_connection_url=conf['mqtt_bridge']['test_connection_url']
data_post_url=conf['mqtt_bridge']['data_post_url']
data_interfaces=conf['mqtt_bridge']['topic_to_subscribe']
#===========要订阅的主题放在这里===============
#要订阅的主题放在下边,一行一个
# data_interfaces = []
# data_interfaces.append("/ShaoLinSi/add_data")
#↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓要写的数据库的逻辑放在这里↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓==========
from DianDongChe.Dao import SensorsDao
from DianDongChe.models.Sensor import sensors_data as model_sensor_data
from DianDongChe.models import Sensor
from drivers.db_connection import get_session
db=get_session()
import datetime

def add_lots_of_data_by_name(datas_json):
    for data_json in datas_json:
        print(data_json)
        print('------------')
        try:
            if data_json["time"] is None or data_json["time"]=="":
                data_json['time'] = str(datetime.datetime.now())
            id=SensorsDao.get_id_by_name(data_json["sensor_name"],db)
            if id is None:
                continue

            one_data = Sensor.sensors_data(
                                           sensor_id=id,
                                           name=data_json["name"],
                                           type=data_json["type"],
                                           value=data_json["value"],
                                           time=data_json["time"]
                                           )
            SensorsDao.add_one_data(one_data, db)
        except Exception as e:
            print(e)
            print(f'''{data_json["sensor_name"]} not succeed ''')



#↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
#====================================连接要用的回调函数===============================================================
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    global data_interfaces
    print(data_interfaces)
    for interface in data_interfaces:
        client.subscribe(interface)
        print(f"INFO: 订阅了{interface}主题")

def on_message(client, userdata, msg):
    # print(msg.topic + " " + str(msg.payload))
    if msg.topic in data_interfaces:
        try:
            #好像还不能用str方法,因为加载的是一个字典,但是eval有个坏处
            #eval是直接直行了,万一谁故意发一些奇怪的东西,就执行了,就寄了
            m=eval(msg.payload)

            add_lots_of_data_by_name(m['sensor_datas'])
            print()
            print()
            #requests.post(url=data_post_url,data=json.dumps(m),verify=False,headers={'Connection': 'close'})
        except Exception as ex:
            print("数据没存到表里")
            print(ex)

def waiting_util__app_working():
    print('正在尝试连接...')
    headers = {
        'Accept': "application/json, text/plain, */*",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    }
    requests.DEFAULT_RETRIES = 5  # 增加重试连接次数
    s = requests.session()
    s.keep_alive = False  # 关闭多余连接
    # s.proxies = {"https": "127.0.0.1:8080", "http": "127.0.0.1:8080", }
    while True:
        try:
            if s.get(test_connection_url, headers=headers).status_code == 200:
                break

        except Exception as e:
            print('连接中...')
            print(e)
            time.sleep(1)
        time.sleep(1)
    # print("")

    print('INFO:MQTT_Router_Working......')

def run_mqtt():
    # waiting_util__app_working()
    global client
    client.on_connect = on_connect
    client.on_message = on_message
    client = connect(client)
    client.loop_forever()
#==================================================================================================================
# if __name__ == '__main__':
#     run_mqtt()
#     pass






