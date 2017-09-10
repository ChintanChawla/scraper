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
quote_finder=starting.find_all(class_="oncl_q")
quote_graber=quote_finder[10]
#quote=quote_graber.find(class_="b-qt qt_389605 oncl_q").get_text()
# above line is showing attribute error  
print(quote_graber.prettify())
#print(quote)
