from dao import data_dao
from models_and_schemas import models
from connection_pool.db_connection import get_session
db=get_session()

def add_sensor_data_in_dict_to_db(datas:dict):
    for sensor_data_to_webApp in datas:
        one_da = models.sensors_data()
        one_da.sensor_name = sensor_data_to_webApp["sensor_name"]
        one_da.name = sensor_data_to_webApp["name"]
        one_da.type = sensor_data_to_webApp["type"]
        one_da.value = sensor_data_to_webApp["value"]
        one_da.time = sensor_data_to_webApp["time"]
        one_da.is_sent_out = False
        data_dao.add_one_data(one_da, db)
        print(one_da)
