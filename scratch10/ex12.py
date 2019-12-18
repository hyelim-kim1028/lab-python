"""
한겨레 신문사 페이지에서, 특정 검색어 검색 결과 50개의
1) URL 주소, 기사 제목 출력
2) URL 주소, 기사 제목, 기사 내용 출력
3) URL 주소, 기사 제목, 기사 내용을 파일에 저장

"""

# EX1
# How to apply it for different news periodicals
# http://search.hani.co.kr/Search?command=query&keyword=%EB%A8%B8%EC%8B%A0+%EB%9F%AC%EB%8B%9D&sort=d&period=all&media=news
import requests
from bs4 import BeautifulSoup
import datetime


# How I did:
# def hani_search(keyword):
#     url = 'http://search.hani.co.kr/Search?command=query&sort=d&period=all&media=news'
#     # 검색 결과는 1페이지부터 5페이지 까지
#     for page in range(5):
#         print(f'=== Page {page} ===')
#         req_params = {
#             'keyword': keyword,  # 검색어(키워드)를 쿼리 스트링에 파라미터로 추가
#             'pageseq': page  # 한계례는 0,1,2,3,4를 쓴다
#         }
#         response = requests.get(url, params=req_params)
#         html = response.text.strip()
#
#         soup = BeautifulSoup(html, 'html5lib')
#         # news_links = soup.select('.search-result-section ul li dl')
#         #  위처럼 하면 내용은 나오고, 링크는 안나옴
#         news_links = soup.select('.search-result-section ul li a')
#         # 위 처럼 하면 링크가 2번씩 출력되고 제목은 나오지만 날짜와 내용이 None 으로 출력됨
#         # news_links = soup.select('.search-result-section ul li dl a')
#
#         for link in news_links:
#             news_url = link.get('href')
#             news_title = link.text
#             news_date = link.dateto
#             # news_date = link.dd # link.dd > data None 이라고 뜸
#             news_content = link.detail # detail 을 못 읽고 None 이라고 뜬다 (detail 이 기사가 있는 곳) => 어떻게 가져올까
#             # print(news_url, news_title, news_date)
#             print(news_url, news_title,news_date, news_content)
# current code returns two repeated links and only returns its title



# What teacher did:
def hani_search(keyword):
    # url = http://search.hani.co.kr/Search?command=query&keyword=%EB%A8%B8%EC%8B%A0+%EB%9F%AC%EB%8B%9D&media=news&submedia=&sort=d&period=all&datefrom=2000.01.01&dateto=2019.12.09&pageseq=2
                                                        #keyword = 없어도된다                                  # submedia = 후에 아무 값도 없다, 지워도 된다    #datefrom ~ dateto 이 부분 없어도 된다 #pageseq없어도 된다
    url = 'http://search.hani.co.kr/Search?command=query&media=news&period=all'
    # 쿼리 스트링(query string, 질의 문자열)의 파라미터 설정
    for page in range(5): #0:4까지의 페이지를 반복한다
     req_params = {
        'keyword': keyword, #검색어
        'pageseq':page #페이지 번호
     }
     # get의 역할은 서버로 역할을 보내는 것 (request) -> 서버로 요청을 보낸 후, 응답(response)를 받는다
     response = requests.get(url, params = req_params)
    # 응답에서 html 문서를 추출
    html = response.text.strip() # strip은 문자열 앞뒤의 공백만 제거; 문자열과 문자열 사이의 공백은 안 제거
    # HTML 문서를 분석하기 위한 BeautifulSoup 객체 생성
    soup = BeautifulSoup(html, "html5lib")
    # div = search-result-section 혹은 ul = search-result-list 에서 부터 시작해도 괜찮다
    results = soup.select('ul.search-result-list li dt a')
    # 링크가 2개가 나온 이유는 이미지와 뉴스의 같은 링크가 똑같이 걸려 있어서 # dl 아래에 dt와 dd가 있고, dt -> news link;dd->사진 링크가 걸려있다
    for link in results:
        news_url = link.get('href')
        news_title = link.text
        print(news_url, news_title)
        hani_article(news_url) # 검색 결과 뉴스 링크를 새로 열기 > 검색 후 뉴스를 여는 과정

# 우리가 준 url 주소로 들어가서 기사 1개씩 오픈해주는
def hani_article(url):
    response = requests.get(url)
    html = response.text.strip()
    # print(html[:500]) -> ???
    soup = BeautifulSoup(html, 'html5lib')
    # article = soup.find('div', class_ = 'text').text.strip()
    # article = soup.select('div.article-text div.text')
    # div class = article-text 는 기사만 주기 위한 값일 경우가 높다
    # text는 사진을 포함한 밑에 있는 부분 (자식 클래스)
    # select 는 여러가지 값이 나오기 때문에 list로 출력된다. 그래서 인덱스 + text.strip() 함수를 줘서 우리가 원하는 내용만 출력한다
    article = soup.select('div.article-text div.text')[0].text.strip()
    # 신문기사의 내용 출력
    print(article)
    # 그냥 다 보여준다
    # with - as 구문을 사용해서 write - close 해주어야한다

if __name__ == '__main__':
    hani_search('머신 러닝')

    # hani_article 사용:





