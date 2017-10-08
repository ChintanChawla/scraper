import requests
import pandas as pd
#pd.set_option('display.max_colwidth', -1)
page=requests.get("https://www.brainyquote.com/quotes/topics/topic_motivational.html")
page
page.status_code
page.content
from bs4 import BeautifulSoup
soup=BeautifulSoup(page.content,'html.parser')
#print (list(soup.children))
#print([type(item)for item in list(soup.children)])
#html=list(soup.children)
#body=list(html.children)
#print(soup.find_all(id="first"))
#print(soup.find_all('p')[0].get_text())
starting=soup.find(id="quotesList")

quote_graber=[]
author=[]
i=5

while i<=10:
 Id="qpos_1_"+str(i)
 quote_finder=starting.find(id=Id)
 quote_graber.append(quote_finder.find_all('a')[1].get_text())
 author.append(quote_finder.find_all('a')[2].get_text())
 #print(quote_graber + '-'+ author)
 #print(author)
 i+=1


quotes = pd.DataFrame({
"author": author,
"quotes": quote_graber
     })

print(quotes)
#print(soup.prettify())  

