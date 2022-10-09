import os
#您的自启动文件的位置:
auto_start_service_file="/home/pi/Desktop/my_iot_competition/auto_start_service.py"
os.system("sudo chmod 777 "+auto_start_service_file)
file="#!/bin/bash \n"+\
    '''sudo nohup /usr/bin/python3.9  '''+\
    auto_start_service_file+\
    '''  > /home/pi/Desktop/auto_start.log 2>&1  &\r\n'''+\
     "exit 0 \n"
print(file)

with open('/etc/rc.local','w',encoding='utf-8') as rl:
    rl.write(file)
    rl.close()