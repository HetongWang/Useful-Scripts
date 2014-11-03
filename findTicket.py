#-*- coding: UTF-8 -*-
import sys
import urllib, urllib2
import ConfigParser
import json
import time
import smtplib

class FindYW(object):
	def __init__(self, url, train_code, ticket_type):
		self.send_email = False
		self.url = url
		self.train_code = train_code
		self.ticket_type = ticket_type
		self.base_dir = os.path.dirname(__file__)
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
			for train in data['data']:
				if train['queryLeftNewDTO']['station_train_code'] == self.train_code:
					self.train = train
					break
		else:
			self.train = data['data'][0]
	
	def getPassword(self):
		config = ConfigParser.RawConfigParser()
		config.read(os.path.join(self.base_dir, "config.ini"))
		password = config.get('email', 'password')
		return password
	
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
		num = self.train['queryLeftNewDTO'][self.ticket_type]
		print self.train['queryLeftNewDTO']['station_train_code']
		none = u'\u65e0'
		if num != none:
			self.sendEmail()
			self.send_email = True
				

que_url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2014-10-31&leftTicketDTO.from_station=HZH&leftTicketDTO.to_station=KSH&purpose_codes=ADULT'
train_code = 'G44'
ticket_type = 'ze_num'
FindYW(que_url, train_code, ticket_type)