'''
断网重连,
mqtt客户端断线重连
*校准时间?
'''
from configs.read_yaml import conf

import time
import requests
import threading

connecting_flag:int=0
def refresh_http_flag():
    global connecting_flag
    while True:
        try:
           requests.get(conf['test_page'])
           # print("网络已连接")
           connecting_flag=1
        except Exception as e:
            print("没联网")
            connecting_flag=0
        time.sleep(1.5)

# threading.Thread(target=refresh_http_flag).start()

def get_connecting_flag():
    return connecting_flag