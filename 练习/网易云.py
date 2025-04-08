import requests
import json
from Crypto.Cipher import AES
from base64 import b64encode

url = 'https://music.163.com/weapi/comment/resource/comments/get'

data = {
  "csrf_token":"",
  "cursor": "-1",
  "offset": "0",
  "orderType": "1",
  "pageNo": "1",
  "pageSize": "30",
  "rid": "R_SO_4_357279",
  "threadId": "R_SO_4_357279",
}

# 处理加密

""" 
返回随机的16位字符串
function a(a) {
  var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
  for (d = 0; a > d; d += 1)
      e = Math.random() * b.length,
      e = Math.floor(e),
      c += b.charAt(e);  
  return c
}

function b(a, b) {
  var c = CryptoJS.enc.Utf8.parse(b)
    , d = CryptoJS.enc.Utf8.parse("0102030405060708")
    , e = CryptoJS.enc.Utf8.parse(a)
    , f = CryptoJS.AES.encrypt(e, c, { 
      iv: d,  偏移量 
      mode: CryptoJS.mode.CBC 模式cbc
  });
  return f.toString()
}

function c(a, b, c) {
  var d, e;
  return setMaxDigits(131),
  d = new RSAKeyPair(b,"",c),
  e = encryptedString(d, a)
}

function d(d, e, f, g) {
    var h = {}
      , i = a(16);    # 随机生成16位字符串
    return h.encText = b(d, g),
    h.encText = b(h.encText, i),
    h.encSecKey = c(i, e, f), 两次加密
    h
}

d : JSON.stringify(i5n)  数据
e : bsi0x(["流泪", "强"]) '010001'
f : bsi0x(BT1x.md)  '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
g : bsi0x(["爱心", "女孩", "惊恐", "大笑"]) '0CoJUm6Qyw8W8jud'
i : 5Y58c1GBIMaDeS1Z
encSecy = "74588298141e70e589a700976a715bba2589ee145cb5f9068fe6896505465a8af28fa3902bb733da285412f83593ff14e25091c085920874d630ef22bc8e009bd9ab6076c358e3ffdd508534f4a660782c16acf184618d6a6521add572dbf145a7adc3eaf0d7dc32370194fbefa0e5caa03b81d927d387355544e09a8b9aaa09"
"""
def to_16(data):
    pad = 16 - len(data) % 16
    data += pad * chr(pad)
    return data

def get_encSecy():
    return "74588298141e70e589a700976a715bba2589ee145cb5f9068fe6896505465a8af28fa3902bb733da285412f83593ff14e25091c085920874d630ef22bc8e009bd9ab6076c358e3ffdd508534f4a660782c16acf184618d6a6521add572dbf145a7adc3eaf0d7dc32370194fbefa0e5caa03b81d927d387355544e09a8b9aaa09"

def get_params(data):
    g = '0CoJUm6Qyw8W8jud'
    i = '5Y58c1GBIMaDeS1Z'
    first = enc_params(data, g)
    second = enc_params(first, i)
    return second

def enc_params(data,key):
    iv = '0102030405060708'
    data = to_16(data)
    aes = AES.new(key=key.encode("utf-8"), IV=iv.encode("utf-8"), mode=AES.MODE_CBC)
    bs = aes.encrypt(data.encode("utf-8")) # 加密 长度必须是16的倍数
    return b64encode(bs).decode("utf-8")

res = requests.post(url=url, data={
    'params': get_params(json.dumps(data)),
    'encSecKey': get_encSecy()
})

info = res.json()['data']['hotComments']

for i in info:
    print(i['content'])