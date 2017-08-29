# coding=utf8
import time, random, itchat, utils, swicher


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
    swicher.receive_message(msg)
    # 找到指定用户并发消息
    send_message_to_specific_user()
    # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
    default_reply = 'I received: ' + msg['Text']
    return default_reply


def send_message_to_specific_user():
    # 根据用户名或者备注名搜索到这个好友。这个name为 nickname || remarkname， 结果为数组
    users = itchat.search_friends(name=u'测试')
    # 找到UserName
    userName = users[0]['UserName']
    # 然后给他发消息
    itchat.send('hello', toUserName=userName)
    # 根据备注名搜索用户
    # testUsers1 = itchat.search_friends(remarkName=u'张三')


itchat.login(loginCallback=utils.login_callback)
itchat.run()
