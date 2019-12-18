"""
url schema (how url is composed):

웹 주소(URI, URL)의 형식:
프로토콜://서버주소(:포트번호)/경로? query string

#Example 1
 https://www.youtube.com
#/http: protocol name/ s - secure
# ~.com -> server address /
# address of a some random video: https://www.youtube.com/watch?v=XjPdJEOYHfs
# wathch? 경로 -> ? 뒷쪽 => query string (사용자가 서버로 보내는 정보를 담고있다)
# v = 비디오 ID
# 우리가 서버로 보내주는 정보

Example 2
# https://m.sports.naver.com/news.nhn?oid=003&aid=0009597324
# 프로토콜//서버주소         /경로,path/ ? 후에 두 가지 정보(oid & aid)를 서버에 보낸다 oid=003&aid=0009597324
# query string 은 &로 짤라서 보면 된다 + 더 붙여줄 때에도 &로 붙여줌

# 대부분 웬사이트는 포트번호를 생략한다 (80으로 같기때문에)
# query string: browser가 server로 보내는 정보
# param 이름 = param 값 형식으로 작성
# 파라미터가 여러개일 경우에는 &로 파라미터들을 구분

# 다음에서 머신러닝으로 검색한 기사 100개의 url 주소와 기사 제목을 출력
# 다음에서 임의이 검색(키워드)로 검색한 기사 100개의 주소와 기사 제목을 출력하는 함수를 작성
"""

import requests
from bs4 import BeautifulSoup

# query string: 브라우저가 서버로 정보를 보내는 용도


# 두번째 문제:
def daum_search(keyword):
    url = 'https://search.daum.net/search?w=news&DA=PGD&spacing=0'
    # machine learning 부분 (q = 부터 ~ 이상한 글자들 ~ &DA 전까지) 지워버린다
    # 검색 결과는 1페이지부터 10페이지 까지
    for page in range(1, 11):
        print(f'=== page {page} ===')
        req_params = {'q': keyword,  #검색어(키워드)를 쿼리 스트링에 파라미터로 추가
                      'p': page # 검색 페이지 번호를 쿼리 스트링에 파라미터로 추가
                      }
        #'https://search.daum.net/search?w=news&DA=PGD&spacing=0' 뒤에 & q = blahblah & p = blah 이렇게 추가해 주겠다
        # 검색어는 함수를 호출할 때 준다, 페이지번호는 1페이지부터 10페이지까지 자동으로 증가시켜준다
        response = requests.get(url, params = req_params)
        html = response.text.strip()

        soup = BeautifulSoup(html, 'html5lib')
        news_links = soup.select('.coll_cont ul li a.f_link_b')
        # find_all 의 단점: < a class = ""> ___ </a> 까지는 찾을 수 있지만, 자식 태그는 못 찾음
        # 또한, 다른 div 의 a 태그까지 찾을 수 있는 오류성이 있기 때문에, 범위를 줄여서
        # div 를 정해서, 거기서 자식 태그들의 자식 태그를 타고 들어가다보면 우리가 원하는 태그에 찾아 들어갈 수 있다
        # 1페이지에  news_links 와 같은 링크가 10개가 있다
        for link in news_links:
            news_url = link.get('href')
            # HTML 요소가 가지고 있는 컨텐트 문자열
            news_title = link.text
            print(news_url, news_title)


# teacher's solution
if __name__ == '__main__':

    daum_search('시동')

    # METHOD A
    # url = 'https://search.daum.net/search?w=news&q=%EB%A8%B8%EC%8B%A0%20%EB%9F%AC%EB%8B%9D&DA=PGD&spacing=0&p='
    #                                             # 머신 러닝이라고 한글로 입력한 값 (UTF-8로 반환된 것)
    #                                             # w -> 파라미터 이름, = new (파라미터 값)& q = dkjfieak & spacing = 0 & p = 1
    # for page in range(1, 11):
    #     print(f' === page {page} ===')
    #     page_url = url + str(page)
    #     # str을 붙인 이유, 더하기는 같은 타입끼리만 가능하다, url 이 문자이고, page는 숫자이기 때문에 숫자를 문자로 변환해준 것
    #     # print(url)
    #     # 해당 페이지 url 주소로 get방식의 요청을 보내고, 서버에서 보낸 응답(response)을 문자열로 처리
    #     # page_url 요청보내고 응답받은 것을 텍스트화 시킴. 앞뒤 공백까지 제거
    #     html = requests.get(page_url).text.strip()
    #     # html 객체가 생겼으니 BeautifulSoup 생성
    #     soup = BeautifulSoup(html, 'html5lib')
    #     # html 분석기가 필요해서 parsor을 넣어주어야하는데, 우리가 사용한 파서: html5lib
    #     news_links = soup.select('.coll_cont ul li a.f_link_b')
    #     for link in news_links:
    #         news_url = link.get('href')
    #         news_title = link.text
    #         print(news_url, news_title)
        #     print(link.get('href'), link.text.strip())


    # METHOD B
    # if False: # 새로 만든 함수를 사용해보려고 모두 거짓으로 나오게 놔두었다
    #     url = 'https://search.daum.net/search?w=news&q=%EB%A8%B8%EC%8B%A0%20%EB%9F%AC%EB%8B%9D&DA=PGD&spacing=0'
    #     for page in range(1, 11):
    #         print(f'=== Page {page} ===')
    #
    #         # 해당 페이지 URL 주소로 Get 방식 요청 (request) 보내고,
    #         # 서버에서 보낸 응당(response)을 문자열로 처리
    #         # html = requests.get(page_url).text.strip()
    #         response = requests.get(url, params = {'p': page})
    #         # requests.get(url, params = {key:value}):
    #         # params의 내용을 url의 query srting의 파라미터로 추가해줌
    #         # url? ... &key = value
    #         html = response.text.strip()
    #
    #         # Beautiful 객체 생성
    #         soup = BeautifulSoup(html, 'html5lib')
    #         news_links = soup.select('.coll_cont ul li a.f_link_b')
    #         for link in news_links:
    #             # HTML 요소 (element)의 href속성 (attribute)값을 읽음
    #             news_url = link.get('href')
    #             # HTML 요소가 가지고 있는 컨텐트 문자열
    #             news_title = link.text
    #             print(news_url, news_title)

















