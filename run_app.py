'''
运行该app,
默认在80端口运行,也可以在命令行中指定端口运行
例如:
    python3 run_app.py 443
'''
import os
import sys
if len(sys.argv)<2:
    os.system("sudo nohup /usr/local/bin main:app --host '0.0.0.0' --port 80 &")
else:
    os.system(f"sudo nohup /usr/local/bin main:app --host '0.0.0.0' --port {sys.argv[1]} &")