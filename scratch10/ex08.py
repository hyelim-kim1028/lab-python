"""
파이썬으로 HTML 문서 분석:
설치해야할 패키지
1) beautifulsoup4  #4 = version number!
    : HTML 요소들을 분석하는 패키지
2) html5lib: HTML 문서를 parsing (분석)
# html5lib 으로 parsing -> 후에 beautifulsoup4를 이용해서 요소들을 분석
3) requests: HTTP 요청(request)을 편리하게 사용하는 패키지
# 요청을 보내고, 서버로부터 응답(response)을 받는 기능을 담당.
"""
from bs4 import BeautifulSoup

#파일을 읽기 모드로 열기
with open('web1.html', mode = 'r', encoding = 'UTF-8')as f:
    # HTML 문서를 파라미터에 전달해서 BeautifulSoup 객체 생성
    soup = BeautifulSoup(f,'html5lib')
    # print (soup) #HTML의 내용

    # HTML 요소들 중에서 h1 요소를 찾음
    h1 = soup.find('h1')
    print(h1) # find()에 tag 이름을 줘서 찾는다
    print(h1.string)

    h2 = soup.h2 #soup.태그이름 = soup.find('태그이름')
    print(h2) #se funciona!!!
    # <h2> HTML: HyperText Markup Language </h2>
    # como podemos leer sin <h2></h2>? usa la funcion 'string()'
    print(h2.string)
    print(h2.text) #text = h2의 text부분만 출력

    # paragraph 요소 안에 문자열을 찾아서 출력
    p1 = soup.find('p')
    p2 = soup.p
    print(p1)
    print(p1.text)
    print(p2)
    print(p2.text)

    # h1 & h2 에서는 사이에 다른 html element 가 들어가있지 않았다 (오직 문자열만)
    # - 그럴때에는 string 이라고하면 문자열을 읽어준다
    # p와 같은 경우에는 다른 child element 가 콘텐츠에 들어가있다 (i.e. <b>)
    # text 속성은 자식 요소(child element) 태그들을 제거하고, 텍스트만 찾아줌
    # string y text tienen las funcionas mismas

    # print(soup.find('a'))
    # print(soup.a)
    # 1개밖에 못 찾는다, 2번째 태그는 못 찾음
    # find의 동작 원리는: 위에서부터 한줄, 한줄 분석하고, 찾고자하는 것을 찾으면 멈추고 리턴 (밑에 더 있어도 처음 만나면 리턴하고 멈춤)

    #
    print(soup.find_all('a'))
    # 모든 값을 리스트로 리턴해줌
    # 나중에 인덱스로 [<a href="https://www.daum.net/">다음 카카오 </a>, <a href="https://www.daum.net"> 다음
    #         <img src="img.png" style="with: 400px;"/>
    #     </a>]
    # soup.find_all('a')[0] -> a href="https://www.daum.net/">다음 카카오 </a>,
    # 처럼 따로따로 꺼내줄 수도 있다

    #HTML 문서의 모든 링크에서 링크 주소(href)만 추출해서 출력
    for link in soup('a'):
        # HTML 요소.get('attr 이름') - attr의 값을 구함
        print(link.get('href'))



