import serial #用来规范格式
import time
from connection_pool.uart_connection import ble_uart
import threading
ble_uart=ble_uart

'''
思路:在该文件中放一些全局变量,
对于在逻辑中需要耗时或者是阻塞的事情,可以单独开一个线程
对于需要和其它文件共享的全局变量,会被引用出去作为标志位进行判断
在这里所有收到的数据都是字典格式,只需要判断里边的逻辑就可以执行操作
使用函数中传进来的蓝牙串口,发送消息进行控制
'''

#这里的操作被放进大循环中,这个函数外边是个循环
#像是这样
#while True:
#  try:
dht1_t=0
dht2_t=0
def deal_with_local(msg:dict):
    #在此函数中,所有操作应均为非阻塞的方法

    return '1'


