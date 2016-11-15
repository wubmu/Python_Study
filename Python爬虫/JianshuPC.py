import requests
from bs4 import BeautifulSoup
baseUrl='http://jianshu.com'
#获取URL
page=requests.get(baseUrl).content
#用beautifusoup解析URL
soup=BeautifulSoup(page)
#print(soup.find_all("a",href_=''))
a=soup.select(".title")

print(a[10].a['href'])

add_url = soup.select(".ladda-button")[-1].get("data-url")
article_list = [i.get_text() for i in soup.select( '.title')]
for al in  article_list:
    print(al)
#artict_List=[(i.get_text(),j.get_text) for i,j in (soup.select(".title a"),soup.select("'.title a"))]
#article_list = [i.get_text() for i in soup.select( '.title')]
#for al in  article_list:
# print(al)
