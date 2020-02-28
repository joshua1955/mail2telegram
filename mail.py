import easyimap
import telebot
import urllib
import socket
import socks
import time
import os
from telebot import apihelper


#Specify your mail
login = 'username@example.com'
password = 'secret'
mailbox = "INBOX"

#Specify your telegram bot and id
token = "yyyy:xxxxx"
chat_id = '123456789'

bot = telebot.TeleBot(token)

#Specify your proxy
apihelper.proxy = {'https': 'socks5://sockduser:server.com:port'}
id=0

#def attachmentSend(docpath):
#	global bot
#	global chat_id
#	doc = open(docpath, 'rb')
#	bot.send_document(chat_id, doc)

def textSend(text):
	global bot
	global chat_id
	bot.send_message(chat_id, text, disable_web_page_preview=True)

imapper = easyimap.connect('imap.example.ru', login, password, mailbox)
lastdate = None
while True:
	mail = imapper.listup(1)[0]
	id_new=mail.message_id
	if mail.date!=lastdate and id_new!=id:
		textSend(mail.date + ' from ' +mail.from_addr + mail.title + ' - ' + mail.body)
		print(mail)
		print("Send")
		id=mail.message_id
#        for attachment in mail.attachments:
#            if not os.path.exists("attachments/"+mail.date[5:15].replace(' ','')+'/'):
#                os.makedirs("attachments/"+mail.date[5:15].replace(' ','')+'/')
#            f = open("attachments/"+mail.date[5:15].replace(' ','')+'/' + attachment[0], "wb+")
#            f.write(attachment[1])
#           f.close()
#            attachmentSend("attachments/"+mail.date[5:15].replace(' ','')+'/')
#        lastdate = mail.date
	else:
		continue









