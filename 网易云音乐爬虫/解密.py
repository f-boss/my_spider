"""
:return: encText encSecKey
"""

import binascii
import os
from Crypto.Cipher import AES
import base64


def aes_encrypt(msg, key):
    iv = "0102030405060708"
    pad = 16 - len(msg) % 16
    msg = msg + pad * chr(pad)
    encryptor = AES.new(str.encode(key), mode=AES.MODE_CBC, IV=str.encode(iv))
    result = encryptor.encrypt(str.encode(msg))
    result_str = base64.b64encode(result).decode('utf-8')
    return result_str


def rsa_encrypt(a, b, c):
    a = a[::-1]
    rs = pow(int(binascii.hexlify(a), 16), int(b, 16), int(c, 16))
    return format(rs, 'x').zfill(256)


def encrypt(d, e, f, g):
    i = binascii.hexlify(os.urandom(14))[:16]
    encText = aes_encrypt(d, g)
    encText = aes_encrypt(encText, i.decode('utf-8'))
    encSecKey = rsa_encrypt(i, e, f)
    data = {'params': encText, 'encSecKey': encSecKey}
    return data


# "{"logs":"[{\"action\":\"play\",\"json\":{\"id\":\"1469628663\",\"type\":\"song\"}}]","csrf_token":""}"
# d = '{"logs":"[{"action":"play","json":{"id":"1469628663","type":"song"}}]","csrf_token":""}'
d = '{"ids":"[1455273374]","level":"standard","encodeType":"aac","csrf_token":""}'
e = "010001"
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud"
data = encrypt(d, e, f, g)

import requests
url = 'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Referer': 'http://music.163.com/',
    # 'Cookie': '_iuqxldmzr_=32; _ntes_nnid=ca27115d4e90e6b598b58e9e51eaaddb,1595393206767; _ntes_nuid=ca27115d4e90e6b598b58e9e51eaaddb; WM_TID=B4bsN60hPJBBFVAAFVJ%2BDjt0t5UrOM7U; _ga=GA1.2.497864248.1596960459; NTES_PASSPORT=sRuxxeKTz0ftELt331pC0cvIcCEuf_6.yYRULJnYinfb_q13_H8IY.YFy23KlCmIZcjXsLI6XZyC6HzHBGWzulwcQi.zMspMHn9dqNuv_y7iYlzxRn4XyHawVEnDDl5.wxcOfl4DETxqcdAP5alnEAQ82PKhUY_52jxPUdd9ipaOSQvy9bo9EVbKazg5a4ntskjx7SYgpiJx.; P_INFO=2362315840@qq.com|1596960510|1|codecombat|00&99|gud&1591011974&x19_client#gud&445200#10#0#0|&0||2362315840@qq.com; NTES_CMT_USER_INFO=306291435%7C%E6%9C%89%E6%80%81%E5%BA%A6%E7%BD%91%E5%8F%8B0igqbH%7Chttp%3A%2F%2Fcms-bucket.nosdn.127.net%2F2018%2F08%2F13%2F078ea9f65d954410b62a52ac773875a1.jpeg%7Cfalse%7CMjM2MjMxNTg0MEBxcS5jb20%3D; UM_distinctid=173d24d5a79421-062bf7a3bf8732-335c4c73-1fa400-173d24d5a7a49f; vinfo_n_f_l_n3=0d6effd93289b5c5.1.0.1596961150578.0.1596961171043; JSESSIONID-WYYY=C6SuBn%2FH2odyMh8%5CM51kI7ycXfa7FxzPETgvb40KjgPJTx0GtY6dEGluI2kmKnW%2FOHBrgyWu1x2RIUnYy%2B9kg0WkHC0rKxiyl%2Ft%2FJK5WzvdlZ9hcrCvjP7tvSgl5PcmCJHzlKwrdiWy6Rk7ZmMKtuyiuOQKBso2d9%5CjybwtDkD1qXOS9%3A1597222191753; WM_NI=Is%2BzLqE43hE7h5QnEK%2BfaCBbZo0%2FulyUqmaz85LIm839KdPRgzloHhK7eHKEfA6wTS8mqfCqd85oxVXD%2FxkmfNlGtTKVjSz4pvPhEQ4%2F7ZEsuDQGSl3SY0oSlx4V8%2FU4RzE%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee85cd258ea998a6e63389eb8ea7c84f928e8bafae54b2ef8894c4479187e1b1e82af0fea7c3b92a8bade59bcf7b87ecfd89c83daceb9f8fc841e9baafa4c16a9ab100d0f868bb8bbf8ee472fceb84aaf034f1e78585d35aa5a6a490cb6489e9aba9ca4fa69ffa98d759fcb3bf87c27ba8e8fb90fb5e9c9ce199ea67a692a4a8f760898aa6b4f940b4aaa089c85bf8f1f9bbc879b79c9fa8d268f18d97d1ee59b0a8fcb7bb2597ec9e9bc837e2a3'
}
re = requests.post(url, data=data, headers=headers)
print(re.text)
