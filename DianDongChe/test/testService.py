import requests
da={
  "sensors_datas": [
    {
      "sensor_name": "test",
      "name": "string",
      "type": "string",
      "value": "string",
      "time": "2022-10-7 21:02:1"
    },
    {
      "sensor_name": "test",
      "name": "string",
      "type": "string",
      "value": "string",
      "time": "2022-10-7 21:02:2"
    },
  {
      "sensor_name": "test",
      "name": "string",
      "type": "string",
      "value": "string",
      "time": "2022-10-7 21:02:1"
    }
  ]
}
r=requests.post(url='http://42.192.227.238/DianDongChe_add/one_data'
                ,json=da)

print(r)
print(r.text)
print(type(r.text))