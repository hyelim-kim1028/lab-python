#November 05, 2019
"""
tuple(튜플) : (원소)값들을 변경할 수 없는 리스트
"""
# 값들이 들어가 있으면 바꿀 수 없다
# 튜플은 대괄호를 사용하지 않고, 소괄호( )를 사용한다

numbers = (1,2,3)
print(numbers)
# 리스트와 똑같이 인덱스를 갖는다
print(numbers[0]) # index
print(numbers[0:2]) #slicing
one, two, three = numbers #decomposition
print(one,two,three)

# 리스트와의 차이점:
numbers[0] = 100
# 타입 에러 발생, 튜플 타입은 값을 변경할 수 없다
