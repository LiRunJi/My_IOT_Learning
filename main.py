
from connection_pool.uart_connection import ble_uart
print(-1)
from handler.HttpService import send_http
print(-2)
from handler.LocalService import deal_with_local
print(-3)
import json
import threading
'''
加载一堆进程
'''
from handler.NetWorkService import refresh_http_flag
print(-4)
from handler.DBService import send_unsent_datas_in_db
print(-5)
from handler.MqttService import working_start
print(-6)
#开启刷新连接到服务器标志位的线程
print(-7)
threading.Thread(target=refresh_http_flag).start()
#开启联网就上传断网数据的线程
print(-8)
threading.Thread(target=send_unsent_datas_in_db).start()
print(-9)
#开启mqtt接收控制的线程
threading.Thread(target=working_start).start()
print(-10)



#与硬件的通信格式
ble_return={
    "id":0,
    "local":{},
    "http":0
}
while True:
    try:
        message=ble_uart.read_until()
        # if message==b'\xff':
        #     continue
        message=message.strip()
        if message is not None and message!=b'':
            message=eval(message)#解析消息成为字典
            print(message)
            ble_return['id']=message['id']
            #http透传
            try:
                ble_return['http'] =send_http(message['http'])
            except Exception as e:
                ble_return['http']='e'
                print("最外层,http出问题")
            #处理不需要联网的事情
            try:
                ble_return['local'] =deal_with_local(message)
            except Exception as e:
                print("最外层,本地出问题")
                ble_return['local']='e'
            #发送返回的消息
            try:
                n = ble_uart.write(bytes(json.dumps(ble_return),encoding='utf-8'))
                ble_uart.write(bytes('\n',encoding='utf-8'))
                print("写了n个字节")
            except Exception as e:
                print("最外层,串口出问题")
    except Exception as e:
        print(e)
        print("读收到的消息出问题")

