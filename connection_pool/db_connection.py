'''
这里是数据库连接的创建与配置模块,
本模块提供对数据库操作的初始化,

'''

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

db_type='mysql'
db_driver='pymysql'
db_url='127.0.0.1:3306'
db_userName='root'
db_password='123456'
db_name='test'
url=db_type+'+'+db_driver+'://'+db_userName+":"+db_password+"@"+db_url+'/'+db_name

print("数据库网址: ")
print(url)

engine = create_engine(url, echo=False, future=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_session():
    session=Session(engine)
    return session

