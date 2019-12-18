"""
what is overloading
"""

def test():
    print('test')

def test(param = 0):
    print(
        'test param =', param
    )

test() #얜 누구를 호출할까?
# 파이썬에서는 이름이 같은 두 함수를 만들 수 없다, 마지막에 온 아이가 전에 온 아이들을 모두 덮어써버린다
# C## 이나 java 와 같은 경우에 같은 이름으로 다른 파라미터를 가진 아이들을 만들 수 있다
# overload 과적하다

#overloading:
# 함수(메소드)의 파라미터가 다른 경우
# 같은 이름으로 여러개의 함수(메소드)를 정의하는 것
# 파이썬은 overloading 을 제공하지 않습니다

