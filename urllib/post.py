import urllib.request
import urllib.parse
import json
# url = 'https://tianchang.art/handbook/geekVerse/%E5%BC%80%E6%BA%90%E5%8D%B3%E8%B4%A3%E4%BB%BB.html'

# urllib.request.urlretrieve(url,'tianchang.html')
# print('下载完成')

url = 'https://fanyi.baidu.com/ait/text/translate'

# params = {
#   'aid': 2608,
#   'uuid': 7353547692041569828,
#   'spider': 0,
#   'verifyFp': 'verify_m6yczs64_3oeew7Np_kOt4_4Y7F_9Llj_JfljWHLCH8rr',
#   'fp': 'verify_m6yczs64_3oeew7Np_kOt4_4Y7F_9Llj_JfljWHLCH8rr',
#   'msToken': 'U0evEs9ZucgHlyc2RmCdjs5GMKVdQwii1IMy0YCVzL3DtJIHmC0MN3IxV6ZceMmip4PH2k_1xyi_cE_KHj8LMtdXR6mmR9MTckd9K9EbOs4MFg72csT5mBe5O_z8HeAG',
#   'a_bogus': 'Qf0DDOZ4Msm1haWRshDz9bKthdy0YW45gZEPxJybmtLI'
# }

data = {
  'corpusIds':[],
  'domain':'common',
  'from':'en',
  'milliTimestamp':1740557643968,
  'needPhonetic':'true',
  'query':'hello',
  'reference':'',
  'to':'zh',
}

# new_params = urllib.parse.urlencode(params)

# new_url= url + new_params

new_data = urllib.parse.urlencode(data).encode('utf-8')

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'cookie':'BAIDUID_BFESS=DD75435B8F6A813C3C6F7724B421FF13:FG=1; PSTM=1731896838; BIDUPSID=AF5D454E4F1F2CCB873C67D9EFA3ACDE; ZFY=vZoRDXXMlrJbqZsVuiPt:Bv7lKJckzpyZoJjoDFKDWYo:C; H_PS_PSSID=61027_61667_61985_62054_62067_62073_62087_62107_62100_62095_62111_62159; RT="z=1&dm=baidu.com&si=84b707b9-5346-4323-a208-80677d985e6e&ss=m7ln2i4r&sl=4&tt=2vq&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf"; ab_sr=1.0.1_ODMxZDhiMTBhNDBhOTllNjNlMmRjZDc0ZGQwMjdhZDFiYTU5MzkzMjdhZTFhMWI0MjhjNDljYTA5MTJkNmQ4ZDZmOGVjYTgwNjdjMjg4ZWY3MjRhNGU3ZDAwODE3MGUwNWExZDFjMDJlMTFmN2E3Njk4MmRiNmRmNzcwM2E0NDFhMzU5NjE4ZjFlNTc1OTQ1NGJjMWEyNGE0OTNlZThhOQ==',
    'acs-token':'1740542812540_1740558635175_RhIPCnR/g8VNzVX7mroW2JMd9xSYsFAMLdKNhOnUbn/2uNta76qzwhWQoMGhwTffCp2bp9fX4KHXAXtD5b55n0XoIP7wFcYoscOjt56dnHjJcC59vSvAHiYsB4gBtPHddfAbIndChKSfNSUcuHDwD7rJNWvl5c7WBJW6JZGINFd1DOYUmliJlJGRduO43D68zmZVYFj1LCr0qxACG+9OI/EfEFI/pxD1SN2cwy8bryi9a1l0PKO4M9cXL2nbl2ooQEaBeIMfPJyhVZHAfYlfbkqnpYhGqmH3hxh1kdMWXeFEtnrFoM4amWH1jW/4esYdvEWBSJQkKPnlUjgd8dBuOrabifCFk2xfGwFrWM3PpSXfESzddffyh/2gaLqtNiCjrAouiA51r4UASScneX+5hWsJgvESRak1UugrBuEFm2Edrz2YaIXW+Ml3eUnpnuN9',
    'host':'fanyi.baidu.com',
}

req = urllib.request.Request(url=url,data=new_data,headers=headers,method='POST')

res = urllib.request.urlopen(req)

content = res.read().decode('utf-8')

# content_json = json.loads(content)

print(content)
# print(content_json)