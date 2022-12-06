import datetime
from typing import List
from pydantic import BaseModel

class sensors:
    id: int
    name: str
    type: str
    location: str
    smart_node_id: int
    data_names: List[str]
    data_types: List[str]

#
class sensors_datas(BaseModel):
    class sensors_data(BaseModel):
        sensor_name: str
        name: str
        type: str
        value: str
        time: str
        class Config():
            orm_mode = True
    sensors_datas:List[sensors_data]

    class Config():
        orm_mode = True

class control_threshoud(BaseModel):
    class threshoud(BaseModel):
        name:str
        target:str
        value:float
        class Config():
            orm_mode=True
    id:int
    auto_control:int
    thresholds:List[threshoud]
    class Config():
        orm_mode=True


class control_package(BaseModel):
    class control_instruction(BaseModel):
        target_name:str
        instruction:int
        class Config():
            orm_mode=True
    id:int
    auto_control:int
    alarm:int
    control_instructions:List[control_instruction]
    class Config():
        orm_mode=True


class table_query(BaseModel):
    class one_cloumn(BaseModel):
        sensor_name:str
        data_name:str
        class Config():
            orm_mode = True

    limit: int
    one_cloumns:List[one_cloumn]
    class Config():
        orm_mode = True

# =============================================================

class people_data(BaseModel):
    people_name:str
    card_num:str
    company_name:str
    class Config():
        orm_mode=True
class peoples(BaseModel):
    peoples:List[people_data]
    class Config():
        orm_mode=True

class how_many_people(BaseModel):
    id : int
    company_name : str
    total_people : int


