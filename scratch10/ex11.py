"""
# url 스키마/ url 이 어떻게 이루어져 있는지에 대해서:

웹 주소 (URI, URL)의 형식:
프로토콜://서버주소(:포트번호)/경로?쿼리스트링

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
# 다음에서 임의이 검색(키워드)로 검색한 기사 100개의 주소와 기사 제목을 출력하는 함수를 작성하고 테스트
"""

import requests
from bs4 import BeautifulSoup

# url = 'https://search.daum.net/search?w=news&q=%EB%A8%B8%EC%8B%A0%20%EB%9F%AC%EB%8B%9D&DA=PGD&spacing=0&p=1'
#
# html = requests.get(url).text.strip()
# print(html)
#
# # 전체 link만 찾아서 출력해보기
# soup = BeautifulSoup(html, 'html5lib')
#
# links = soup.find_all('a')
# for link in links:
#     print(link.get('href'))
#
# # 전체의 link 들 중 뉴스기사만 뽑아보기
# div_coll_cont = soup.find_all(class_ = 'coll_cont')
# news_link = soup.select('.coll_cont ul li a.f_link_b')
# for link in news_link:
#     print(link.get('href'))

print('===== repeat 10 times =====')

# what I did:
# 뉴스기사들 뽑는 것을 10번 반복하기
# url = 'https://search.daum.net/search?w=news&q=%EB%A8%B8%EC%8B%A0%20%EB%9F%AC%EB%8B%9D&DA=PGD&spacing=0'
# for i in range(10):
#     url += '&p=i'
#     div_coll_cont = soup.find_all(class_='coll_cont')
#     news_link = soup.select('.coll_cont ul li a.f_link_b')
#     for link in news_link:
#         print(link.get('href'))

# se sale 100 enlaces, pero no son de la repeticion

# def title():
#     news_titles = []
#     for title in news_titles:
#     news_title += soup.select('.wrap_tit mg_tit')
#     print(news_titles)
#     # .wrap_tit mg_tit



# teacher's solution

if __name__ == '__main__':
#url = 'https://search.daum.net/search?w=news&q=%EB%A8%B8%EC%8B%A0%20%EB%9F%AC%EB%8B%9D&DA=PGD&spacing=0&p=1'
                                            # 머신 러닝이라고 한글로 입력한 값 (UTF-8로 반환된 것)
                                    # w -> 파라미터 이름, = new (파라미터 값)& q = dkjfieak & spacing = 0 & p = 1
    url = 'https://search.daum.net/search?w=news&q=%EB%A8%B8%EC%8B%A0%20%EB%9F%AC%EB%8B%9D&DA=PGD&spacing=0&p='
    for page in range(1, 11):
        print(f' === page {page} ===')
        page_url = url + str(page)
                    # str을 붙인 이유, 더하기는 같은 타입끼리만 가능하다, url 이 문자이고, page는 숫자이기 때문에 숫자를 문자로 변환해준 것
        # print(url)
        # 해당 페이지 url 주소로 get방식의 요청을 보내고, 서버에서 보낸 응답(response)을 문자열로 처리
        # page_url 요청보내고 응답받은 것을 텍스트화 시킴. 앞뒤 공백까지 제거
        html = requests.get(page_url).text.strip()
        # html 객체가 생겼으니 BeautifulSoup 생성
        soup = BeautifulSoup(html, 'html5lib')
                    # html 분석기가 필요해서 parsor을 넣어주어야하는데, 우리가 사용한 파서: html5lib
        news_links = soup.select('.coll_count ul li a.f_link_b')
        for link in news_links:
            news_url = link.get('href')
            news_title = link.text
            print(news_url, news_title)

# 뭐가 틀린지 모르겠다

# if __name__ == '__main__':
#     url = 'https://search.daum.net/search?w=news&q=%EB%A8%B8%EC%8B%A0%20%EB%9F%AC%EB%8B%9D&DA=PGD&spacing=0&p='
#     for page in range(1, 11):
#         print(f'=== Page {page} ===')
#         page_url = url + str(page)
#         # print(page_url)
#
#         # 해당 페이지 URL 주소로 GET 방식 요청(request)을 보내고,
#         # 서버에서 보낸 응답(response)을 문자열로 처리
#         html = requests.get(page_url).text.strip()
#
#         # BeautifulSoup 객체 생성
#         soup = BeautifulSoup(html, 'html5lib')
#         news_links = soup.select('.coll_cont ul li a.f_link_b')
#         for link in news_links:
#             news_url = link.get('href')
#             news_title = link.text
#             print(news_url, news_title)


# teaher's solution 2

# if __name__ == '__main__':
#     url = 'https://search.daum.net/search?w=news&q=%EB%A8%B8%EC%8B%A0%20%EB%9F%AC%EB%8B%9D&DA=PGD&spacing=0&p='
#     for page in range(1, 11):
#         print(f' === page {page} ===')
#         response = requests.get(url, params = {'p': page}).text.strip() # page # 가 없는 요청 주소 (page주소는 쿼리 스트링이 파라미터로 넣어준다)
#         html = response.text.strip()
#
#         # html 객체가 생겼으니 BeautifulSoup 생성
#         soup = BeautifulSoup(html, 'html5lib')
#                     # html 분석기가 필요해서 parsor을 넣어주어야하는데, 우리가 사용한 파서: html5lib
#         news_links = soup.select('.coll_count ul li a.f_link_b')
#         for link in news_links:
#             news_url = link.get('href')
#             news_title = link.text
#             print(news_url, news_title)





















