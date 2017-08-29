# coding=utf8
import time, random
import itchat
import utils


def buy_flowers():
    return 'buy flowers'


def about_us():
    return 'about us'


# 这里是我们在“1. 实现微信消息的获取”中已经用到过的同样的注册方法
@itchat.msg_register(itchat.content.TEXT)
def receive_message(msg):
    print msg.fromUserName
    # 微信名
    print msg.User.NickName
    # 备注名
    print msg.User.RemarkName
    # 微信账号的前三个字幕
    print msg.User.KeyWord
    print "I'm in"
    this_time = random.randint(2, 6)
    print this_time
    time.sleep(this_time)
    switcher = {
        1: buy_flowers,
        2: about_us()
    }
    switcher.get(msg['Text'])
    # 根据用户名或者备注名搜索到这个好友。
    # 这个name为 nickname || remarkname， 结果为数组
    users = itchat.search_friends(name=u'测试')
    # 根据备注名搜索用户
    # testUsers1 = itchat.search_friends(remarkName=u'熊彬')
    # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
    default_reply = 'I received: ' + msg['Text']
    return default_reply


itchat.login(loginCallback=utils.login_callback)
itchat.run()
