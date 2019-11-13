"""
명시적 형 변환 (casting): int(),float(),str()


"""

# print("3.1" + 1.2)
# ERROR: exit code 1 (비정상적인 종료) - can only concatenate str (not "float") to str
# type error : it does not convert the data type automatically
# 그래서 우리는 명시적 데이터 타입 변환을 해서 계산을 해주어야한다

# We can solve the error if "3.1" is not a str but a float
# 숫자 타입으로 변환 후 산술 연산을 실행
print(float('3.1') + 1.2)
# returns 4.3

print('3.1'+str(1.2))
# 1.2 를 문자열 취급해서 그냥 3.1 과 1.2 를 이어붙여줬다
# 문자열 + 문자열: concatenate (문자열 이어 붙이기)
# 입력받는 모든 아이들을 (숫자포함) 문자이다. 하지만 예를 들어 계산기를 만들려고 하는데 입력 받는 값은 모두 > 문자 (읭)

#간단한 계산기

x = input('>>> 숫자(x) 입력')
y = input('>>>숫자(y) 입력')
print(x+y)
# x = 5,  y= 5 를 입력했더니 5 5 가 답으로 나옴
# 이유: 숫자가 아닌 문자열로 받아드려서 그럼

# input: 키보드로 입력을 받을 때 사용하는 함수 > 문자열로만 받아드린다
# 파일에 저장된 문자들을 받아올 때도 마찬가지로 숫자도 모두 문자열로 취급한다

x = float(x) #문자열을 실수로 변환 # x = 숫자(실수)
y = float(y) #문자열을 실수로 변환
# is the same as: y = float('>>>숫자(y) 입력')
print(x + y)
# 이렇게 하면 x + y 의 값이 10 으로 나온다
print(f'{x} + {y} = {x + y}')
# formatted string 은 중괄호 안에서 연산이 가능하다

y = float(input('>>>숫자(y) 입력'))
x = float(input('>>>숫자(x) 입력'))
print(f'{x} + {y} = {x + y}')


print(f'{x} - {y} = {x-y}')
print(f'{x} - {y} = {x-y}')
print(f'{x} - {y} = {x-y}')
print(f'{x} - {y} = {x-y}')
# ctrl + d : 커서가 있는 줄을 복사 & 붙여넣기

print(f'{x} / {y} = {x/y}')
print(f'{x} * {y} = {x * y}')

# 변수와 연산자에 대해 공부해 보았다


