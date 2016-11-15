import requests
from bs4 import BeautifulSoup
baseUrl='http://jianshu.com'
#获取URL
page=requests.get(baseUrl).content
#用beautifusoup解析URL
soup=BeautifulSoup(page)
#print(soup.find_all("a",href_=''))
add_url = soup.select(".ladda-button")[-1].get("data-url")
page2=requests.get(baseUrl+''+add_url)
soup2=BeautifulSoup(page2)
#print(soup2.select(".title a"))
#artict_List=[(i.get_text(),j.get_text) for i,j in (soup.select(".title a"),soup.select("'.title a"))]
article_list = [i.get_text() for i in soup2.select( '.title')]
for al in  article_list:
    print(al)
    print(2)