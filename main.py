from urllib.request import urlopen, Request
from itertools import cycle
from threading import Thread
from json import loads
import time, base64, hashlib

#########################################
niggerlist = ['Mario123P0wer'] # unused but essentially banlist
#########################################
userName = "insert username"
password1 = "insert password"
firstACCID = ""
gjp123 = ""
secret = "Wmfd2893gb7"
#########################################

thing = "getGJUsers20"
thing1 = "getGJComments21"
thing2 = "getGJCommentHistory"
thing3 = "uploadGJComment21"

def accountID(user):
    url = f"http://www.boomlings.com/database/{thing}.php"
    params = f"str={user}&total=0&page=0&secret={secret}".encode()
    stuff = urlopen(url, params).read().decode()
    if stuff == "-1":
        return "Failed!"
    else:
        stuff2 = stuff.split(":")[21]
        stuff3 = stuff.split(":")[3]
    return stuff2, stuff3

def getComments(level):
    url = f"http://www.boomlings.com/database/{thing1}.php"
    params = f"page=0&total=0&mode=0&levelID={level}&count=1&secret={secret}".encode()
    stuff = urlopen(url, params).read().decode()
    try:
        stuff2 = base64.urlsafe_b64decode(stuff.split("~")[1].encode()).decode()
        stuff3 = stuff.split("~")[14]
    except:
        print("Failed!")
    return stuff2, stuff3

def gjpEncrypt(password):
    key = '37526'
    xored = xore(password, key)
    based = base64.b64encode(xored.encode())
    based_split = based.decode().split('\'')
    return based_split[0]

def post(level, comment):
    try:
        url = f"http://www.boomlings.com/database/{thing3}.php"
        gjp = gjpEncrypt(password1)
        accID = accountID(userName)[0]
        comm = base64.b64encode(comment.encode("utf-8")).decode()
        chk = getCHK(userName, comment, level)
        params = f"accountID={accID}&gjp={gjp}&userName={userName}&comment={comm}&levelID={level}&percent=69&secret={secret}&chk={chk}".encode()
        stuff = urlopen(url, params).read().decode()
        return "OK"
    except:
        return ""

def xore(data, key):
    return ''.join(chr(ord(a) ^ ord(b)) for (a, b) in zip(data, cycle(key)))

def getCHK(username2, comment2, levelid2):
    salted = username2 + base64.urlsafe_b64encode(comment2.encode("utf-8")).decode() + levelid2 + "69" + "0" + "xPT6iUrtws0J"
    hashed = hashlib.sha1(salted.encode('utf-8'))
    hashed2 = hashed.hexdigest()
    key2 = '29481'
    xored2 = xore(hashed2, key2)
    basedXXX = base64.b64encode(xored2.encode())
    b_split = basedXXX.decode().split('\'')
    return b_split[0]

def getDemons(name):
    if " " in name:
        name = name.replace(" ", "%20")
    url = f"https://www.pointercrate.com/api/v1/demons/?name={name}"
    response = urlopen(url)
    html = response.read().decode()
    x1 = html[1:]
    x2 = x1[:-1]
    try:
        htm2 = loads(x2)
        xxx = ""
        if htm2['verifier']['banned'] == True:
            xxx = "(banned)"
        else:
            xxx = ""
        return f"{htm2['name']} is currently #{htm2['position']} on the list, its verifier is {htm2['verifier']['name']}{xxx}"
    except:
        return "Level is not on demonlist"

def getuserinfo(a2ccountID):
    url = "http://boomlings.com/database/getGJUserInfo20.php"
    a2 = accountID(a2ccountID)
    params = f"accountID={firstACCID}&gjp={gjp123}&targetAccountID={a2}&secret={secret}".encode()
    stuff = urlopen(url, params).read().decode()
    stu2ff = stuff.split(":")
    listedshit = [stu2ff[1], stu2ff[13], stu2ff[15], stu2ff[5], stu2ff[7], stu2ff[17], stu2ff[19]]
    return listedshit

def commentBot(levelID):
    dsplit = getComments(levelID)[0]
    try:
        com = dsplit.split("!demon ")[1]
        ccc = getDemons(com)
        cccc = post(levelID, ccc)
        print("Succ")
    except:
        return ""
    
def source(levelID):
    dsplit = getComments(levelID)[0]
    try:
        com = dsplit.split("!source")[1]
        ccc = "You can find my source code @ github.com/ImNotEnd/gmdbot"
        cccc = post(levelID, ccc)
        print("Succ")
    except:
        return ""

def morestuff(levelID):
    dsplit = getComments(levelID)[0]
    try:
        per = random.randint(0, 100)
        com = dsplit.split("!ship ")[1].split(" x ")
        ccc = f"{com[0]} is {str(per)}% in love with {com[1]}"
        cccc = post(levelID, ccc)
        print("Succ")
    except:
        return ""

x = input("Level ID: ")

z = 1
while True:
    t = Thread(target=commentBot, args=(x,))
    t2 = Thread(target=source, args=(x,))
    t3 = Thread(target=morestuff, args=(x,))
    t.start()
    t2.start()
    t3.start()
    time.sleep(0.3)
