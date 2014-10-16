#-*- coding: UTF-8 -*-
import os, sys
import urllib, urllib2
import re
import json
import time
import smtplib

class FindYW(object):
	def __init__(self, url, train_code, ticket_type):
		self.send_email = False
		self.url = url
		self.train_code = train_code
		self.ticket_type = ticket_type
		self.loop()

	def loop(self):
		if self.send_email:
			sys.exit(0)
		else:
			print "no ticket"
			self.seek()
			time.sleep(30)
			self.loop()
	
	def getTrain(self):
		data_json = urllib2.urlopen(self.url).read()
		data = json.loads(data_json)
		if self.train_code:
			for train in data['data']['datas']:
				if train['station_train_code'] == self.train_code:
					self.train = train
					break
		else:
			self.train = data['data']['datas'][0]
	
	def getPassword(self):
		with open('pw.txt', 'r') as f:
			return f.read()
	
	def sendEmail(self):
		smtp = smtplib.SMTP()
		password = self.getPassword()
		msg = 'Subject: 主人主人~ 人家新发现了一张车票，请赶快去抢吧~ 喵呜~~~'
		try:
			smtp.connect('smtp.qq.com', '25')
			smtp.login('hetong583', password)
			smtp.sendmail('hetong583@qq.com', 'hetong583@qq.com', msg)
			smtp.quit()
		except Exception, e:
			print str(e)
	
	def seek(self):
		self.getTrain()
		num = self.train[self.ticket_type]
		print self.train['station_train_code']
		none = u'\u65e0'
		if num != none:
			self.sendEmail()
			self.send_email = True
				

que_url = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate=2014-10-01&from_station=HZH&to_station=KSH'
train_code = 'G7586'
ticket_type = 'ze_num'
FindYW(que_url, train_code, ticket_type)

train_code = 'G7584'
ticket_type = 'ze_num'
FindYW(que_url, train_code, ticket_type)