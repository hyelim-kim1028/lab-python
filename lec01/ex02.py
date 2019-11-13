"""
여러가지 print() methods
"""
#November 04,2019
print('Hello,python!')
# f for function (parameters)
age = 16
name = '오쌤'
print('나이:', age, '이름:', name)
# 쉼표로만 나열을 해주면 된다
# 결과에서 ',' 을 주는 것은 불가능 (age와 쉼표 사이의 공백을 주는 것은 불가능)
# 아예 중간에 print('나이:', age, ', 이름:', name) 이렇게 주지 않는 이상

#formatted string
print(f'나이: {age}, 이름: {name}')
# {변수 이름} 중괄호 안에 들어가 있는 변수 이름

# Another way of making a formatted string:
print('나이: {}, 이름: {}'.format(age,name))
# {} we have not yet decided which variable to come, like a place holder

print('나이:%d, 이름:%s' % (age, name))
# 첫번째 % 자리에 첫번째 변수가, 두번째 % 자리에 두번째 변수가 들어간다
# %d = 정수 (d for digit), %f = 실수 (f for float), %s = 문자열 (s for string)
# why do we call a 실수 a float? floating point
# the points or decimal points are folating,,, that is why it's called as a float (dude)

"""
사용자 입력(키보드 입력) 처리 
"""

print('>>> 이름을 입력하세요:')
name = input()
print(f'name: {name}')
# 입력을 받으려고 대기중이라 계속 돌고 있고, 이름을 입력해야 이제 process finished 라고 뜸

age = input('>>> 나이를 입력하세요: ')
age = input()
print(f'age: {age}')
# 줄바꿈이 안되는 상태로 위에서 입력이 되서 아래로 프린트; 아래로 내려가거나 커서가 움직이지 않아요
# 키보드로 입력하는 것은 모두 다 문자열, 고로, age = 문자열
print(age + 1) # print(age + 1) # Error (Type error)

# ctrl + / 는 주석 토글 (주석이 없으면 만들어주고, 있으면 없애준다)
