import requests
import pandas as pd
pd.set_option('display.max_colwidth', -1)
page=requests.get("https://www.brainyquote.com/quotes/topics/topic_motivational.html") #Getting page from which quotes will be scraped
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
starting=soup.find(id="quotesList")#Finding the starting point

quotesTable=[]
quote_graber=[]
author=[]
i=1
s=0
stoper=7# Used to see if all quations have been scraped

while s<=stoper:
 try:
  Id="qpos_1_"+str(i) #Getting quote id
  quote_finder=starting.find(id=Id)
  currentQuote = quote_finder.find('a',title="view quote").get_text() #Getting quote from the page
  quote_graber.append(currentQuote)
  currentAuthor = quote_finder.find('a',title="view author").get_text()#Getting author from the page
  author.append(currentAuthor)
  quoteDictionary = {"quote": currentQuote, "author": currentAuthor} #Creating dictonary of quotes and their respective authors
  quotesTable.append(quoteDictionary)
  
  i+=1
  s=0
 except AttributeError:  
  print("no quotationss")
  i+=1
  s=s+1
  continue
  
quotes = pd.DataFrame({.   #Using panads library to create a table
"author": author,
"quotes": quote_graber
     })

print(quotesTable)
print(quotes)
#print(soup.prettify())  

