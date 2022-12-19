import datetime

directory=r'/home/My_IOT_Learning/'
"cd /home/my_iot_competition/;python3 run_app.py"
'''
使用这个开机自启的脚本需要以下几步:
1. 在上边输入您放置该程序的目录
2. 手动把脚本加入到 /etc/rc.local
您可以使用这条指令 nano /etc/rc.local
然后在 `exit 0` 前添加这一行代码:
    例如 sudo nohup python3 /home/ryan/Desktop/iot/auto_start_app.py &
    sudo nohup python3 <您的路径>auto_start_app.py &
    sudo nohup python3 /home/my_iot_competition/auto_start_app.py &
    
    如果使用的是centos系统,可以运行该博客中的内容激活rc.local
    https://blog.csdn.net/x356982611/article/details/90414752
    
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
    20	 sudo nohup python3 /home/ryan/Desktop/iot/auto_start_app.py &
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

#这个app需要在emqx启动后,且可以联网时启动,会调用这个函数等待运行结束
def wait_util_connected_to_internet():
    import urllib3
    while True:
        try:
            http = urllib3.PoolManager()
            http.request('GET', 'https://baidu.com')

            break
            # print("???")
        except Exception as e:
            print(e)
            print("还没连上")
            time.sleep(1)
            # print("!!!???")
            # print('connect...')
            continue

'''
用户自定义指令区:
要执行的指令可以以变量的形式存在这里:
这样以后也方便改
'''
###########################

###########################

'''
需要连接到WIFI后执行的程序,请放到以下部分
'''
#########################
# os.system()

#########################
wait_util_connected_to_internet()
print("connected to internet")
'''
需要联网后执行的程序,请放到以下部分
'''
########################

os.system("sudo emqx start")
time.sleep(20)
cmd=f"cd {directory};/usr/local/bin/python3.10 run_app.py"
os.system(cmd)
os.system(f"echo {datetime.datetime.now()}\n >{directory}auto_start_time.txt")


#########################
