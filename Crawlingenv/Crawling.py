from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

# response = urlopen('https://en.wikipedia.org/wiki/Main_Page')
# soup = BeautifulSoup(response, 'html.parser')
# for anchor in soup.find_all('a'):
#     print(anchor.get('href', '/'))
# 기본 예제

headers = {"User-Agent": "Mozilla/5.0"}# 403 에러 해결 코드
url =Request('https://comic.naver.com/index', headers=headers)
response = urlopen(url)
soup = BeautifulSoup(response, 'html.parser')
f = open('Crawling1', 'w')
rank = 1
for anchor in soup.select('a.tit'):
    data = str(rank)+"등 "+ anchor.get_text()
    rank += 1
    f.write(data)
f.close()