import datetime

from sqlalchemy.orm import Session
from DianDongChe.models.Sensor import sensors, sensors_data
from DianDongChe.models.people import people,people_working,how_many_people



def add_one_people(a_people:people,db:Session):
    db.add(a_people)
    db.commit()

def query_if_exits(card_num,db:Session):
    p=db.query(people).\
        filter(people.card_num==card_num).\
        order_by(people.id).first()
    return p

def get_all_people(db:Session):
    return db.query(people).all()

def get_people_working_by_people_id(id,db:Session):
    return db.query(people_working).\
        filter(people_working.people_id==id).\
        order_by(-people_working.id).limit(1).first()


def change_many(t:int,db:Session):
    (db.query(how_many_people).first().total_people)=t
    db.commit()


def get_many(db:Session):
    return db.query(how_many_people).first().total_people

def add_working_message(p:people_working,db:Session):
    db.add(p)
    db.commit()



def get_details_in_kj(db:Session):
    peoples=db.query(people_working).\
        filter(people_working.end_time==None)
    return peoples

def get_details_in_kj_by_kjName(kjName:str,db:Session):
    return \
        db.execute(f'''SELECT 
people.people_name,
people.card_num,
people_working.start_time,
time_to_sec(timediff(NOW(),people_working.start_time)) as total_time
FROM people,people_working
WHERE people.id=people_working.people_id
and people_working.end_time is NULL
and people.company_name='{kjName}';
''').all()
    # return peoples
def get_name_by_id(id,db:Session):
    return db.query(people).filter(people.id==id).first().people_name

def get_card_by_id(id,db:Session):
    return db.query(people).filter(people.id==id).first().card_num