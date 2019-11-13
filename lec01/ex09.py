"""
dict: key - value 의 쌍으로 이루어진 데이터들을 저장하는 사전 (dictionary) 식 데이터 타입
"""
# key - value (key 를 설명)
# dict 를 사용할 때에는 중괄호를 사용 {}

person = {'name': '오쌤', 'age':16, 'height':170.5}
print(person)
# 만든 그대로 출력
print(type(person))

#dict의 데이터 참조 - key를 사용
# print(person[0])
print(person['name'])
print(person['age'])

print(person.keys()) #DICT 의 KEY를 알아낼 때
# returns the variable names in the list
print(person.values()) # DICT 의 VALUES 를 알아낼 때
# returns the values in the list
# How about if there is more than one in the list? or is it impossible to put more than one in the list?
print(person.items()) # DICT 의 BOTH (KEY,VALUES)  를 알아낼 때

students = {1:'강다혜', 2:'김수인', 3:'김영광, 10: 안도연'}
# key: numbers, values: string (names)
print(students[1])

#dict 에 값을 추가
students[4] = '김재성'
print(students)
# 1,2,3,4 순서대로 출력되지 않고, 마지막에 넣은 값이 마지막에 들어간다

#dict에 값을 변경
students[4] = 'gildong'
print(students)

#dict에 값을 삭제
students.pop(4)
print(students)

book = {
    'title': 'Python Programming Textbook',
    'Authors': ['Jennifer','Paul','Jason'], #여러명의 저장 -> list format
    'Publisher': 'Gilbut',
    'isbn':97911
}
print(book)
print(book['title'])
print(book['Authors'])
print(book['Authors'][0])
