'''
自动把能发出去的数据发出去,
存出去之后就删掉(节省空间),
先用Navicate 生成只有时间的假数据,然后更新字段
UPDATE sensors_data
set `name`='test',
type='test',
sensor_name='test',
value='test',
is_sent_out=0
WHERE time is not NULL;
这样就得到测试用的假数据了
'''

#断网重连后数据不丢失
def send_unsent_datas_in_db():
    while True:
        import time
        try:
            import requests
            from dao import data_dao
            from handler import Formatter
            import time
            from connection_pool.db_connection import Base, engine, get_session  # 加载数据库需要的驱动
            from handler.NetWorkService import get_connecting_flag
            from configs.read_yaml import conf
            data_url = conf['data_url']
            Base.metadata.create_all(engine)
            db = get_session()
            while True:
                try:
                    if get_connecting_flag()==1:
                        datas = data_dao.get_unsent_data(db=db, limit=10)
                        if datas is not None and datas!=[]:
                            print(datas)
                            j = Formatter.change_data_objs_to_json(datas)
                            if j=='''{"sensors_datas": []}''':
                                time.sleep(1)
                                continue
                            print(data_url)
                            r=requests.post(url=data_url, json=j)
                            print(r.status_code)
                            print(r.text)
                            if r.status_code==200:
                                print("清除中心节点缓存的数据...")
                                data_dao.delete_the_given_datas(datas, db)

                except Exception as e:
                    print(e)
                    print("数据库里存的没发出去")
                    pass
                time.sleep(1.5)
        except Exception as e:
            print(e)
            time.sleep(2)
        print("初始化出问题")


# import threading
# threading.Thread(target=send_unsent_datas_in_db).start()