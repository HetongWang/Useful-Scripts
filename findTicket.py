#-*- coding: UTF-8 -*-
import sys, os
import urllib2
import ConfigParser
import json
import time
import smtplib
from datetime import datetime

class FindYW(object):
	def __init__(self):
		self.base_dir = os.path.dirname(__file__)
		config = ConfigParser.RawConfigParser()
		config.read(os.path.join(self.base_dir, "config.ini"))
		self.target_email = config.get('ticket', 'target_email')
		self.query_url = config.get('ticket', 'query_url')
		self.train_code = config.get('ticket', 'train_code')
		self.ticket_type = config.get('ticket', 'ticket_type')
		self.email_password = config.get('ticket', 'password')
		self.send_email = False
		self.loop()

	def loop(self):
		while (not self.send_email):
			self.seek()
			time.sleep(10)
		sys.exit(0)
	
	def getTrain(self):
		now = datetime.now()
		print now
		data_json = urllib2.urlopen(self.query_url).read()
		data = json.loads(data_json)
		for train in data['data']:
			if train['queryLeftNewDTO']['station_train_code'] == self.train_code:
				self.train = train['queryLeftNewDTO']
				break
	
	def sendEmail(self):
		smtp = smtplib.SMTP()
		password = self.email_password
		msg = 'Subject: 主人主人~ 人家新发现了一张车票，请赶快去抢吧~ 喵呜~~~'
		smtp.connect('smtp.qq.com', '25')
		smtp.login('hetong583', password)
		smtp.sendmail('hetong583@qq.com', self.target_email, msg)
		smtp.sendmail('hetong583@qq.com', 'hetong583@qq.com', msg)
		smtp.quit()
	
	def seek(self):
		try:
			self.getTrain()
			num = self.train[self.ticket_type]
			none = u'\u65e0'
			if num != none:
				self.sendEmail()
				self.send_email = True
			else:
				print "no ticket, do next try after 10 seconds"
		except KeyError:
			print 'Error:', 'query failed'
		except Exception as e:
			print 'Error:', e
				

FindYW()