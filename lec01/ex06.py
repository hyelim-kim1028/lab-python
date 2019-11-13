#November 05, 2019
"""
문자열 (str) 타입
"""
u = '''
안녕하세요 
Python
'''
# 큰 따옴표, 작은 따옴표 모두 사용가능 하고, 주석과는 다르다

d = """
안녕하세요, 
Python 
"""

"""
이건 주석입니다, 하지만 위에 아이는 문자열 입니다 
"""

t = """
    def my_function(x: int) -> int: 
        return x + 1
"""
print(t)
# 큰/작은 따옴표 3개를 사용한 문자열의 경우 내가 문자열을 만든 그대로 출력 (공백과 indentation 모두 그대로)
# Be coherent with the use of symbols
# 여러 줄의 문자열을 한번에 쓰고 싶을 때 사용하는 방법

q = '''    네칸을 띄고 쓰면 줄 바꿈없이 사용가능해요 
'''

c = '''\
    back slash 를 사용하면 줄 바꿈없이 사용 가능해요 22 
'''

print(q)

# 원래는 문자열 중간에서 줄바꿈을 넣으려면 \n 이라는 특수기호를 사용해야 했다
s = '안녕하세요\nPython'
print(s)

st = '\thello\n\tpython'
print(st)
# \t = tab, \n 줄 바꿈 (n for new line)
# 그래서 파이썬에서 """ 혹은 ''' 을 제공해서 이런 과정들을 더 쉽게 만들었다

# 문자열의 인덱스, 슬라이싱 (자르기)
# 파이썬의 모든 문자열은 인덱스를 가지고 있다 (sequence of character: 문자열)
# hello
o = 'hello'
print(o[0])
print(o[1])
# print(o[5])
# print(o[5]) # Index error 발생
# finished with exit code 1: IndexError: string index out of range
# Hello has up to index 4, (0 to 4), thus, index 5 refers to a string longer than expected

#slicing
# x:y - from x(포함, include) to y (미포함, exclude)
print(o[0:2])
# sale h y e
print(o[1:5])
# no hay el error porq el comment se dice a excluye #5 > okie
print(o[1:])
# 범위 연산자에서 끝 인덱스가 없는 경우는 배열의 끝까지
# 1부터 문자열의 끝까지
print(o[:3])
# 0,1,2 번의 값을 리턴해준다
# 범위 연산자에서 시작 인덱스가 없는 경우는 문자열의 시작(0) 부터 지정하는 번호까지

print(o[-3:-1])
#음수 인덱스는 뒤에서부터 시작해서 붙여나가는 것