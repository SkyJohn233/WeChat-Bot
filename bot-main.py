# -*- encoding:utf-8 -*-
# created by SkyJohn

import time
import itchat
from itchat.content import *
from get_room_ids import *
import requests
import random
from datetime import datetime
# FromUserNames in the group chat

@itchat.msg_register(TEXT, isGroupChat=True)
def group_text_reply(msg):
	if msg["FromUserName"] in chatroom_ids :
		print(1)
		print(msg)
		search_answer = itchat.search_friends(userName=msg["ActualUserName"])
		print(search_answer)
		friend_name = search_answer["RemarkName"]
		if friend_name is None or friend_name is "" :
			friend_name =search_answer["NickName"]
		if friend_name in chatroom_nicknames:
			pass
			# msg.user.send("%s: %s" % (msg.ActualNickName, "sb"))
		else :
			msg.user.send(u"Q酱棒棒哒！")
	if msg["ToUserName"] in chatroom_ids:
		msg.user.send(u"Q酱棒棒哒")


@itchat.msg_register([PICTURE], isGroupChat=True)
def group_picture_reply(msg):
	print(msg)
	if msg["FromUserName"] in chatroom_ids :
		print(1.5)
		search_answer = itchat.search_friends(userName=msg["ActualUserName"])
		print(search_answer)
		friend_name = search_answer["RemarkName"]
		if friend_name is None or friend_name is "" :
			friend_name =search_answer["NickName"]
		if friend_name in chatroom_nicknames:
			# msg.user.send("%s%s" % (msg.ActualNickName, "sb"))
			sticking_num = 9
			sticking =random.randint(1,sticking_num)
			print(sticking)
			msg.user.send_image(str(sticking)+".jpg")
		else:
			msg.user.send(u"Q酱大帅比")
	if msg["ToUserName"] in chatroom_ids:
		msg.user.send(u"Q酱大帅比")


caocao =  "@0c04671674deb44d6974644b4ff6f968f1c8d5d1b639fb8a48e0d77cb1b51cbf"
shenshen = "@f5814bbfcc757115f660ad5b07e77e4630e06d87af2fa42f611c8a739638bae9"
@itchat.msg_register(TEXT, isGroupChat=False)
def text_reply(msg):
	print(2)
	print(msg)
	if msg['ToUserName'] == "filehelper":
		itchat.send(u"test", toUserName=msg["ToUserName"])
		url = msg.text
		try:
			r=requests.get(url,verify=False)
			filepath = r"C:\Users\skyjohn\Desktop\wechat"
			filepath += '\\'+url.split('/')[-1]
			with open(r"C:\Users\skyjohn\Desktop\wechat\1.pdf","wb") as file_:
				file_.write(r.content)
		except:
			print("Url download failed") 		
	if msg["FromUserName"] == caocao:
		if(msg.text==u"口一哈"):	
			msg.user.send(u"mua")
		else:
			msg.user.send('%s: %s' % (msg.type, msg.text))
	elif msg["FromUserName"] == shenshen:
		msg.user.send(u"叶志晟牛逼！")


my_uuid = "@a0d8a365cce9931ab7c85880bd3e2272bce8138090d10fbd300a3948554ee5e1"
@itchat.msg_register([PICTURE], isGroupChat=False)
def picture_reply(msg):
	print(2.5)
	print(msg)
	picture_sender=msg["FromUserName"]
	if picture_sender in[ caocao, shenshen] :
		sticking_num = 9
		sticking =random.randint(1,sticking_num)
		print(sticking)
		itchat.send_image(str(sticking)+".jpg", toUserName=picture_sender)
	if picture_sender == my_uuid:
		sticking_num = 9
		sticking = random.randint(1,sticking_num)
		print("2.5.2")
		itchat.send("send image"+str(sticking)+".jpg",toUserName="filehelper")
		itchat.send_image(str(sticking)+".jpg",toUserName="filehelper")



@itchat.msg_register([ATTACHMENT])
def download_files(msg):
	if(msg["ToUserName"]!="filehelper"): return None
	print(msg)
	msg.download(msg.filename)

itchat.auto_login(True)
itchat.send(u"auto reply begin", toUserName="filehelper")
random.seed(time.time())
# print(itchat.search_friends(userName="@dea0e53b8d4678cbb5c685953ebd2973ed99e9511c70999e7bbafbf4d35ea467"))
# print(itchat.search_friends(userName=shenshen))
# print(itchat.search_friends(userName=caocao))
itchat.run()
