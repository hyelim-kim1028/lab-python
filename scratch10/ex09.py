from bs4 import BeautifulSoup

with open('web2.html', mode = 'r', encoding = 'UTF-8') as f:
    soup = BeautifulSoup(f, 'html5lib')
    # print(soup)

    # HTML 문서 안의 모든 div 태그를 찾음
    for div in soup.find_all('div'): #soup('div') 와 soup.find_all('div')는 동일
        print(div)
        print(div.text)

    #HTML 문서 안의 "class1" 클래스 속성을 갖는 모든 요소들을 찾음
    # attribute의 이름: class, attribute의 값은 class1 (key:value)
    # attr의 이름을 알고있을 때
    for cls_1 in soup.find_all(attrs = {'class':'class1'}):
        print(cls_1)

    for cls_1 in soup(attrs={'class':'class1'}):
        print(cls_1)
    # soup.find_all(attrs={key:value}) = soup(attrs={key:value})

    #HTML 문서 안의 "class2" 클래스 속성을 갖는 모든 요소들을 찾음
    for cls_2 in soup.find_all(class_='class2'):
        print(cls_2)

    # this is the same as
    for cls_2 in soup(class_='class2'):
        print(cls_2)
        # why class_? not class? class는 파이썬의 예약어라서 변수이름으로 쓰면 안된다
        # def, if 와 같은 논리로 파이썬의 예약어는 변수이름으로 ㄴㄴ 라서 마지막에 _를 붙여준 것

    #HTML 문서 안의 'id1' 아이디 속성을 갖는 요소를 찾음
    # attrs = dict 을 사용하거나, kwargs (keyword arguments) 를 사용해서 값을 주면 된다
    for id_1 in soup(id_='id1'):
        print(id_1)

    # 이렇게 해주는 이유는 어짜피 1개밖에 없으니까 이므니다
    # 속성은 .find를 줄여쓸 수 없다
    print(soup.find(attrs = {'id':'id1'}))
    print(soup.find(id = 'id1'))
    print(soup.find(id = 'id1').text)

    # 태그와 속성을 사용하는 방법이 다르다

    # DOM Tree 자체가 soup 이라는 객체이고, soup 이 가지고 있는 멤버 변수들 -> HTML, head, body, p, div 등등
    # soup.X 에 바로 올 수 있는 아이들을 태그이름들 (만나는 원소 1개만 리턴)
    # 하지만 속성 (태그 아래에 있는 아이들) 은 그럴 수 없기 때문에, .find 를 줄여 쓸 수 없다
    print(soup(id = 'id1')) # find all 과 같은 결과를 준다 -> 원소가 하나밖에 없어도 list로 출력
                            # list 형태로 출력
    # list 는 .text 해서 태그를 없애 줄 수 없다
    # print(soup(id =  'id1').text)
    # AttributeError: ResultSet object has no attribute 'text'.
    # HTML element가 아니고, HTML element를 가지고 있는 list 라서 그렇다!
    print(soup(id =  'id1')[0].text)
    # 이렇게하면 같은 값을 준다 -> 리스트의 원소를 하나를 선택해서 그 원소에 text()를 적용

   # find 와 find_all은 리턴하는 형식이 다르기때문에 늘 조심해야한다
   # soup.find_all(id = 'id1')[0].text
   # 이럴 때 한번에 보고 이해도가 떨어질 수도 있기 때문에, 변수에 함수이름을 저장하고 인덱스만 바꿔가며 사용도 가능하다
