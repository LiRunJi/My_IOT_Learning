import datetime
import time
import json
from sqlalchemy.orm import Session

from fastapi import Depends
from drivers.db_connection import get_db, Base, engine, get_session
from FarmModule.models.CentralNode import central_nodes
from FarmModule.models.Logs import logs
from FarmModule.models.User import users
from FarmModule.models.SmartNode import smart_nodes
from FarmModule.models.Sensor import sensors, sensors_data

from FarmModule.FarmDao import CentralNodesDao,SmartNodesDao,SensorsDao

db = get_session()


def create(centeral: central_nodes, db: Session):  # Depends(get_db)):

    db.add(centeral)
    db.commit()
    db.refresh(centeral)
    return centeral


# user=users(name="李四")
# db.add(user)
# db.commit()
# zhansan=db.query(users).filter(users.name=='李四').first()
# print(zhansan.name)
#
# c=central_nodes(name="fire3",location="csxy",user_id=zhansan.id)
#
#
#
#
Base.metadata.create_all(engine)
#
# CentralNodesDao.add_one_central_node(c,db)
# zhansan=db.query(users).filter(users.name=='李四').first()

CentralNodesDao.delete_central_node_by_name("fire3", db)
nodes = CentralNodesDao.get_central_nodes_by_username("李四", db)
# print(nodes.id)
for node in nodes:
    print(node.name, node.id)
    # print( create(c,get_session()))


n1 = CentralNodesDao.get_central_node_by_id(18, db)
#time.sleep(1)
print('----------')

print(n1.name)
print(n1)
print(n1.__dict__)


receive_json={
"central_nodes":[
    {"name": "fire2","location": "csxy", "user_id": 6, "logs_id": 11},
    {"name": "fire2","location": "csxy", "user_id": 6, "logs_id": 11}
    ],
"smart_nodes":[
     {"name": "N1","location": "csxy_zhiYuanLou", "central_node_name":"fire3"},
     {"name": "N2","location": "csxy_zhiHanxuLou", "central_node_name":"fire3"},
     {"name": "N3","location": "csxy_zhiMingZhiLou", "central_node_name":"fire3"}
 ],
"sensors":[
{"name ":"dht1" ,"type":"reader",
"location":"zhiyuanlou",
"smart_node_name":"N1",
"data_names":["temperature","humidity"],
"data_types":["float","float"]
},
{"name ":"dht2" ,"type":"reader",
"location":"zhiyuanlou",
"smart_node_name":"N1",
"data_names":["temperature","humidity"],
"data_types":["float","float"]
},
{"name ":"dht3" ,"type":"reader",
"location":"zhiyuanlou",
"smart_node_name":"N1",
"data_names":["temperature","humidity"],
"data_types":["float","float"]
}
]
}
send_json={
    central_nodes:[
     {"central_node_name" : "fire1", "id": 1},
     {"central_node_name" : "fire2", "id": 2},
     {"central_node_name" : "fire2", "id": 2}
    ],
    smart_nodes:[
     {"smart_node_name" : "N1", "id": 1},
     {"smart_node_name" : "N2", "id": 2},
     {"smart_node_name" : "N3", "id": 2}
    ],
    sensors:[
     {"sensor_name" : "dht1", "id": 1},
     {"sensor_name" : "dht2", "id": 2},
     {"sensor_name" : "dht3", "id": 2}
    ]
}
#/////////-------------以下内容发到中心节点的主题上--------------\\\\\\\\\\\\\\\
#这个里边对应传感器数据表里边的时间要自己加上
mqtt_data_package1={
    "snesor_data":{
    "sensor_id":1,
    "name":"temperature",
    "type":"float",
    "value":"25.0"
    }
}
mqtt_data_package2={
    "snesor_data":{
    "sensor_id":1,
    "name":"humidity",
    "type":"float",
    "value":"55.0"
    }
}
#......

mqtt_control_package={
    "target_type":"smart_node",
    "target_name":"",
    "target_instruction":"open"
}

#b=json.dump(n1)
smart_node1=smart_nodes(name="N1",central_node_id=18)
smart_node2=smart_nodes(name="N2",central_node_id=18)
smart_node3=smart_nodes(name="N3",central_node_id=18)

dht1=sensors(name="dht1",
             type="reader",
             smart_node_id=7,
             data_names="temperature,humidity",
             location='csxy',
             data_types="float,float")
dht2=sensors(name="dht2",
             location='csxy',
             type="reader",
             smart_node_id=7,
             data_names="temperature,humidity",
             data_types="float,float")
dht3=sensors(name="dht3",
             location='csxy',
             type="reader",
             smart_node_id=7,
             data_names="temperature,humidity",
             data_types="float,float")
light1=sensors(name="light1",
             location='csxy_教学楼',
             type="reader",
             smart_node_id=8,
             data_names="light",
             data_types="int")
light2=sensors(name="light2",
             location='csxy',
             type="reader",
             smart_node_id=8,
             data_names="light",
             data_types="int")
light3=sensors(name="light3",
             location='csxy_食堂',
             type="reader",
             smart_node_id=8,
             data_names="light_宿舍",
             data_types="int")

'''
----->name 
----> cun --->id
--->id
'''

# db.commit()
# SmartNodesDao.delete_smart_node_by_name("N1",db)
# SmartNodesDao.delete_smart_node_by_name("N2",db)
# SmartNodesDao.delete_smart_node_by_name("N3",db)

# SmartNodesDao.add_one_smart_node(smart_node1,db)
# SmartNodesDao.add_one_smart_node(smart_node2,db)
# SmartNodesDao.add_one_smart_node(smart_node3,db)

# SensorsDao.add_one_sensor(dht1,db)
# SensorsDao.add_one_sensor(dht2,db)
# SensorsDao.add_one_sensor(dht3,db)
# SensorsDao.add_one_sensor(light1,db)
# SensorsDao.add_one_sensor(light2,db)
# SensorsDao.add_one_sensor(light3,db)

# SensorsDao.add_one_data(,db=db)

#清一下缓存
# db.execute("delete  from smart_nodes where logs_id is null ;")
# db.execute("delete  from central_nodes where logs_id is null ;")
# db.commit()

data1=sensors_data(sensor_id=1,name="temperature",type="float",value="25",time=datetime.datetime.now())
data2=sensors_data(sensor_id=1,name="temperature",type="float",value="26",time=datetime.datetime.now())
data3=sensors_data(sensor_id=1,name="temperature",type="float",value="27",time=datetime.datetime.now())
data4=sensors_data(sensor_id=7,name="light",type="int",value="125",time="2022-06-29 01:19:45")
data5=sensors_data(sensor_id=7,name="light",type="int",value="125",time="2022-06-29 01:19:45")
data6=sensors_data(sensor_id=7,name="light",type="int",value="125",time="2022-06-27 21:09:45")
data7=sensors_data(sensor_id=7,name="light",type="int",value="125",time="2022-06-27 21:09:45")
data8=sensors_data(sensor_id=7,name="light",type="int",value="125",time="2022-06-28 21:19:45")
data9=sensors_data(sensor_id=7,name="light",type="int",value="125",time="2022-06-28 21:19:45")

# SensorsDao.add_one_data(data1,db)
# SensorsDao.add_one_data(data2,db)
# SensorsDao.add_one_data(data3,db)
# SensorsDao.add_one_data(data4,db)
# SensorsDao.add_one_data(data5,db)
# SensorsDao.add_one_data(data6,db)
# SensorsDao.add_one_data(data7,db)
# SensorsDao.add_one_data(data8,db)
c=db.query(central_nodes).filter(central_nodes.id == 18).first()
s=db.query(smart_nodes).filter(smart_nodes.id==8).first()

a=SensorsDao.get_the_last_one_by_sensorName_and_dataName(sensor_name="dht1",data_name="temperature",db=db)
print("-----")
print(a)

for x in c.smart_nodes:
    print(x.name)
for x in s.sensors:
    print(x.name)

