# dictionary comprehension

numbers = [1,2,3,4,5]
names = ['a','b','c','d','e']
# 두개의 리스트를 매핑 시킬 수 있고, 두 리스트의 크기는 다르면 안된다
# 이 두 리스트를 가지고 dictionary 를 생성한다

students = {} #create an empty dictionary
for i in range(5): #you can also write len(numbers) or len(names) en lugar de 5 => range(leng(names))
    students[numbers[i]] = names[i]
print(students)
# in dictionary we call key not an index, therefore there is no such thing as index range error
# if there is no key value, the program arbitrarily makes one

#dictionary comprehension을 이용해서
students2 = {numbers[i]:names[i]
             for i in range(len(numbers))}
print(students2)

num_name = zip(numbers, names) #zip = 묶어버리겠다ㅏㅏㅏ
print(num_name)
for x in num_name:
    print(x)
# 반복문 안에 zip obj 을 넣으면 list 에서 똑같은 인덱스에 있는 아이들을 꺼내서 튜플을 생성해줌
# 그래서 아래와 같이 해줘도 같은 결과를 준다
for x in zip(numbers, names):
    print(x)

Student3 = {}
for key,value in zip(numbers,names):
    Student3[key] = value
print(Student3)

# decomposition = 성분들의 분해
students4 = {k: v for k, v in zip(numbers, names)}
print(students4)
# key 와 value의 쌍들을 zip 이라는 곳에 튜플로 저장

# if문 써보기
students5 = {k:v
             for k,v in zip(numbers,names)
             if k % 2}
print(students5)

# students5 = {k:v
#              for k,v in zip(numbers,names)
#              if k % 2} #이 코드는 k % 2 == 1 원래 True라서 생략이 가능하지만 , 짝수를 찾을 때는 k % 2 == 0 은 == 0을 스킵 불가능
# 숫자 0 은 False 취급하고, 그 외의 나머지는 T 취급하는 성질을 이용할 것
# 그래서 k%2 만 해도 홀수를 구해준다 (굳이 k % 2 == 1 이라고 해주지 않아도 됨)

# tuple comprehension 은 없다: 변경이 불가능한 아이라서 없음
