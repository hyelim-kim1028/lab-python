#November 04, 2019
# Python Data Type:

# 변수가 어떤 타입의 데이터를 저장하는가가 중요하다
# 명시하지는 않지만 미리 만들어져 있다

"""
1. 숫자 타입
2. 논리타입
3. 문자열
4. 시퀀스
5. 매핑
6. 집합
7. none
"""



# 1. 숫자 타입: int(정수/ integer), float(실수), complex(복소수)

intVal = 123
print(type(intVal))
# returns the data type
print(id(intVal))
# returns its memory address(?)

floatVal = 3.141592
print(type(floatVal))
print(id(floatVal))

complexVal = 1 + 2j
print(type(complexVal))
print(id(complexVal))
# 숫자에서 제곱해서 마이너스 1이 되는 숫자를 i 라고 표시하고, 파이써는 i 대신 j 라고 표현
# 이유는 for/if 에서 i 라고하는 변수를 많이 사용해와서 j로 대체
print(1j**2)
# ** = ^

# 변수에 값을 저장할 때에는 그냥 써주면 된다
# The lecture was to inform how Python works internally

# 논리타입: bool (T/F)
result = 10 > 2 #10은 2보다 크다
print(result)
#변수이름이 왼쪽에 오고 오른쪽에 계산식 등이 온다
# 변수에도 우선순위가 있다 (계산이 가장 마지막)

#문자열: str
name = 'abc'
print(type(name))

# Sequence type : list, tuple
# 여러개의 자료들을 저장하는 배열을 시퀀스라고 이야기하는데 두 종류, list 와 tuple 이 있다
# Mapping type : dict
# dict for dictionary (dictonary has a word: meaning which becomes like a map)
# How Python saves info like a dictionary: dict
# list, tuple, dict are very important concepts

# 집합 (set)
# None : 값이 없음을 나타내는 데이터 타입
# 데이터를 저장하는 주소가 없습니다, 데이터가 없습니다 ( none in other languages are called as NULL)

name = None
print(type(name))
#None type 이라고 뜬다






