'''
这个Service是用来查数据的,
查各种数据,组装成本表
'''
import datetime
from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from drivers.db_connection import get_db
from typing import List
from DianDongChe.schemas import schemas
#====以上是官方库,下边的是自己写的=======
from DianDongChe.Dao import SensorsDao

router = APIRouter(
    prefix="/DianDongChe_query",
    tags=['拿到数据']
)

@router.get('/all_sensors')
def get_all_sensors(db: Session=Depends(get_db)):
    return SensorsDao.get_all_sensors(db)

@router.get('/one_sensor_last_data')#,response_model=List[schemas.ShowBlog])
def get_the_last_data_by_sensor_name_or_id(
        sensor_name:str="dht1",
        data_name:str="temperature",
        # id:int=None,
        db: Session=Depends(get_db)):
    '''
    给出传感器名称返回最近的一条给出的数据,\r\n
    为了测试考虑,默认提供数据库最靠前的传感器的数据\r\n
    name: 传感器名称\r\n
    id: 传感器名称\r\n
    return: 返回一个json包,格式如下:\r\n
    {\r\n
        "sensor_id": 1,\r\n
        "name": "temperature",\r\n
        "type": "float",\r\n
        "value": "25.0",\r\n
        "time": "2022-06-28 21:19:45"\r\n
    }\r\n
    '''
    one_data=SensorsDao.\
            get_the_last_one_by_sensorName_and_dataName(sensor_name=sensor_name,
                                                        data_name=data_name,
                                                        db=db)


    if one_data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="没得这个")

    return one_data


@router.get('/one_sensor_lots_of_data')
async def get_a_lots_of_data(
        sensor_name: str= "dht2",
        data_name:str= "temperature" ,
        limit: int = 7,
        db: Session = Depends(get_db)
):

    '''
    输入传感器的名字和传感器的数据名称,以及要查几条,
    返回最新的这几条数据.
    [{"value": "25","time": "2022-06-28T21:19:46"},{"value": "25.0","time": "2022-06-28T21:19:48"}]
    '''
    a=SensorsDao.sort_data_by_sensor_name_and_dataName_and_limit(sensor_name,data_name,limit,db)
    j={"time":"","value":""}
    xx=[]
    for x in a:
        k = {"time": "", "value": ""}
        k["value"]=x.value
        k["time"]=str(x.time)
        xx.append(k)
    return xx

#获得指定传感器,指定数据名称,限制时间内的数据,有默认值
@router.get('/select_between_time')#,response_model=List[schemas.ShowBlog])
def get_a_serious_of_data_by_sensorName_dataName_startTime_and_endTime(
        sensor_name:str= "dht1",
        data_name:str= "temperature",
        start_time:datetime.datetime= "2022-06-28T21:19:46",
        end_time:datetime.datetime= datetime.datetime.now(),
        db: Session=Depends(get_db)
):
    '''
    按照传感器名称,数据名称,开始时间,结束时间来获得数据        \r\n
    可不给开始时间,默认开始时间为 2022-06-28T21:19:46      \r\n
    也可不给结束时间,默认结束时间是现在的时间\r\n
    sensor_name: 传感器名称,字符串类型,如需所有传感器传入参数"all"即可\r\n
    data_name: 数据名称,字符串类型,如需所有数据,传入参数"all"即可\r\n
    start_time: 开始时间,类型需要是DATATIME型, 例如:2022-06-28 21:19:46,可不给开始时间,默认开始时间为 2022-06-28T21:19:46\r\n
    end_time:  结束时间,也可不给结束时间,默认结束时间是现在的时间\r\n
    return: 返回一串数据,格式类似下面的例子:\r\n
    tip: 值默认都是字符串,但提供数据类型,可根据"type"把字符串转化为其它类型 \r\n
    [
    {
    "sensor_id": 1,
    "name": "temperature",
    "value": "25",
    "type": "float",
    "id": 4,
    "time": "2022-06-28T21:19:46"
    },

    {
    "sensor_id": 1,
    "name": "temperature",
    "value": "25.0",
    "type": "float",
    "id": 69,
    "time": "2022-06-28T21:19:48"
    }
    ]
    '''
    datas=SensorsDao.\
        get_a_serious_of_data_by_sensorName_dataName_startTime_and_endTime(sensor_name,data_name,start_time,end_time,db)

    return datas

#获得人员数据,目前是假数据,后续打算建一个RFID表
@router.get('/people_data')
async def get_a_lots_of_data(
        # sensor_name: str="dht2",
        db: Session = Depends(get_db),
        # limit:int=1000
):
    ren='''{
"p_datas":[
{
"people_message":"p1",
"ic_message":"dasdasdsa"
},
{
"people_message":"p2",
"ic_message":"wqewqeqweqw"
}
]
}'''
    ren=ren.strip()
    ren=eval(ren)
    return ren


#获得人员数据,目前是假数据,后续打算建一个RFID表
@router.post('/table_data')
async def get_a_lots_of_data(
        request:schemas.table_query,
        db: Session = Depends(get_db),

):
    '''
    输入这样一个json包,limit限制一共查多少,
    one_cloumns中每一个为要查的传感器的数据种类名,
    按照查询顺序返回数据
    如果哪个属性找不到,就返回空值,
    以下是一个示例:
    \r\n
    param->request:

{
 "limit":3,
"one_cloumns":[
 {"sensor_name":"dht1","data_name":"temperature"},
{"sensor_name":"light1","data_name":"light"}
 ]
}
\r\n
    return:
[
  [
    {
      "time": "2022-09-20 15:52:33",
      "value": "26"
    },
    {
      "time": "2022-09-20 15:52:33",
      "value": "26"
    },
    {
      "time": "2022-09-20 15:52:33",
      "value": "26"
    }
  ],
  [
    {
      "time": "2022-09-14 21:20:36",
      "value": "190"
    },
    {
      "time": "2022-09-14 21:20:34",
      "value": "192"
    },
    {
      "time": "2022-09-14 21:20:32",
      "value": "192"
    }
  ]
]
    '''
    returns = []
    result=SensorsDao.query_to_table(request,db)
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="传感器或传感器的属性不在数据库内")
    else:
        for r in result:
            xx = []
            for x in r:
                k = {"time": "", "value": ""}
                k["value"] = x.value
                k["time"] = str(x.time)
                xx.append(k)
            returns.append(xx[::-1])
    return returns

