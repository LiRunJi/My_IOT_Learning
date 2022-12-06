from drivers.db_connection import Base
from sqlalchemy import Column, Integer,VARCHAR, ForeignKey,DATETIME
from sqlalchemy.orm import relationship



class sensors(Base  ):
    __tablename__ = "sensors"
    id = Column(Integer,primary_key=True)  # INTEGER NOT NULL,
    name           = Column(VARCHAR(20))  # VARCHAR(20) NOT NULL,
    type           =Column(VARCHAR(20))
    location       = Column(VARCHAR(40))  # VARCHAR(40) NOT NULL,
    smart_node_id  = Column(Integer,ForeignKey("smart_nodes.id"))
    data_names     = Column(VARCHAR(200))
    data_types     = Column(VARCHAR(200))





class sensors_data(Base):
    __tablename__ = "sensors_data"
    id=Column(Integer,primary_key=True)
    sensor_id = Column(Integer,ForeignKey("sensors.id"))
    name = Column(VARCHAR(20))
    type = Column(VARCHAR(20))
    value = Column(VARCHAR(20))
    time = Column(DATETIME)
    def __repr__(self):
        return f"sensors_data(id={self.id!r},name={self.name!r},type={self.type!r}," \
               f"value={self.value!r})"
