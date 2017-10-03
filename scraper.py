import requests
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


i=5
while i<=10:
 Id="qpos_1_"+str(i)
 quote_finder=starting.find(id=Id)
 quote_graber=quote_finder.find_all('a')[1].get_text()
 author=quote_finder.find_all('a')[2].get_text()
 print(quote_graber + '-'+ author)
 i+=1

#quote=quote_graber.find(class_="zoomc bqpht").get_text() b-qt qt_389605 oncl_q
# above line is showing attribute error  
#print(quote_graber.prettify())

      
#counter+=1  
#print(quote)
