'''
这个模块用于各种数据格式转换
'''
from models_and_schemas.models import sensors_data
from typing import List

def change_data_objs_to_json(data_objs:List[sensors_data]):
    sensor_datas_to_web1=[]
    for da in data_objs:
        sensor_data_to_webApp = {}
        sensor_data_to_webApp["sensor_name"] =da.sensor_name
        sensor_data_to_webApp["name"] = da.name
        sensor_data_to_webApp["type"] = da.type
        sensor_data_to_webApp["value"] = da.value
        sensor_data_to_webApp["time"] = str(da.time)
        sensor_datas_to_web1.append(sensor_data_to_webApp)
        print(sensor_data_to_webApp)
    sensor_datas_to_web_dict = {"sensors_datas":sensor_datas_to_web1}
    return sensor_datas_to_web_dict