#list comprehension
# list 와 반복문이 합쳐져 있는 unique to Python 인 문법

numbers = [1,2,3,4,5]
print(numbers)

# 5~10 개의 리스트는 손으로 넣을 수 있지만, 100개, 1000개 혹은 그 이상의 일정한 규칙을 가지는 숫자들을 만든다고 한다면 (혹은 난수를 발생해도)
# based on our lectures so far, 아래와 같이 코드를 짤 것이다

numbers2 = []
for x in range(1,6):
    numbers2.append(x)
print(numbers2)

# list comprehension 은 for 문을 간단히 쓸 수 있게 해준다

numbers3 = [n for n in range(1,6)] #n = 우리가 추가해야할 임의의 숫자
print(numbers3)

# 2,4,6,8,10 # 리스트에 이렇게 저장하고 싶다
even = [2 * n for n in range(1,6)]
print(even)

# Method2 : 성능은 덜 좋다 (더 많은 활동을 해야함)
even2 = []
for n in range(1,11): #1~10
    if n % 2 == 0:
        even2.append(n) #1~10까지 저장됨
print(even2)

#Method3
even3 = [n for n in range(1, 11) if n % 2 == 0]
print(even3)

# 1,4,9,16,25
squares = [n **2 for n in range(1,6)]
print(squares)

# random number 10개 만들기
import numpy as np
randoms = [np.random.randint(0,101) for i in range(10)] #i는 사실 필요 없는 변수 _ underscore 사용 가능
print(randoms)

#이중 for loop & comprehension
# EX. 주사위 2개를 던졌을 떄 경우의 수
# (1,1), (1,2), (1,3) ... (6,4), (6,5), (6,6)
# 주사위의 값들을 튜플이라고 생각하기로 한다. 그러면 36개의 튜플이 생성
# 이런 튜플들을 저장하는 리스트

dice1 = [] #빈 리스트 생성
for x in range(1,7): #주사위에 숫자가 나올 수 있는 경우의 수 1부터 6까지
    for y in range(1,7):
        dice1.append((x,y)) #(x,y) tuple을 리스트에 추가
print(dice1)

dice2 = [(x,y) for x in range(1,7) for y in range(1,7)]
     # list is composed of tuples (x,y)
print(dice2)

# (1,1)
# (2,1) , (2,2)
# (3,1), (3,2), (3,3)
# ... 이런식으로 저장하려면
# (x,y) such that x >= y 의 조건을 만족하는
dice3 = []
for x in range(1,7):
    for y in range(1,7):
        if x >= y:
            dice3.append((x,y))
print(dice3)

# List comprehension format:
dice4 = [(x,y)
         for x in range(1,7)      #줄 바꿔서 사용할 수 있다
         for y in range(1,7)
         if x >= y]
print(dice4)

# 학생들의 점수
# 이 점수들은 난수로 만든다 (numpy 는 위에서 이미 import해왔기 때문에 패쓰)
# 시험점수(0~100) 10개를 가지고 있는 리스트를 난수로 생성한다
scores = [np.random.randint(0,101) for _ in range(10)]
print(scores)
# 평균보다 높은 점수들의 리스트
mean = np.mean(scores)
above_mean = []
for s in scores:
    if s > mean:
        above_mean.append(s)
print(above_mean)

# 위의 코드를 아래와 같이도 만들 수 있다
above_mean2 = [s for s in scores if s > mean]

