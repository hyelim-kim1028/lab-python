import requests
from bs4 import BeautifulSoup

#접속할 주소
# 다음에서 '머신 러닝'을 검색하고 그 주소값을 url 값에 넣어줌
url = 'https://search.daum.net/search?w=news&nil_search=btn&DA=NTB&enc=utf8&cluster=y&cluster_page=1&q=%EB%A8%B8%EC%8B%A0%20%EB%9F%AC%EB%8B%9D'

# 사이트(웹 서버)에 요청(requests)를 보냄
# html = requests.get(url).text
# 아래에서 strip(공백들을 제거하기 위해서)을 추가한 코드와 같은 코드이다
# print(html)

#url을 알아내는/요청하는 방식 1) get 2) post
#두 방식의 차이점
# Get method: 웹 서버에서 검색어를 보내고, 서버로 보내는 데이터가 주소에 함께 포함이 됨
# 이 데이터에는 검색어 외에도 다른 정보등리 감춰져서 서버로 보내짐

# post method
# encia la informacion ocultada
# 주소에 아무런 정보가 표시되지 않는다 그래서 브라우저에서 보내는 방식의 기준은 get방식이다

# print(html[0:100])
# 문자열 slicing 가능가능
# 전체 문자열에서 100자만 확인 (너무 많으니까)
# 앞에 공백이 들어와 있고, <!doctype html> 부터 lang = "ko

html = requests.get(url).text.strip()
# print(html)

# 전체 링크만 찾아서 출력해보기
# 1. BeautifulSoup 객체 생성
soup = BeautifulSoup(html, 'html5lib')

#2. HTML 문서의 모든 링크에 걸려 있는 주소들을 출력
links = soup.find_all('a')
for link in links:
    print(link.get('href'))

# 3. Extract links of news articles
div_coll_cont = soup.find_all(class_ = 'coll_cont')
print(len(div_coll_cont))

news_link = soup.select('.coll_cont ul li a.f_link_b')
for link in news_link:
    print(link.get('href'))

