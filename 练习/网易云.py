import requests

url = 'https://music.163.com/weapi/comment/resource/comments/get'

data = {
  "csrf_token":"",
  "cursor": "-1",
  "offset": "0",
  "orderType": "1",
  "pageNo": "1",
  "pageSize": "20",
  "rid": "R_SO_4_357279",
  "threadId": "R_SO_4_357279",
}

# 处理加密

"""
function d(d, e, f, g) {
    var h = {}
      , i = a(16);
    return h.encText = b(d, g),
    h.encText = b(h.encText, i),
    h.encSecKey = c(i, e, f),
    h
}

d : JSON.stringify(i5n)
e : bsi0x(["流泪", "强"]) '010001'
f : bsi0x(BT1x.md)  '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
g : bsi0x(["爱心", "女孩", "惊恐", "大笑"]) '0CoJUm6Qyw8W8jud'
"""
