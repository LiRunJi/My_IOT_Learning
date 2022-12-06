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
from DianDongChe.Dao import PeopleDao
from DianDongChe.models.people import people,people_working
router = APIRouter(
    prefix="/DianDongChe_people",
    tags=['入']
)

def time_many_start_end(card_num:str):

    pass
@router.post('/add_one_people')
async def add_one_people(request:schemas.people_data,db:Session=Depends(get_db)):
    '''
    增加一个人,要给人的卡号,姓名,还有公司名(矿井名)
    '''
    p=people(card_num=request.card_num,
             people_name=request.people_name,
             company_name=request.company_name)
    PeopleDao.add_one_people(p,db=db)
    return "ok"

@router.post('/exits')
async def return_1_if_exits(request:str,db:Session=Depends(get_db)):
    '''根据卡号查这个人是不是存在,同时记录进入矿井的数据'''
    p=PeopleDao.query_if_exits(card_num=request,db=db)
    if p is None:
        return 0

    pw=PeopleDao.get_people_working_by_people_id(p.id,db)
    if pw is None:
        PeopleDao.add_working_message(people_working(people_id=p.id),db)
        pw = PeopleDao.get_people_working_by_people_id(p.id, db)
    if pw.start_time is None :
      pw.start_time=datetime.datetime.now()
      db.commit()
    elif pw.end_time is None:
        pw.end_time=datetime.datetime.now()
        pw.total_time=(datetime.datetime.now()-pw.start_time).seconds
        db.commit()

    elif pw.end_time is not None and pw.start_time is not None:
        pp=people_working(people_id=pw.people_id,start_time=datetime.datetime.now())
        PeopleDao.add_working_message(pp,db)

    return 1



@router.get('/all_people')#,response_model=schemas.peoples)
async def get_all_people(db:Session=Depends(get_db)):
    '''查所有人'''
    return PeopleDao.get_all_people(db)

@router.post('/change_people_many')
async def change_working_num(request:int,db:Session=Depends(get_db)):
    '''改变矿井里有多少人'''
    PeopleDao.change_many(request,db)
    return "ok"

@router.get('/get_how_many')
async def get_many(db:Session=Depends(get_db)):
    '''查询有多少人在'''
    return PeopleDao.get_many(db)

# @router.get('/get_how_many_by_kj')
# async def get_many(kj:str,db:Session=Depends(get_db)):
#     '''查询有多少人在'''
#     return db.execute('''
#     select count(*) from
#     ''').all()
@router.get('/shishi')
async def shishi(db:Session=Depends(get_db)):
    '''查询有多少## 实时计时给一个接口,查接口**返回人的姓名,卡号,以及累计时间**'''
    r=[]
    ps=PeopleDao.get_details_in_kj(db)
    for p in ps:
        print(p)
        d = {"name": "", "card": "", "start_time": "", "total_time": ""}
        d["name"]=PeopleDao.get_name_by_id(p.people_id,db)
        d["card"]=PeopleDao.get_card_by_id(p.people_id,db)
        d["start_time"]=str(p.start_time)
        d["total_time"]=(datetime.datetime.now()-p.start_time).seconds
        r.append(d)


    return r

@router.get('/duokuangjingshishi')
async def shishi(kjName:str,db:Session=Depends(get_db)):
    '''查询有多少## 实时计时给一个接口,查接口**返回人的姓名,卡号,以及累计时间**'''
    return PeopleDao.get_details_in_kj_by_kjName(kjName,db)
