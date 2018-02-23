#-*- coding: utf-8 -*-

import requests
import itchat  # 这是一个用于微信回复的库

KEY = '9e8a645bff274cd78801e30676101386'  # 这个key可以直接拿来用# 向api发送请求


def get_response(msg):
    Url = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': KEY,
        'info': msg,
        'userid': 'pth-robot',
    }

    try:
        print 2222
        r = requests.post(Url, data=data).json()
        print r
        return r.get('text')
    except:
        print 3333
        return  # 注册方法@itchat.msg_register(itchat.content.TEXT)


def tuling_reply(msg):
    # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
    print 1111
    defaultReply = 'I received: ' + msg['Text']  # 如果图灵Key出现问题，那么reply将会是None
    reply = get_response(msg['Text'])  # a or b的意思是，如果a有内容，那么返回a，否则返回b
    print reply
    return reply or defaultReply  # 为了让修改程序不用多次扫码,使用热启动


# itchat.auto_login(hotReload=True)
# itchat.run()

print('你好，我是一枚萌萌哒的机器人！')
while 1:
    s = raw_input()
    msg = {}
    msg['Text'] = s
    msgs = tuling_reply(msg)
    print msgs