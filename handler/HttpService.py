'''
解析json,
按照json发http
返回r.text
'''
from handler import DaoServices
import requests
import datetime

def add_time(msg:dict):
    for data in msg['sensors_datas']:
        data["time"] = str(datetime.datetime.now())
    return msg

def send_http(msg:dict):
    method=msg['method']
    data=msg['data']
    url=msg['url']
    mode=msg['mode']
    save=msg['save']
    try:
        if mode=="json":
            data=add_time(data)
            r=requests.request(method=method,url=url,json=data)
            print(r)
            t=r.text.replace("\"", "")

            if save==1:
                if t!="ok":
                    DaoServices.add_sensor_data_in_dict_to_db(data['sensors_datas'])
        elif mode=="param":
            r=requests.request(method=method,url=url,params=data)
            t=r.text.replace("\"", "")

        print(t)
        return t
    except Exception as e:
        print(e)
        print(f"http请求失败")
        r='e'
        if mode=="json" and save==1:
            print("数据层1")
            DaoServices.add_sensor_data_in_dict_to_db(data['sensors_datas'])
            print("数据层出问题")

    return str(r)

