#!/usr/local/bin/python3
import requests
from itertools import cycle
from threading import Thread
import base64, hashlib
import sys
import random, time
h = {'Content-Type':'application/x-www-form-urlencoded'}
def comment_chk(*,username,comment,levelid,percentage,type):
	part_1 = username + comment + levelid + str(percentage) + type + "xPT6iUrtws0J"
	return base64.b64encode(xor(hashlib.sha1(part_1.encode()).hexdigest(),"29481").encode()).decode()
def xor(data, key):
	return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(data, cycle(key)))
def gjp_encrypt(data):
	return base64.b64encode(xor(data,"37526").encode()).decode()
def gjp_decrypt(data):
	return xor(base64.b64decode(data.encode()).decode(),"37526")
def getGJUsers(target):
	request =  requests.post("http://boomlings.com/database/getGJUsers20.php",f"gameVersion=21&binaryVersion=35&gdw=0&str={target}&total=0&page=0&secret=Wmfd2893gb7",headers=h).text.split(":")[1::2]
	print(request)
	username = request[0]
	uuid = request[2]
	accountid = request[10]
	return (username,accountid,uuid)
def accID(name):
        request =  requests.post("http://boomlings.com/database/getGJUsers20.php",f"gameVersion=21&binaryVersion=35&gdw=0&str={name}&total=0&page=0&secret=Wmfd2893gb7",headers=h).text.split(":")[1::2]
        return request[10]
def getInfo(username,password):
	data = "userName={}&password={}&sID=76561198404485776&udid=5B7A96BC-5702-4FF4-801B-B162EE55C070&secret=Wmfv3899gc9".format(username,password)
	r = requests.post("http://boomlings.com/database/accounts/loginGJAccount.php",data,headers=h).text.split(",")
	print(r)
def uploadGJComment(name,passw,comment,level):
        global h
        h['X-Forwarded-For'] = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
        try:
                accountid = accID(name)
                gjp = gjp_encrypt(passw)
                c = base64.b64encode(comment.encode()).decode()
                chk = comment_chk(username=name,comment=c,levelid=level,percentage="69",type="0")
                return requests.post("http://boomlings.com/database/uploadGJComment21.php",f"gameVersion=21&binaryVersion=35&gdw=0&accountID={accountid}&gjp={gjp}&userName={name}&comment={c}&levelID={level}&percent=69&chk={chk}&secret=Wmfd2893gb7",headers=h).text
        except:
                return
