# import datetime
# 
# import requests
# import serial #用来规范格式
# import time
# from connection_pool.uart_connection import ble_uart
# import threading
# ble_uart=ble_uart
# 
# '''
# 思路:在该文件中放一些全局变量,
# 对于在逻辑中需要耗时或者是阻塞的事情,可以单独开一个线程
# 对于需要和其它文件共享的全局变量,会被引用出去作为标志位进行判断
# 在这里所有收到的数据都是字典格式,只需要判断里边的逻辑就可以执行操作
# 使用函数中传进来的蓝牙串口,发送消息进行控制
# '''
# 
# #这里的操作被放进大循环中,这个函数外边是个循环
# #像是这样
# #while True:
# #  try:
# # dht1_t=0
# # dht2_t=0
# from pydantic import BaseModel
# from typing import List
# 
# 
# class sensors_data(BaseModel):
#     sensor_name: str
#     name: str
#     type: str
#     value: str
#     time: str
# 
#     class Config():
#         orm_mode = True
# 
# class sensors_datas(BaseModel):
#     class sensors_data(BaseModel):
#         sensor_name: str
#         name: str
#         type: str
#         value: str
#         time: str
#         class Config():
#             orm_mode = True
#     sensors_datas:List[sensors_data]
# 
#     class Config():
#         orm_mode = True
# 
# def send_control_package(id,ff):
#     ctrl='''{'''+f'''
#     "id": {id},
#       "auto_control": 666,
#       "alarm": 666,
#       "ff":{ff},'''+''' "control_instructions": [
#         {
#           "target_name": "string",
#           "instruction": 0
#         }
#       ]
#     }
#     '''
#     ctrl=ctrl.strip()
#     ble_uart.write(ctrl)
#     ble_uart.write(bytes('\n', encoding='utf-8'))
# def get_period():
#     try:
#         url='http://192.168.253.251:443/DianDongChe_BaoJing/get_period'
#         s=requests.get(url)
#         return eval(s.text)
#     except:
#         return None
# 
# print(get_period())
# def ff(msg:dict):
#     try:
#         if msg['local']['ask']==1:
#             p = get_period()
#             if p is None:
#                 return '0'
#             t = datetime.datetime.now()
#             # 在此函数中,所有操作应均为非阻塞的方法
#             which = msg['which']
#             if t >= p[0] and t < p[1]:
#                 return '1'
#             else:
#                 s=sensors_data()
#                 s.sensor_name='ff'+str(which)
#                 s.value="1"
#                 s.time=t
#                 s.name='f'
#                 d=sensors_datas()
#                 d.sensors_datas=[s]
#                 requests.post(url='http://42.192.227.238/DianDongChe_add/one_data',json=d.json())
#                 send_control_package(which, 1)
#     except Exception as e :
#         print(e)
def deal_with_local(msg:dict):
    #ff(msg)

    return '0'


# 