"""
Python 반복문 - for statement
for 변수 in 반복 가능한 타입들 (iterable) :
    반복할 문장들
- Iterable types are: list, tuple, set, dictionary, character/string(문자열) ...
"""

# range(to): 0부터 (to -1) 범위의 숫자들을 준다
# range(from, to): desde from a (to - 1) 범위의 숫자들을 준다
# range(from, to, step): desde from a (to-1) step 만큼씩 increment 된다

for i in range(5): # 0,1,2,3,4
    print(i)

for i in range(5):
    print(i, end = ' ')
# 이렇게하면 옆으로 출력이 된다
# ' ' 이 옆에 공백을 주라는 뜻, end 의 default = 줄 바꿈 but we changed it to a space
print()

for i in range (1,5): # 1,2,3,4
    print(i, end = ' ')
print()

for i in range (1,5,2): #1 3
    print (i, end=' ')
# 1 + 2 = 3 3 + 2 = 5 하지만 5는 포함하지 않음, 그래서 1과 3만 출력
print()

# 문자열도 iterable
for s in 'Hello, Python!':
    print(s, end = ' ')
# 문자열도 인덱스가 있다, slicing 가능 = iterable 가능
print()

# Iterable list type
languages = ['PL/SQL', 'R', 'Python', 'Java']
for lang in languages:
    print(lang, end = ' ')
print()
# then, how can we put an index in front of each languages?

for i in range(4):
    print(i,languages[i])
print()
# However, there might be an error that the length of elements may change every time it's run
# So we use len() to fix the length of elements

for i in range(len(languages)):
    print(i, languages[i])

#dictionary
alphabets = {1:'a', 2:'b', 3:'c'}
print(alphabets.keys()) #dict 의 키들/key vlue 알면 value 알 수 있음
for key in alphabets.keys():
    print(key, alphabets[key])

# in dict 는 딕셔너리의 key들을 반복한다
for key in alphabets:
    print(key)

for item in alphabets.items():
    print(item)
# key와 value의 쌍을 넘겨주는: item
# 튜플 형태로 출력이 된다

# list & tuple: we can decompose them
# key, value = (1,'a')
for key, value in alphabets.items():
    print(key,value)
# 분해를 해서 바로 key & value의 값을 알 수 있다


