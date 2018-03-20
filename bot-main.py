# -*- encoding:utf-8 -*-
# created by SkyJohn

import time
import itchat
from itchat.content import *
from get_room_ids import *

# FromUserNames in the group chat

@itchat.msg_register(TEXT, isGroupChat=True)
def group_text_reply(msg):
	if(msg.User.NickName==u"鸡友群"):
		if itchat.search_friends(userName=msg["FromUserName"])["NickName"] in chatroom_nicknames:
			msg.user.send("%s: %s" % (msg.ActualNickName, msg.text))
		else :
			msg.user.send(u"Q酱棒棒哒！")


caocao =  "@0c04671674deb44d6974644b4ff6f968f1c8d5d1b639fb8a48e0d77cb1b51cbf"
shenshen = "@f5814bbfcc757115f660ad5b07e77e4630e06d87af2fa42f611c8a739638bae9"
@itchat.msg_register(TEXT, isGroupChat=False)
def text_reply(msg):
	print(2)
	print(msg)
	if msg['ToUserName'] == "filehelper":
		itchat.send(u"test", toUserName=msg["ToUserName"])
	if msg["FromUserName"] == caocao:
		if(msg.text==u"口一哈"):
			msg.user.send(u"mua")
		else:
			msg.user.send('%s: %s' % (msg.type, msg.text))
	elif msg["FromUserName"] == shenshen:
		msg.user.send(u"叶志晟牛逼！")


itchat.auto_login(True)
itchat.send(u"test",toUserName="caoshengcao1006")
itchat.send(u"auto reply begin", toUserName="filehelper")
itchat.run()
