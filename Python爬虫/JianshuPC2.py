from bs4 import BeautifulSoup
import requests
url=requests.get('http://www.jianshu.com/top/daily?note_ids%5B%5D=6971775&note_ids%5B%5D=6921213&note_ids%5B%5D=6880553&note_ids%5B%5D=6962991&note_ids%5B%5D=6971400&note_ids%5B%5D=6855868&note_ids%5B%5D=6965610&note_ids%5B%5D=6960967&note_ids%5B%5D=6862760&note_ids%5B%5D=6962163&note_ids%5B%5D=6883567&note_ids%5B%5D=6850879&note_ids%5B%5D=6819395&note_ids%5B%5D=6971309&note_ids%5B%5D=6957088&note_ids%5B%5D=6972701&note_ids%5B%5D=6967563&note_ids%5B%5D=6969161&note_ids%5B%5D=6957971&note_ids%5B%5D=6906587&note_ids%5B%5D=6960951&page=2')
print(url)
#print(url.content)
soup=BeautifulSoup(url.content)#content是关键
#i=soup.select('.title a')[10].get('href')
#print(i)
article_list = [i.get_text() for i in soup.select( '.wrap-img')]
for al in  article_list:
    print(al)
