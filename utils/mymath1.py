"""
mymath1.py
# math 패키지를 흉내내보자!
"""
pi = 3.14  #math.pi 흉내내기~^^*

# 간단한 함수 만들기
def add(x: int, y: int) -> int:
    """
    두 정수  x 와 y가 주어졌을 때, x + y 을 리턴하는 함수
    Function returns the sum of  x + y when two integers x and y are given
    :param x: 정수 (integer/int)
    :param y: 정수 (integer/int)
    :return: x + y
    """
    return x + y

def subtract(x: int, y: int) -> int:
    """
    두 정수 x 와 y가 주어졌을 때, x - y 를 리턴하는 함수
    Function returns the subtract of x - y when two integers x and y are given
    :param x: 정수 (integer/int)
    :param y: 정수 (integer/int)
    :return: x - y
    """
    return x - y

# print(__name__) # dos '_'
#                 # se vuelva '__main__'
# print('pi = ', pi)
# print('add =', add(1,2))
# print('subtract=', subtract(1,2))

# 파이참은 콘솔창에서 python.exe 이라는 파이썬 프로그램을 사용해서 저장되어있는 파일들을 위에서 아래로 해석하면서 실행시켜준 것

if __name__ == '__main__':
    print(__name__)
    print('pi = ', pi)
    print('add =', add(1, 2))
    print('subtract=', subtract(1, 2))
# 이렇게하면 메인에서는 출력이 되고, 아니면 출력이 되지 않는다
# 이런식으로 모듈을 직접 만든다면 이런식으로 해주면 된다

# my problem was that they appeared in other modules even though I had lines of code to block them
# How did I solve them: 위의 코드 (lines 28 -32)를 주석처리해주어야한다!
# if 구문이 아니라, 주석처리가 안된 아이들이 salieron en otros paginas



