import csv
import requests
import urllib.request
import urllib.parse
import json as m_json
from googlesearch import search
data=[]
ifile  = open('sss.csv', "rt", encoding="utf-8")
read = csv.reader(ifile)
for row in read :
    print (row)
    data.append(row)
print(data)
for a in data:
    str1 = ''.join(str(e) for e in a)
    query = str1
    for j in search(query, tld="co.in", num=4, stop=1, pause=2):
                   print(j)
##    query1 = urllib.parse.quote(str1)
##    response = urllib.request.urlopen ( 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query1 ).read()
##    print(response)
##    json = m_json.loads ( response )
##    results = json [ 'responseData' ] [ 'results' ]
##    for result in results:
##        title = result['title']
##        url = result['url']   # was URL in the original and that threw a name error exception
##        print ( title + '; ' + url )
