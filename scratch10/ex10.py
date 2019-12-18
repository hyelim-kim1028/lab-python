import requests
from bs4 import BeautifulSoup

#접속할 주소
# 다음에서 '머신 러닝'을 검색하고 그 주소값을 url 값에 줌
url = 'https://search.daum.net/search?w=news&q=%EB%A8%B8%EC%8B%A0%20%EB%9F%AC%EB%8B%9D&DA=PGD&spacing=0&p=1'

# 사이트(웹 서버)에 요청(requests)를 보냄
html = requests.get(url).text
# 아래에서 stip (공백들을 제거하기 위해서)을 추가한 코드와 같은 코드이다
print(html)

# url을 알아내는/요청하는 방식 1) get   2) post
# 두 방식의 차이점:
# GET method:
# 웹 서버로 검색어(i.e. 머신 러닝)를 보내고 -> 서버로 보내는 데이터가 주소에 함께 포함이 된다
# https://search.daum.net/search?nil_suggest=btn&w=news&DA=SBC&cluster=y&q=Machine+Learning+
# 이 데이터에는 검색어 외에도 다른 정보들이 감춰져서 서버로 보내짐

# post method
# envia la informacion ocultada (i.e. id & password)
# 주소에 아무런 정보가 표시가 되지 않는다
# 그래서 브라우저에서 보내는 방식의 기준은 get 방식이다

print(html[0:100])
# 문자열 slicing 가능가능
# 전체 문자열에서 100자만 확인 (너무 많으니까)
# 앞에 공백이 들어와있고, <!doctype html> 부터 lang="ko" class=" 까지 출력

html = requests.get(url).text.strip()   # strip 사용 후에는 앞에 공백이 사라졌다
                                        # 요청의 결과(응답, response)를 저장 -> html 문서 -> 이 문서를 html 이라는 변수에 저장했다

# 전체 link만 찾아서 출력해보기
# 1. Beautiful Soup 객체 생성
soup = BeautifulSoup(html, 'html5lib')

# 2. HTML 문서의 모든 링크에 걸려 있는 주소들을 출력
links = soup.find_all('a')
for link in links:
    print(link.get('href'))

# 전체 링크들 중에서 우리가 원하는 링크(뉴스)만 찾을 수 있을까

print('====== news links ======')

# print('====== Trial 1 =====')
# cp.news.search.daum.net
# 링크를 사용한 것들이 뉴스가 아닐까
# news_links = []
# link1 = 'cp.news.search.daum.net'
# for link in soup('a'):
#     print(link.get('herf'))
#     if link1 in soup:
#         news_links.append(link)
#         # elif link2 in soup:
#         #     news_links.append(link)
#     print(news_links)

# keep on returning empty lists

#trial 2
#
# class: 공통으로 사용되는 것일 떄
# div class = "coll content" 를 찾았다면, 다른것이 있는 것인지 고민해 봐야한다
# id: 오직 하나만 찾기위해 사용된다 (보통) ; 하지만 여러개가 들어가도 에러가 나지 않느다
# class 와 id 가 하나가 있는지, 여러개가 있는지 확인해봐야한다

# 웹 페이지로 들어가서 F12 누르고, 링크를 찾아서 리스트를 감싸고 있는 부분을 찾는다

# coll_cont
div_coll_cont = soup.find_all(class_ = "coll_cont")
# soup.find_all(attrs = {'class': 'coll_cont'})
print(len(div_coll_cont)) #4 # div_coll_cont 가 4개가 있다 # 같은 클래스 이름을 가진 HTML 요소들을 찾음
# 그렇다면, 이 div 가 몇번 째인지 찾아봐야한다
# 웹 페이지를 들어가서 f12창이 켜져있는 상태에서 ctrl + F 로해서 coll_cont 를 찾아보면 => 모든 검색창을 보여줌 (coll_cont로 묶여있는)
# 우리가 찾은 부분은 4개 중 가장 먼저나온 부분 [0]
# child 를 찾아 나가는 방법 -> HTML 하위 요소 (sub/child element)를 찾는 방법:
# 1) parent_selector > child_selector
# 바로 아래쪽에 있는 element만 찾아갈 수 있다
#           div > ul > li
#               .coll_cont > #clusterResultUL > .fst
# class 이름 앞에 . 써준다 (. 이 붙으면 class 이름, 없으면 태그 이름)
# 그리고 id 이름 앞에는 #을 붙여준다
# 그런데 depth가 너무 깊다,,, 엉엉
# 클래스 이름 > 클래스를 가지고 있는 원소 아래에 있는 id 이름 > 그 아래 자식의 아이디

# 2) ancestor_selector (조상 선택자) descendent_selector (자식 선택자):
#   공백만 놔두면 된다  => div li / 클래스 이름으로 쓰면: .coll_cont .fst (중간에 공백을 주면 됨!!!!!!!!!)
#  1) 에서는 4단계를 걸쳐 div부터 li까지 찾아갔다
#  2) 에서는 div에서 li까지 바로 내려올 수 있다
#  div li (div의 자손 요소들 중 li들)
#  .coll_cont .fst (클래스 .coll_cont 요소의 자손 요소들 중 클래스가 .fst인 요소들)
# 차일드를 찾아갈 때에는 > , 차일드의 차일드를 찾아갈 때에는 공백만 준다
# soup.select (css_selector): soup 객체에서 css선택자로 요소들을 찾는 방법
# news_link = soup.select('.coll_cont ul li a') # 여기서 멈추면 모든 a를 찾는다
#                                                           -> 그래서 뉴스 제목의 unique한 클래스 이름인 .f_link_b 을 찾아 주었다
news_link = soup.select('.coll_cont ul li a.f_link_b')
for link in news_link:
    print(link.get('href'))

# 기사 이름만 뽑을 것이냐, 연관기사 까지 뽑을 것이냐
# 기사 이름만 뽑을 것 이라면,

# 연관기사까지 뽑을 것 이라면











