import os
import urllib, urllib2
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('E:\GitHub\Python_pro\config.ini')
username = config.get('zjulogin', 'username')
password = config.get('zjulogin', 'password')
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