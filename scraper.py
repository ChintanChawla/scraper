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
#starting=soup.find(id="quotesList")
quote_finder=soup.find(id="qpos_1_3")

counter=1
#while counter<=17:
#quote_graber=quote_finder[0]
#quote=quote_graber.find(class_="zoomc bqpht").get_text() b-qt qt_389605 oncl_q
# above line is showing attribute error  
print(quote_finder.prettify())
      
#counter+=1  
#print(quote)
