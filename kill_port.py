'''
杀掉占用指定端口的程序
如果程序占用后台的80端口,运行后程序将关闭
例如:
    python3 kill_port.py 80
'''
import os
import subprocess
import sys
if len(sys.argv)<2:
    print("您未输入参数,请重新输入")
    sys.exit(1)

port=sys.argv[1]
cmd = f"netstat -tunlp|grep 0.0.0.0:{port}"

res = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)

pid_port = 0
for line in res.stdout.readlines():
    l = line.decode("utf-8")
    l = l.split()

    if l[3] == f'0.0.0.0:{port}':
        pid_port = l[len(l) - 1].split('/')[0]
        # print('80端口,进程: '+pid_80)

if type(pid_port) == str:
    os.system("kill -9  " + pid_port)
    print(f'{port}端口,进程: ' + pid_port + ' 已关闭,查看以确认是否关闭成功')
else:
    print("没找到,请手动关闭")
os.system(f"netstat -tunlp|grep {port}")

