'''
增加数据的业务,
这个业务是本地的mqtt路由在调用
'''
import datetime
from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from drivers.db_connection import get_db
from typing import List
from DianDongChe.schemas import schemas
#====以上是官方库,下边的是自己写的=======
from DianDongChe.Dao import SensorsDao
from DianDongChe.models.Sensor import sensors_data as model_sensor_data
from datetime import datetime
router = APIRouter(
    prefix="/DianDongChe_add",
    tags=['拆入数据']
)

'''
#查一次id,然后加到表里
def add_lots_of_data_by_name(datas_json):
    for data_json in datas_json:
        print(data_json)
        print('------------')
        if data_json["time"] is None or data_json["time"]=="":
            data_json['time'] = str(datetime.datetime.now())
        id=SensorsDao.get_id_by_name(data_json["sensor_name"],db)
        if id is None:
            continue
        one_data = Sensor.sensors_data(sensor_id=id, 
        name=data_json["name"],
         type=data_json["type"],
        value=data_json["value"],
         time=data_json["time"])
        SensorsDao.add_one_data(one_data, db)
'''
@router.post('/one_data')
async def add_one_sensor_data(request:schemas.sensors_datas,db:Session = Depends(get_db)):
    for sensor_data in request.sensors_datas:
        sensor_id = SensorsDao.get_id_by_name(sensor_data.sensor_name, db)
        if sensor_id is None:
            sensor_id=SensorsDao.add_one_sensor(sensor_name=sensor_data.sensor_name,db=db)
        if sensor_data.time is None or sensor_data.time=='' or sensor_data.time=="string":
            sensor_data.time=datetime.now().__str__().split('.')[0]

        SensorsDao.add_one_data(
                                model_sensor_data(
                                sensor_id=sensor_id,
                                name=sensor_data.name,
                                type=sensor_data.type,
                                value=sensor_data.value,
                                time=sensor_data.time
                                ),
                                db=db)

    return "ok"


