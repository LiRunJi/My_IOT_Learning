import yaml
import platform
# ubuntu='#54-Ubuntu SMP Fri Aug 26 13:26:29 UTC 2022'
# tencent='#1 SMP Wed May 18 16:02:34 UTC 2022'
with open("config_files/appConfig.yml",'r',encoding='utf-8') as f:
    confs = yaml.load(f.read(), Loader=yaml.FullLoader)
'''
在腾讯云服务器上和Windows上还有虚拟机上边是三套不同的配置,
通过platform库进行区分,以加载相应不同的配置
'''
if platform.system()=="Windows":
    conf = confs['on_win_to_tencent']
    # print(f"{platform.version()}")
else:
    if platform.version().__contains__("Ubuntu"):
        conf = confs['on_ubuntu_vm']
        print("on_ubuntu")
    else:
        conf = confs['on_win_to_tencent']
        print("on_tencent")

print()
print(conf)
