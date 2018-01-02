import requests
import json 


from bs4 import BeautifulSoup




quotesTable=[]
quote_graber=[]
author=[]
i=1
s=0
stoper1=15
pg_no=1
header= {'content-type': 'application/json'}

while page.status_code==200:
 page_data={ 

 "ab":"a",
 "id" : "t:132622",
 "langc":"en",
 "m":0,
 "pg":pg_no,
 "typ":"topic",
 "v":"7.1.0c:2479039",
 "vid":"7b363d749b4c7c684ace871c8a75f8e6",
 "cookie":"__cfduid=d30da375ed7d92e2f5c8f1a28c62cf8391504357529;  __gads=ID=4c297e8ad58ea162:T=1504422267:S=ALNI_MaoHwdk8HGWTPtMqYjR1Yuit7Ussg; JSESSIONID=607CE21287D034E988CA59B90FEC7311; bqContNum=5; bqRnd=66; bqPvd=2; _ga=GA1.2.426932399.1504357531; _gid=GA1.2.2009441863.1509680196; __ybotb=ffd8; __ybotu=j74e68jgl5hyl8pr7x; __ybotv=1509680204971; __ybots=j9jclzwjl7b2b73x5a.0.j9jcm5d7kgdwg7xgw1.4; __ybotc=http%3A//ads-adseast-vpc.yldbt.com/m/; __ybotn=1; bqBcavg=500; brainyPrefs=bqHasPrefs_tracelog~off_lastsc~26; abg=b"


 }
 page = requests.post("https://www.brainyquote.com/api/inf",data=json.dumps(page_data),headers=header)


 soup=BeautifulSoup(page.text,'html.parser')
 starting=soup.find(id="quotesList")

 while s<=stoper1: #this loop is to go to next quoter till no quotes are left 
  try:
   Id="qpos_1_"+str(i)
   quote_finder=starting.find(id=Id)
   currentQuote = quote_finder.find('a',title="view quote").get_text()
   quote_graber.append(currentQuote)
   currentAuthor = quote_finder.find('a',title="view author").get_text() 
   author.append(currentAuthor)
   quoteDictionary = {"quote": currentQuote, "author": currentAuthor}
   quotesTable.append(quoteDictionary)
  
   i+=1
   s=0
  except AttributeError:  
   print("no quotationss")
   i+=1
   s=s+1
   continue
 pg_no+=1
 

print(quotesTable)


