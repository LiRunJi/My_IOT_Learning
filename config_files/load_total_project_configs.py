import yaml
# import os
#
# path = os.getcwd()  # 获取当前路径
#
# # print(path)
#
# config_file_path = os.path.join(path, "appConfig.yml")
# print(config_file_path)
import platform
my_ubuntu='#54-Ubuntu SMP Fri Aug 26 13:26:29 UTC 2022'
my_tencent='#1 SMP Wed May 18 16:02:34 UTC 2022'
with open("config_files/appConfig.yml",'r',encoding='utf-8') as f:
    confs = yaml.load(f.read(), Loader=yaml.FullLoader)

#在这里挑选运行对应的服务器配置:
if platform.version()==my_ubuntu:
    conf=confs['on_ubuntu_vm']
    print("on_ubuntu")
elif platform.version()==my_tencent:
    conf=confs['on_win_to_tencent']
    print("on_tencent")
else:
    conf = confs['on_win_to_ubuntu']
    print(f"unknown platform: {platform.version()}")
print()
print(conf)
