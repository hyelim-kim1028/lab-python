#November 04. 2019

"""
연산자(operator)
- 계산을 해주는 아이
- 할당 연산자 (assignment) : =
- 산술연산 (numerical operator) : +,-,*,/ , % (정수의 나눗셈에서 나머지만), // (정수의 나눗셈에서 몫만 )
- 복합 할당 연산: +=, -=, *=, /= ...
- 논리 연산: and, or, not
- 비교 연산: >, >=, <, <=, ==, !=
- identity (타입 확인) 연산자: is, is not
"""

# Assignment
# = se significa que 오른쪽의 값을 연산자 왼쪽 변수에 저장(할당)
#This is possible:
x = 1
#Pero esto, no 1 = X

# Numerical Operator
print(2 ** 3)
#2*2*2
print(3/2) # 그냥 일반적인 나누기를 해준다
print(10//3) # 정수 나눗셈의 몫
print(10 % 3) #정수 나눗셈의 나머지
print(10/3)

#논리 연산 - and, or, not
x = 1
print('x =', x)

# 복합 할당 연산
x += 10
print('x =', x )
# print ('x =', x ) returns 11, it is the same as x = x + 10 where x above was 1
# thus, it is the same as x = 1 + 10 = 11 (simple equation, complex description)

# 등호하나는 값을 저장하기 위해 사용되기 때문에, 비교를 위해서는 등호 2개를 같이 써준다 ==, !=
# 비교 연산를 return TRUE or FALSE

print(1==2)
# FALSE
print(1!=2)
# TRUE
# returns in boolean type

x = 50
print(x>0 and x<100)
# grey underline: warning > there are ways to write the code simpler
# alt + enter 하면 힌트가 나오고 simplified version (아래) 으로 바꿔준다
print(0 < x < 100)
print(x < 0 or x > 10)

# identity 연산자 :
print(x is int)
# id()는 주소값을 나타내주고, is, is not 연산자는 id()함수의 값이 같은지 다른지 비교해주는 연산자 이다
# == 와는 다른다






