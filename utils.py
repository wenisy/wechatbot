# coding=utf8
import itchat

def login_callback():
    myUserName = itchat.search_friends()['UserName']
    itchat.send_msg(u'您好，小嗨机器人已经上线，你可以休息一会儿啦！', myUserName)
