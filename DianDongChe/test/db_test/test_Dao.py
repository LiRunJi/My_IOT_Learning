from DianDongChe.Dao import SensorsDao
from drivers.db_connection import get_session
db=get_session()
print(SensorsDao.get_all_sensors(db))
db.close()