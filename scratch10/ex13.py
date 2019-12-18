# icrawler
# pip install icrawler
# i for image; image crawler
# file > settings > project interpreter > icrawler installation check!
# dev폴더에 새 폴더 'image'를 만들기
# 웹에서 이미지를 가져오는 패키지

# objective: Icrawler 패키지를 사용해서, Google 이미지 검색 결과의 이미지들을 다운로드

from icrawler.builtin import GoogleImageCrawler
import os

# 이미지 저장 경로 설정
save_dir = os.path.join('C:'+os.sep, 'dev', 'images')
# window 에서만 + os.sep, 처럼 써주고, 다른 os에서는 아니다
# Google ImageCrowler 객체 생성
google_crawler = GoogleImageCrawler(storage = {'root_dir':save_dir})

# 검색 필터링(filtering) 조건들
filters = {
    'size': 'large',
    'license': 'noncommercial,modify',  # refer the google settings
    'color':'blackandwhite'
}

# 이미지 다운로드
google_crawler.crawl(keyword = 'cat', filters = filters, max_num = 50)
# google_crawler.crawl(keyword = 'pengsu', max_num = 50)
# 네이버와 다음은 가지고 있지 않다 / 더 고민해봐야할 문제군 큼큼

# tread -> utilizing all the cores? (can be more than one) (can download more pictures faster)

# Scrapy: A package used for web-scrawling

