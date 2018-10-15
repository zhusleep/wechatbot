# coding:u8
import itchat
import  requests
import  json

def  tulin_robot(text):
    url="http://www.tuling123.com/openapi/api"
    data={
        "key":"*************************",#人apikey值，需要到网址注册自己获取．
        "info":text,#从微信传输过来的文本内容
        'userid': 'wechat-robot',
        'loc':"武汉"
    }
    r=requests.post(url,data=data).json()
    code=r["code"]
    """100000  文本类
       200000  链接类
       302000  新闻类
       308000  菜谱类
       313000  儿歌类
       314000  诗词类"""
    if  code==  302000:
        return  r["text"],r["list"]
    if code==  100000:
        return  r["text"]
    if   code==200000:
        return r["text"],r["url"]
    if   code==313000:
        return r["text"],r["function"]
    if   code==314000:
        return  r["text"],r["function"]
    if   code==308000:
        return r["text"],r["list"]


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    print(msg)
    if msg['User']['NickName'] == '张三':
        xiaocai = msg['User']['UserName']
        itchat.send(tulin_robot(msg['Text']), toUserName=xiaocai)
    if msg['User']['RemarkName'] == '李四':# 
        xiaocai = msg['User']['UserName']
        itchat.send(tulin_robot(msg['Text']), toUserName=xiaocai)
        return

    return tulin_robot(msg.text)

itchat.auto_login(hotReload=False)
itchat.run()
