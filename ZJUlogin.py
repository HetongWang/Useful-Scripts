import os
import urllib, urllib2
import ConfigParser

class zjulogin(object):

    def __init__(self, configFile):
        self.config = ConfigParser.RawConfigParser()
        self.config.read(configFile)

    def post(self, url, item):
        data = self.config.items(item)
        url = url
        print urllib2.urlopen(urllib2.Request(
            url,
            headers = {'Referer': "https://net.zju.edu.cn/srun_port1.php?"},
            data = urllib.urlencode(data)
        )).read()

login = zjulogin(os.path.join(os.path.dirname(__file__), "config.ini"))
login.post("https://net.zju.edu.cn/rad_online.php", "auto_dm")
login.post("https://net.zju.edu.cn/cgi-bin/srun_portal", "login")
