'''
使用这个开机自启的脚本需要以下几步:
1.手动把脚本加入到 /etc/rc.local 下
2.把要执行的指令添加到变量区
3.根据条件按顺序执行
4.给当前脚本加上可运行权限(sudo chmod 777 您的脚本 )
或者:
1.以管理员运行同目录下的`commit_auto_start_service.py`文件
2.把要执行的指令添加到变量区
3.根据条件按顺序执行


这个文件会放到 /etc/rc.local 下,
使用方式为在 `exit 0` 前添加这一行代码:
    sudo nohup python3 这个文件的路径 > 期待的日志的路径 2>&1 &

可以看这个例子:
     1	#!/bin/sh -e
     2	#
     3	# rc.local
     4	#
     5	# This script is executed at the end of each multiuser runlevel.
     6	# Make sure that the script will "exit 0" on success or any other
     7	# value on error.
     8	#
     9	# In order to enable or disable this script just change the execution
    10	# bits.
    11	#
    12	# By default this script does nothing.
    13
    14	# Print the IP address
    15	_IP=$(hostname -I) || true
    16	if [ "$_IP" ]; then
    17	  printf "My IP address is %s\n" "$_IP"
    18	fi
    19
    20	sudo nohup python3 /home/pi/Desktop/iot_center/main.py  > /home/pi/Desktop/iot_center/out.log 2>&1 &
    21
    22
    23
    24	exit 0


该脚本会挂到后台执行,不会阻塞开机
由于这个执行的时候联网啥的可能还没连好,
需要联网或者是连局域网的服务可以按照提示放到指定位置
要执行的shell命令也可也使用os.system('运行命令或者你的shell文件')来实现

'''

import time
# import requests
import os

import urllib3

'''
测试是否连接路由器或者wifi
'''


def test_connection_of_wifi():
    import socket
    ipaddress = socket.gethostbyname(socket.gethostname())
    if ipaddress == '127.0.0.1':
        return False
    else:
        return True

print("......")
def wait_util_connected_to_wifi():
    # r=test_connection_of_wifi()
    while True:
        if test_connection_of_wifi() is True:
            break
        time.sleep(1)
        print("......")


'''
测试是否能联网(默认能连百度就能联网)
'''





def wait_util_connected_to_internet():
    import urllib3
    while True:
        try:
            #ret = subprocess.run("ping baidu.com -n 1", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            #print("exit_code")
            http = urllib3.PoolManager()
            http.request('GET', 'https://baidu.com')
            
            break
            #print("???")
        except Exception as e:
            print(e)
            print("还没连上")
            time.sleep(1)
            #print("!!!???")
            # print('connect...')
            continue

def waiting_to_connect_to_LAN():

    while True:
        try:
            #内网开机会自动开启gitlab,默认八零端口会有页面,
            #可作为判断的标志
            http = urllib3.PoolManager()
            http.request('GET', 'https://192.168.254.103')

            break
            # print("???")
        except Exception as e:
            print(e)
            print("还没连上")
            time.sleep(1)
            # print("!!!???")
            # print('connect...')
            continue

    pass
'''
用户自定义指令区:
要执行的指令可以以变量的形式存在这里:
这样以后也方便改
'''
###########################
project_path="/home/pi/Desktop/my_iot_competition/"
project_main="main.py"
# project_python_path=""
project_logsFilePath="/home/pi/Desktop/"
project_logsFile="iot_node_log.txt"
run_project=f"sudo nohup python3 {project_path}{project_main} > {project_logsFilePath}{project_logsFile} 2 >&1 &"
run_node = r"sudo nohup  python3 /home/pi/Desktop/iot_center/main.py > /home/pi/Desktop/iot_center/out.log 2 >&1 &"
stop_frp_vnc = r'sudo systemctl stop frpc '
run_frp_vnc = r'sudo systemctl start frpc '
######################################
print("project will run after 5 sec")
print(run_project)
os.system(run_project)
print("running......")
print("")


###########################
wait_util_connected_to_wifi()
'''
需要连接到WIFI后执行的程序,请放到以下部分
'''
#########################
# os.system()

#########################
wait_util_connected_to_internet()
'''
需要联网后执行的程序,请放到以下部分
'''
########################
#time.sleep(10)
# os.system(run_node)
os.system(stop_frp_vnc)
time.sleep(1)
os.system(run_frp_vnc)

#########################
