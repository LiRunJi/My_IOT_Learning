from drivers.mqtt_connection import get_client,connect
import threading

#初始化的时候建立一个mqtt连接,手动创建一个非阻塞的线程保证通信流畅
sender=get_client("py_web_sender")
sender=connect(sender)
threading.Thread(target=sender.loop_forever).start()

#控制指令的话是在接收前端消息调用的接口,所以参数多一些,好传参
def send_message_to_topic(topic:str,message,qos=0,retain=False):
    '''
    默认qos为0,retain=False,可修改
    '''
    info=sender.publish(topic=topic,payload=message,qos=qos,retain=retain)
    print(info)
    if info is not None:
        if info[0]==0:
            return "发送成功"
    return "发送失败"

def test():
    import time
    i:int=0
    while True:
        send_message_to_topic("/testTopic",f"test{i}")
        time.sleep(2)

# if __name__ == '__main__':
#     test()