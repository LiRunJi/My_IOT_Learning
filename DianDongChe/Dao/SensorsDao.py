from sqlalchemy.orm import Session
from DianDongChe.models.Sensor import sensors, sensors_data

def add_one_sensor(sensor_name:str,db:Session):
    sensor=sensors()
    sensor.name=sensor_name
    db.add(sensor)
    db.commit()
    db.flush(sensor)
    return sensor.id

###############################################
#                                             #
#      按照传感器名字,数据名字,获得最近一条数据      #
#                                             #
###############################################
def get_all_sensors(db:Session):
    return db.query(sensors).all()
#这个有用
def add_one_data(data: sensors_data, db: Session):
    db.add(data)
    db.commit()


def get_sensor_by_name(name: str, db: Session):
    c = db.query(sensors).filter(sensors.name == name).first()
    return c


#这个比较关键,后边都是按照这个查的
def get_id_by_name(name: str, db: Session):
    try:
        id=get_sensor_by_name(name=name, db=db).id
        return id
    except:
        return None


def get_the_last_one_by_sensorName_and_dataName(sensor_name: str, data_name: str, db: Session):
    one_data = None
    if sensor_name == 'all':
        if data_name == 'all':
            one_data = db.query(sensors_data) \
                .filter(sensors_data.time is not None) \
                .order_by(-sensors_data.time).first()
        else:
            one_data = db.query(sensors_data) \
                .filter(sensors_data.name == data_name, sensors_data.time is not None) \
                .order_by(-sensors_data.time).first()

    else:
        id = get_id_by_name(sensor_name, db)
        if data_name == 'all':
            one_data = db.query(sensors_data) \
                .filter(sensors_data.sensor_id == id, sensors_data.time is not None) \
                .order_by(-sensors_data.time).first()
        else:
            one_data = db.query(sensors_data) \
                .filter(sensors_data.name == data_name, sensors_data.sensor_id == id, sensors_data.time is not None) \
                .order_by(-sensors_data.time).first()
    return one_data


def get_a_serious_of_data_by_sensorName_dataName_startTime_and_endTime(
        sensor_name: str,
        data_name: str,
        start_time,
        end_time,
        db: Session
):
    if sensor_name == "all":
        if data_name == "all":
            datas = db.query(sensors_data).filter(
                sensors_data.time > start_time,
                sensors_data.time < end_time
            ).all()

        else:
            datas = db.query(sensors_data).filter(
                sensors_data.name == data_name,
                sensors_data.time > start_time,
                sensors_data.time < end_time
            ).all()
    else:
        if data_name == "all":
            id = get_id_by_name(sensor_name, db)
            datas = db.query(sensors_data).filter(
                sensors_data.sensor_id == id,
                sensors_data.time >= start_time,
                sensors_data.time <= end_time
            ).all()
        else:
            id = get_id_by_name(sensor_name, db)
            datas = db.query(sensors_data).filter(
                sensors_data.sensor_id == id,
                sensors_data.name == data_name,
                sensors_data.time >= start_time,
                sensors_data.time <= end_time
            ).all()
    return datas


# def get_all_datas(db: Session):
#     return db.query(sensors_data).all()


def sort_data_by_sensor_name_and_type(name: str, type: str, db: Session):
    datas = db.query(sensors_data).filter(sensors_data.name == name, sensors.type == type).all()
    return datas


def sort_data_by_sensor_name_and_dataName(sensor_name: str, dataName: str, db: Session):
    sensor = db.query(sensors).filter(sensors.name == sensor_name).first()
    datas = db.query(sensors_data).filter(sensors_data.id == sensor.id, sensors_data.name == dataName).all()
    return datas


def sort_data_by_sensor_name_and_dataName_and_limit(sensor_name: str, dataName: str, limit: int, db: Session):
    sensor = db.query(sensors).filter(sensors.name == sensor_name).first()

    datas = db.query(sensors_data). \
        filter(sensors_data.sensor_id == sensor.id, sensors_data.name == dataName). \
        order_by(-sensors_data.time). \
        limit(limit)

    return datas


from DianDongChe.schemas import schemas
def query_to_table(qury_args:schemas.table_query,db:Session):
    ids=[]
    data_names=[]
    results=[]
    try:
        for c in qury_args.one_cloumns:
            ids.append(get_id_by_name(c.sensor_name, db))
            data_names.append(c.data_name)
        for i in range(len(ids)):
            results.append(
                db.query(sensors_data). \
                filter(sensors_data.sensor_id == ids[i],
                       sensors_data.name == data_names[i]). \
                order_by(-sensors_data.time). \
                limit(qury_args.limit)
                )
    except:
        return None
    return results