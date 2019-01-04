import urllib.request
import json



res = urllib.request.urlopen('https://picsum.photos/200/?random').read()
#res_body = res.read()

# https://docs.python.org/3/library/json.html
#j = json.loads(res)

print(res)


res = urllib.request.urlopen('http://www.boredapi.com/api/activity/')
res_body = res.read()

# https://docs.python.org/3/library/json.html
j = json.loads(res_body.decode("utf-8"))
activity = j['activity']

print(activity)
