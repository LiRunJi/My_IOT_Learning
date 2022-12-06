from drivers.db_connection import Base
from sqlalchemy import Column, Integer,VARCHAR, ForeignKey,DATETIME
from sqlalchemy.orm import relationship


class people(Base):
    __tablename__ = "people"
    id=Column(Integer,primary_key=True)

    people_name = Column(VARCHAR(20))
    card_num= Column(VARCHAR(20))
    company_name=Column(VARCHAR(20))

class people_working(Base):
    __tablename__ = "people_working"
    id=Column(Integer,primary_key=True)
    people_id = Column(Integer,ForeignKey("people.id"))
    start_time=Column(DATETIME)
    end_time = Column(DATETIME)
    total_time=Column(Integer)

class how_many_people(Base):
    __tablename__ = "how_many_people"
    id = Column(Integer, primary_key=True)
    company_name = Column(VARCHAR(20))
    total_people=Column(Integer)