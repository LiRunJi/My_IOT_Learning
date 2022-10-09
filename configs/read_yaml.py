'''
根据运行平台加载配置文件
'''
import yaml
import platform
#file='/home/pi/Desktop/my_iot_competition/configs/configs.yaml'
with open('configs/configs.yaml','r',encoding='utf-8') as f:
    confs = yaml.load(f.read(), Loader=yaml.FullLoader)

if platform.system() == "Windows":
    conf = confs['to_tencentCloud']
else:
    conf = confs['to_tencentCloud']

print("本次加载的配置文件: ")
print(conf)
