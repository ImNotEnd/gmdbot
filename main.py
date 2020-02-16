from urllib.request import urlopen, Request
from itertools import cycle
from threading import Thread
from json import loads
from t import translateXXX
import time, base64, hashlib, random, bettercomm

#########################################
f = open("banana.txt", "r+")

n = f.read().split(";")

admins = ['lnine', 'akfez']
#########################################
userName = input("Enter bot name: ")
password1 = input("Enter bot password: ")
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
    dsplit = getComments(levelID)
    com = dsplit[0]
    nam = dsplit[1]
    if nam.lower() in n:
        time.sleep(3)
    else:
        try:
            come = com.split("!demon ")[1]
            ccc = getDemons(come)
            bettercomm.uploadGJComment(userName, password1, ccc, levelID)
            print("Succ")
        except:
            return ""

def source(levelID):
    dsplit = getComments(levelID)[0]
    try:
        com = dsplit.split("!source")[1]
        ccc = "You can find my source code @ github.com/ImNotEnd/gmdbot"
        bettercomm.uploadGJComment(userName, password1, ccc, levelID)
        print("Succ")
    except:
        return ""

def morestuff(levelID):
    dsplit = getComments(levelID)
    com = dsplit[0]
    nam = dsplit[1]
    if nam.lower() in n:
        time.sleep(5)
    else:
        try:
            per = random.randint(0, 100)
            come = com.split("!ship ")[1].split(" x ")
            ccc = f"{come[0]} is {str(per)}% in love with {come[1]}"
            bettercomm.uploadGJComment(userName, password1, ccc, levelID)
            print("Succ")
        except:
            return ""

def ggay(levelID):
    dsplit = getComments(levelID)
    com = dsplit[0]
    nam = dsplit[1]
    if nam.lower() in n:
        time.sleep(5)
    else:
        try:
            per = random.randint(0, 100)
            come = com.split("!howgay ")[1]
            ccc = f"{come} is {str(per)}% gay"
            bettercomm.uploadGJComment(userName, password1, ccc, levelID)
            print("Succ")
        except:
            return ""

def banning(levelID):
    dsplit = getComments(levelID)
    com = dsplit[0]
    nam = dsplit[1]
    if nam.lower() in admins:
        try:
            ds = com.split("!ban ")[1].lower()
            with open("banana.txt", "a") as zxz:
                zxz.write(f";{ds}")
                zxz.close()
            ccc = f"{ds} has been banned."
            bettercomm.uploadGJComment(userName, password1, ccc, levelID)
            time.sleep(3)
            print("Succ")
        except:
            return ""
    else:
        time.sleep(5)

def chknm(levelID):
    ninds = getComments(levelID)
    dsplit = ninds[0]
    nam = ninds[1]
    if nam.lower() in n:
        time.sleep(5)
    else:
        try:
            come = dsplit.split("!checkname ")[1]
            result = accountID(come)
            if result == "Failed!":
                result1 = "not taken"
            else:
                result1 = "taken"
            ccc = f"@{nam}, {come} is {result1}"
            bettercomm.uploadGJComment(userName, password1, ccc, levelID)
            print("Succ")
        except:
            return ""

def translateBot(levelID):
    dsplit = getComments(levelID)
    com = dsplit[0]
    nam = dsplit[1]
    if nam.lower() in n:
        time.sleep(3)
    else:
        try:
            if com.startswith("!translate "):
                come = com.split("!translate ")[1].split(" | ")[0]
            lang = com.split(" | ")[1].split(" / ")[0]
            dest = com.split(" | ")[1].split(" / ")[1]
            pp = translateXXX(come, lang, dest)
            ccc = f"@{nam}, {pp}"
            bettercomm.uploadGJComment(userName, password1, ccc, levelID)
            print("Succ")
        except:
            return ""
    time.sleep(7)

xxxx = input("Level ID: ")

z = 1
while True:
    t = Thread(target=commentBot, args=(xxxx,))
    t2 = Thread(target=source, args=(xxxx,))
    t3 = Thread(target=morestuff, args=(xxxx,))
    t4 = Thread(target=chknm, args=(xxxx,))
    t5 = Thread(target=banning, args=(xxxx,))
    t6 = Thread(target=ggay, args=(xxxx,))
    t7 = Thread(target=translateBot, args=(xxxx,))
    t.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    time.sleep(0.3)
