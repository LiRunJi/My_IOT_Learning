'''
因为MQTT是长连接,这里把MQTT的内容转发到主题
减少前端的工作量
'''


from fastapi import APIRouter,Depends,HTTPException,status
from DianDongChe.schemas import schemas
from DianDongChe.mqtt.Transmit.Send import send_message_to_topic

router = APIRouter(
    prefix='/DianChe_control',
    tags=['控制']
)

'''
2022-09-20 以下两个接口试了几次,能用. 
'''

@router.post('/control',status_code=status.HTTP_200_OK)
def send_control_message_to_hardware(request:schemas.control_package):
    '''
    发送控制,具体格式详见--Request body部分
    auto_control=0,alarm字段用于报警
    '''
    # print(request)
    while True:
        if send_message_to_topic(topic="/control_topic",message=request.json()) !='发送成功':
            continue
        else:
            break
    return "发送成功"



@router.post('/thresholds', status_code=status.HTTP_200_OK)
def set_thresholds(request: schemas.control_threshoud):
    '''
    设置阈值
{
"auto_control":1,

"thresholds:[

        {

        "name":"t1",

        "target":"dht11",

        "value": 26.0

        },

        {
        "name":"t2",

        "target":"dht11",

        "value": 60.0

        },

        {
        "name":"l1",

        "target":"led1",

        "value": 60.0

        }


    ]



}
    消息由后端通过mqtt协议转发给硬件\r\n
    '''
    while True:
        if send_message_to_topic(topic="/control_topic", message=request.json()) != '发送成功':
            continue
        else:
            break
    return "发送成功"