'''
这里是数据库连接的创建与配置模块,
本模块提供对数据库操作的初始化,
提供BASE
'''

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from config_files.load_total_project_configs import conf
db_type=conf['db_type']
db_driver=conf['db_driver']
db_url=conf['db_url']
# db_url='192.168.217.103:3306'
db_userName=conf['db_userName']
db_password=conf['db_password']
# db_password='123456'
db_name=conf['db_name']

url=db_type+'+'+db_driver+'://'+db_userName+":"+str(db_password)+"@"+db_url+'/'+db_name
print(url)
#1. 声明引擎
engine = create_engine(url=url,encoding='utf-8',echo=True)
#2. 声明本地会话
'''
       bind
engine=====> SessionLocal
'''
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#3. 声明Base
Base = declarative_base()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_session():
    session=Session(engine)
    return session

