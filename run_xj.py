
from connection_pool.uart_connection import ble_uart
from handler.XunJian import send_http

import threading
'''
加载一堆进程
'''

from tkGUI.tkGui import ui_main
#开启巡检装置



#与硬件的通信格式
ble_return={
    "id":0,
    "local":{},
    "http":0
}
def refresh():
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
                send_http(message['http'])

        except Exception as e:
            print(e)
            print("读收到的消息出问题")

threading.Thread(target=refresh).start()
ui_main()