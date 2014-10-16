import os
import urllib, urllib2

file = open('info', 'r')
username = file.readline()[0:10]
password = file.readline()
url = "https://net.zju.edu.cn/rad_online.php"
d = {
    'action': 'auto_dm',
    'username': username,
    'password': password
}
urllib2.urlopen(urllib2.Request(
    url,
    headers = {'Referer': "https://net.zju.edu.cn/srun_port1.php?"},
    data = urllib.urlencode(d)
))
print d

url = "https://net.zju.edu.cn/cgi-bin/srun_portal"
d = {
	'action': 'login',
	'username': username,
	'password': password,
	'ac_id': 3,
	'type': 1,
	'wbaredirect': "www.baidu.com"
}
print urllib2.urlopen(urllib2.Request(
	url, 
	headers = {'Referer': "https://net.zju.edu.cn/srun_port1.php"},
	data = urllib.urlencode(d)
)).read()