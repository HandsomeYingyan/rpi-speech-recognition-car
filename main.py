#!/usr/bin/env python
#encoding=utf8
import wave
import urllib, urllib2, pycurl
import os,time
import base64
import json
## get access token by api key & secret key

def get_token():
    apiKey = "yaVhQIugoYZw3If2OvramwhS"
    secretKey = "ac4e6386bb36d0c9ca4b03a190fbfa9a"
    auth_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + apiKey + "&client_secret=" + secretKey;
    res = urllib2.urlopen(auth_url)
    json_data = res.read()
    return json.loads(json_data)['access_token']

def dump_res(buf):
    print buf

luyin = time.time()
def ly():
    os.system('mplayer sc/hello.wav')
    os.system('arecord -D "plughw:0,0" -r 16000 -t wav -d 2 -f S16_LE -c 1  lu/%s.wav'%luyin)

def sc(wenzi):
    global shuchu
    shuchu = time.time()
    url = 'http://tsn.baidu.com/text2audio?tex='+wenzi+'&lan=zh&cuid="68-5D-43-F5-62-84"&ctp=1&tok=24.6f29c64c826ace25429223f88b2ca8e2.2592000.1451549761.282335-7227233'
    urld = urllib2.urlopen(url)
    urldata = urld.read()
    f = open('sc/%s.wav'%shuchu,'ab')
    f.write(urldata)
    f.close()
    
    
token = get_token()
def upurl():
    CE_RATE = 16000
    WAVE_FILE = 'lu/%s.wav'%luyin
    USER_ID = "68-5D-43-F5-62-84"
    WAVE_TYPE = 'wav'
    URL = 'http://vop.baidu.com/server_api'
    f = open(WAVE_FILE,'r')
    speech = base64.b64encode(f.read())
    size = os.path.getsize(WAVE_FILE)
    update = json.dumps({'format':WAVE_TYPE,'rate':CE_RATE,'channel':1,'cuid':USER_ID,'token':token,'speech':speech,'len':size})
    r = urllib2.urlopen(URL,update)
    t = r.read()
    return json.loads(t)
while True:
    ly()
    result = upurl()
    print result
    print result[u'err_msg']
    aa = result['result'][0]
    print aa
    if 'success' in  result[u'err_msg']:
       if u'歌曲，' ==  aa:
          sc('请选择')
          time.sleep(1)
          os.system('mplayer sc/asksong.wav')
          time.sleep(1)
       elif u'你好，' ==  aa:
          sc('你好呀!')
          os.system('mplayer sc/name.wav')
          os.system('mplayer sc/finish.wav')
          time.sleep(1)
       elif u'前进，' in  aa:
          sc('执行!')
          os.system('sudo python contror/NEXT.py')
          os.system('mplayer sc/finish.wav')
          time.sleep(1)
       elif u'后退，' in  aa:
          sc('执行!')
          os.system('sudo python contror/BACK.py')
          os.system('mplayer sc/finish.wav')
          time.sleep(1) 
       elif u'向左，' in  aa:
          sc('执行!')
          os.system('sudo python contror/LEFT.py')
          os.system('mplayer sc/finish.wav')
          time.sleep(1)
       elif u'向右，' in  aa:
          sc('执行!')
          os.system('sudo python contror/RIGHT.py')
          os.system('mplayer sc/finish.wav')
          time.sleep(1)
       elif u'转圈，' in  aa:
          sc('执行!')
          os.system('sudo python contror/ROUND.py')
          os.system('mplayer sc/finish.wav')
          time.sleep(1)
       elif u'笑话，' in  aa:
          sc('执行!')
          os.system('mplayer sc/askjoke.wav')
          time.sleep(1)
       elif u'三，' in  aa:
          sc('执行!')
          os.system('sudo mplayer sc/joke1.wav')
          os.system('mplayer sc/finish.wav')
          time.sleep(1)
       elif u'四，' in  aa:
          sc('执行!')
          os.system('sudo mplayer sc/joke2.wav')
          os.system('mplayer sc/finish.wav')
          time.sleep(1)
       elif u'重启，' in  aa:
          sc('执行!')
          os.system('mplayer sc/askrest.wav')
          time.sleep(1)
       elif u'五，' in  aa:
          sc('执行!')
          os.system('sudo mplayer sc/gorest.wav')
          os.system('sudo reboot')
          time.sleep(1)
       elif u'六，' in  aa:
          sc('执行!')
          os.system('sudo mplayer sc/cancel.wav')
          time.sleep(1)
       elif u'关机，' in  aa:
          sc('执行!')
          os.system('mplayer sc/askoff.wav')
          time.sleep(1)
       elif u'七，' in  aa:
          sc('执行!')
          os.system('sudo mplayer sc/gooff.wav')
          os.system('sudo poweroff')
          time.sleep(1)
       elif u'一，' in  aa:
          sc('执行!')
          os.system('sudo mplayer yy/1.mp3')
          os.system('mplayer sc/finish.wav')
          time.sleep(1)
       elif u'二，' in  aa:
          sc('执行!')
          os.system('sudo mplayer yy/2.mp3')
          os.system('mplayer sc/finish.wav')
          time.sleep(1)

       else :
          sc('很抱歉，没有听清楚，可以重新说一遍吗？')
          os.system('mplayer sc/error.wav')

