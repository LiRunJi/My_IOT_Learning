'''
解析json,
按照json发http
返回r.text
'''
from handler import DaoServices
import requests
import datetime
from tkGUI.tkGui import refreshText,make_show
from tkGUI.tkGui import entry3


def add_time(msg: dict):
    for data in msg['sensors_datas']:
        data["time"] = str(datetime.datetime.now())
    return msg


def send_http(msg: dict):
    data = msg['data']
    mode = msg['mode']
    try:
        if mode == "json":
            data = add_time(data)
            for sd in data["sensors_datas"]:
                if sd["name"] == "temperature":
                    tem = sd["value"]
                elif sd["name"] == "smoke":
                    smoke = sd["value"]
                elif sd["name"] == "humidity":
                    hum = sd["value"]
            refreshText(entry3, make_show(tem, smoke, hum))

    except Exception as e:
        print(e)
        print(f"出了点小bug")


