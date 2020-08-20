import urllib.request as req
from urllib.parse import urlparse
from urllib.parse import urlencode

url = "http://www.encar.com"

mem = req.urlopen(url)

#print(type(mem))

"""
print(type({}))
print(type([]))
print(type(()))
"""

"""
print("geturl",mem.geturl())
print("status",mem.status) # 200, 404, 403, 500
print("headers",mem.getheaders())
"""

"""
print("info",mem.info())
print("code",mem.getcode())
"""

#print("read",mem.read())
#print("read",mem.read(50))  # 50 bytes
#print("read",mem.read(50).decode("utf-8")) # euc-kr ...

print(urlparse("http://www.encar.com?test=test&x=x"))

API = "https://api.ipify.org"

values = {'format' : 'json'}

print('before', values)

params = urlencode(values)
print('after', params)

url = API + "?" + params
print("요청 url", url)

reqData = req.urlopen(url).read().decode('utf-8')
print("출력", reqData)
