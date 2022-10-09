'''
订阅主题,
收到控制串口转发
断线重连

'''
from connection_pool.mqtt_connection import client,connect
client=client
from handler.NetWorkService import get_connecting_flag#判断是否联网的标志位
import time
from connection_pool.uart_connection import ble_uart
import threading

def on_message(client, userdata, msg):
    m=(msg.payload).strip()
    m=m.replace(b'\n',b'')
    print(m)
    n=ble_uart.write(m)
    ble_uart.write(bytes('\n',encoding='utf-8'))
    print(n)

#在此处添加订阅的信息
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe('/SQY/User1/fire2/control')
    client.subscribe('/control_topic')

def working_start():
    while True:
        if get_connecting_flag()==1:
            try:
                global client
                client.on_connect = on_connect
                client.on_message = on_message
                client = connect(client)
                threading.Thread(target=client.loop_forever).start()
                print("MQTT服务开始了")
                break
            except Exception as e:
                print("mqtt裂开了")
                print(e)
        time.sleep(1.5)

