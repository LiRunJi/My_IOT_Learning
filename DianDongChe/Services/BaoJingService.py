'''
增加数据的业务,
这个业务是本地的mqtt路由在调用
'''

from fastapi import APIRouter
import datetime
router = APIRouter(
    prefix="/DianDongChe_BaoJing",
    tags=['报警time set']
)



start:None
end:None

@router.post('/set_period')
async def set_period(start_in:type(datetime.datetime.now()),
                     end_in:type(datetime.datetime.now())):
    '''

    '''
    global start,end
    start=start_in
    end=end_in
    return "ok"
@router.get('/get_period')
async def return_1_if_exits():
    ''''''
    global start,end
    return str((start,end))

# @router.get('/get_period')
# async def return_1_if_exits():
#     ''''''
#     global start,end
#     return str((start,end))
