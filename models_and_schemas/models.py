from connection_pool.db_connection import Base
from sqlalchemy import Column, Integer,VARCHAR, DATETIME

import datetime

class sensors_data(Base):
    __tablename__ = "sensors_data"
    id=Column(Integer,primary_key=True)
    sensor_name = Column(VARCHAR(20))
    name = Column(VARCHAR(20))
    type = Column(VARCHAR(20))
    value = Column(VARCHAR(20))
    time = Column(DATETIME,default=datetime.datetime.now())
    is_sent_out=Column(Integer,default=0)
    def __repr__(self):
        return f"sensors_data(id={self.id!r},name={self.name!r},type={self.type!r}," \
               f"value={self.value!r})"
