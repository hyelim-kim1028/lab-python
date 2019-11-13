#November 05, 2019

"""
List: 여러개의 값들을 하나의 변수에 저장하기 위한 데이터 타입
원소 (element): 리스트에 저장된 값
인덱스 (index): 리스트에 값이 저장된 위치 (번호)
리스트 원소들을 변경(추가/삭제) 가능함(mutable).
"""

numbers = [1,2,3,4,5] #list
# Elements: 5 numbers in a list (1,2,3,4,5, each of them)
# Each elements has an index ( index 0 - 1, index 1 - 2, index 3 - 4, index 4 - 5)
print(numbers[0])
# print(numbers[5])
# Error: list index out of range (there is no such thing as index 5 in this list, there is only up to 4)
# 리스트이 마지막 인덱스 = 리스트 길이 - 1
print(numbers[0:3]) #범위 연산자를 사용한 slicing 가능

#배열에 저장된 값(원소)을 변경
numbers[0] = 100
print(numbers)
# 다른 원소들은 그대로 있고, 인덱스 0 만 100 으로 바뀌었다
# 이게 안되는 원소들도 있다 > tuple

# 배열에다 원소를 추가하기 (함수 사용 ().append)
numbers.append(6)
print(numbers)

numbers.extend([7,8,9])
print(numbers)
# 기존 숫자에 반복을 해주는 것? 펼쳐주는 것

#numbers.append vs numbers.extend
# https://stackoverflow.com/questions/252703/what-is-the-difference-between-pythons-list-methods-append-and-extend
numbers.append([7,8,9])
print(numbers)
# append returns [7,8,9] as a whole, even including the brackets
# the input within a bracket is considered as one element
# extend considers the three elements as unique and added to the list as their own 7,8,9

# 원소 삭제
numbers.remove(100)
print(numbers)
# 원소의 값으로 삭제

del numbers[1] #인덱스를 사용해서 원소 삭제
print(numbers)

empty = []
# 원소가 하나도 없는 비어있는 리스트

# 파이썬 리스트는 여러가지 타입의 값들을 함께 저장할 수 있음
person = ['오쌤',16,170.5,True]
# person 이라는 리스트에 4가지 원소들이 있고 각기 다른 타입들이 있다
# 오쌤 - 스트링, 16 - 인티져, 170.5 - 플롯, 트루 - 불리언
# 언어에 따라 한가지 타입을 가져야하는 언어들도 있다 (파이썬은 비교적 자유롭다)
print(person[0], type(person[0]))
print(person[1],type(person[1]))

#list decomposition
name, age, height, marriage = person
# person에 있는 값들을 왼쪽에 각각의 원소로 분해해서 저장하겠다
print(name, age, height, marriage)

# 2 차원 리스트
# 이차원 리스트는 리스트 안에 리스트가 들어가 있는 것 (i.e. .append[7,8,9])

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
print(matrix)
# 크기가 3, 원소의 개수가 3개
print(matrix[0], type(matrix[0]))
print(matrix[0][0])
print(matrix[0][1])
print(matrix[0:1])
print(matrix[0:2])

















