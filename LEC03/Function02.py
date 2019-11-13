"""
함수 정의/선언 (define)
def 함수이름(파라미터 선언, ...) :  #important to put a colon here, and indent the next line(s)
    함수의 기능 작성
    [return value] #This is an option, if there is no return value means there is none
"""


#함수 정의(선언)
def say_hello(): # empty parenthesis: 값을 아무것도 안 받겠다 라는 의미, 하지만 cannot skip it
    """
    '안녕하세요'를 출력하는 함수
    :return: None
    """
    # 함수 아래에 대고 """""" 주석을 주었더니 함수를 설명하는 칸이 생성되었다
    print('안녕하세요')
# no returned value, because we 'made' it but did not 'invoke' it

#함수는 호출해주지 않으면 실행되지 않음
say_hello()

def print_msg(msg):
    """
    문자열 argument / 인수 msg를 화면에 출력하는 함수
    :param msg: Message to be printed (출력할 메시지) (str type)
    :return: None
    """
    print(msg)

print_msg('hello')

# Python 은 데이터 타입을 구분하지 않기 때문에 str 타입이라고 명시를 해도 넘버나 다른 타입을 줘도 출력하는데 문제는 없다
# 이건 호출하는 사람이 결정할 문제

# return 값이 있는 함수 만들어보기
# 두 숫자의 합을 갖는 함수

def add(x ,y):  #함수의 헤더 (이름과 파라미터를 선언해주는 부분)
    """

    숫자 2개를 전달 받아서 그 숫자들의 합을 리턴하는 함수

    :param x:  int
    :param y: int
    :return: x + y를 리턴(int)
    """
    return x + y

result = add(10, 20)
print(f'add result = {result}')

# 함수는 만드는 목적은 반복적인 코드 혹은 기능을 미리 만들어 두어서 코드를 재사용하기 위한 목적

# 리턴값을 두개 갖는 함수

def sum_and_product(x, y):
    """
    두 수 x 와 y의 합(summation)과 곱(product)을 리턴하는 함수

    :param x: int
    :param y: int
    :return: x + y, x * y 순서로 리턴
    """
    return x + y, x * y

result = sum_and_product(10,20)
print(f'summation and product result = {result}')
print(result, result[0], result[1])

sum, product = sum_and_product(11,22)
print(f'sum = {sum}, product = {product}')

# name:age를 변수로 갖는 dict 타입 함수 만들기
def make_person(name,age):
    """
    이름(name), 나이(age)를 전달 받아서 dict 타입을 return 하는 함수
    :param name: name (str)
    :param age: age (int)
    :return: {'name': name, 'age':age}
    """
    return {'name': name, 'age':age}

person = make_person('오쌤', 16)
print(person)

