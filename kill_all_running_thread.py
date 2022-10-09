'''
该脚本用于杀掉位于目标文件夹下的所有python的后台进程,需要管理也权限
因为有时候会占用串口等资源,而且树莓派不想是电脑那么性能过剩,所以没用的时候尽量关
比如说我这边开个pycharm,开个VNC,再开个frpc加上mysql,再运行我自己的脚本,他就受不了了
'''
import os
import subprocess
files_path=[]
#使用的时候请在这里加入要杀的程序在的路径1
files_path.append('/home/pi/Desktop/iot_center/main.py')
#使用的时候请在这里加入要杀的程序在的路径2
files_path.append('/home/pi/Desktop/my_iot_competition/main.py')
# #使用的时候请在这里加入要杀的程序在的路径3...
# file_path.append()

#查询后台进程
cmd = "ps -x|grep python"
res = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
print("查询到路径中文件的后台进程如下:")
# print(res)
'''
查询出来大概是这样,
1050 ?        S      0:00 sudo nohup python3 /home/pi/Desktop/iot_center/main.py 2
1055 ?        Sl     1:35 python3 /home/pi/Desktop/iot_center/main.py 2
'''
pids=[]
for line in res.stdout.readlines():
    l = line.decode("utf-8")
    print(l)
    l = l.split()
    for f in files_path:
        if l[-2] ==f:
            pids.append(l[0])

print("进程号为: ",pids)
for pid in pids:
    os.system(f"sudo kill -9 {pid}")
print("请查看您指定的程序是否被关闭")
os.system(cmd)
