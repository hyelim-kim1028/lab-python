#SET: 집합
# 특징: 저장되는 순서가 중요하지 않고, 같은 값이 중복 저장되지 않는 데이터 타입

# 똑같은 중괄호를 사용하더라도 이건 집합이다.
# This is how dictionary was written: person = {'name': '오쌤', 'age':16, 'height':170.5}
s1 = {1,2,3,3,2,1}
print(s1)
# sale: {1,2,3} -> the repeated values are eliminated, solo sale unique values
s2 = {4,3,2}
print(s2)
# returns an ordered (저장하는 순서가 중요하지 않다)
# set은 순서가 중요하지 않고, 값이 중복되도 상관이 없다

# 여기까지 카피했다

# 집합연산: 합집합, 교집합, 차집합

print(s1 | s2) #합집합 (|) / | as or
print(s1 & s2) #교집합 (&)
print(s1 - s2) #차집합 (-)

# 집합에 원소를 추가/삭제
s1.add(100) #add(value)
print(s1)

s1.remove(3) #remove(element)
print(s1)


