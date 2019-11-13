# 함수(function) : 기능을 수행해서 값을 반환하는 코드 블록
# 인수(argument): 함수를 호출할 때 전달하는 값
# 매개변수(parameter): argument를 저장하기 위해서 함수를 정의할 때 선언하는 함수

print('Hello, Python!')
# 함수 안에 넘겨주는 값을 인수(argument)라고 한다
# 함수는 인수를 저장받아서 화면에 전달받은 값을 출력 (기능을 수행한다 라고 표현)

# 용어 정리:
# 기능: 함수가 하는 일
# 어떠한 변수에 저장이 되지 않는다
result = print('Hello,Python') #1개의 인수
print(result) #None 출력/ 값을 반환하지 않는 함수
print() #a function with no argument
print('hello','python','123') # function with three arguments (each argument distincted by a comma(,))

print('hello', end =',',)
print('python')
# Above two lines are printed out next to each other
# Normally, the line changes but we changed the parameter 'end' to a comma
# which means (do not change the line but simply put a comma)

#Python 내장(built-in) 함수
result = sum([1,2,3,4,5]) # ctrl + q: 문서보기 단축키
#result: 함수 sum의 리턴 값 (반환 값)
print(result)

result = abs(-5)
print(result)

result = pow(2,4) #x,y,z 의 파라미터가 있다 # 2 ** 4
print(result)

result = pow(2,4,3) # x ** y % z
print(result)

