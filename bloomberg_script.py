import requests
 
url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/news/list"
 
headers = {
    'x-rapidapi-key': "3e11649d4dmsh6e9fdb121a00a60p1a4aabjsn09df86801827",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }
 
from datetime import datetime, timedelta
import json
 
s = '2016-01-07'
s = datetime.strptime(s, '%Y-%m-%d')
 
delta = timedelta(days = 20)
delta += s
# url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-historical-data"
 
print(s, delta)
s, delta = str(datetime.timestamp(s))[:-2], str(datetime.timestamp(delta))[:-2]
 
querystring = {"period1":s,"period2":delta,"category":"generalnews","region":"US", "filter":"history"}
 
response = requests.request("GET", url, headers=headers, params=querystring)
 
res = json.loads(response.text)
for key, value in res.items():
    # item
    for key2, value2 in value.items():
 
        for vals in value2:
            for key3, value3 in vals.items():
                
 
                if(key3=='summary'):
                    dt_object = datetime.fromtimestamp(vals['published_at'])
 
                    print(dt_object, vals[key3])
                # print(key3)
                
            print()
 
import requests
url = ('http://newsapi.org/v2/top-headlines?'
       'sources=bloomberg&'
       'from=2018-12-10&'
       'to=2019-02-10&'
       'apiKey=50791771cb844c0e9ecdb8ddedd9c070')
 
response = requests.get(url)
print (response.json())
