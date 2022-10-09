
from sqlalchemy.orm import Session
from models_and_schemas.models import sensors_data
'''
2022-09-11 13:55:59,690 INFO sqlalchemy.engine.Engine 
SELECT
 sensors_data.id AS sensors_data_id, sensors_data.sensor_name AS 
 sensors_data_sensor_name, sensors_data.name AS sensors_data_name, 
 sensors_data.type AS sensors_data_type, sensors_data.value AS
  sensors_data_value, sensors_data.time AS sensors_data_time, 
  sensors_data.is_sent_out AS sensors_data_is_sent_out 
FROM sensors_data 
WHERE sensors_data.is_sent_out = %(is_sent_out_1)s 
 LIMIT %(param_1)s
2022-09-11 13:55:59,691 INFO sqlalchemy.engine.Engine [cached since 18.34s ago] {'is_sent_out_1': 0, 'param_1': 10}
'''



def add_one_data(data:sensors_data,db:Session):
    db.add(data)
    db.commit()

###############################################
#                                             #
#      按照传感器名字,数据名字,获得最近一条数据      #
#                                             #
###############################################

def get_all_datas(db:Session):
    return db.query(sensors_data).all()

def delete_one_data(data:sensors_data,db:Session):
    db.delete(data)
    db.commit()
def delete_the_given_datas(datas,db:Session):
    for da in datas:
        db.delete(da)
    db.commit()

def get_unsent_data(db:Session,limit:int):
    return db.query(sensors_data).filter(sensors_data.is_sent_out==0).limit(limit).all()

def clean_the_sent_data(db:Session):
    datas=db.query(sensors_data).filter(sensors_data.is_sent_out==0).all()
    for da in datas:
        db.delete(da)
    db.commit()