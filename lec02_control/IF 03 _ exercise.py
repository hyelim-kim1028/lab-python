#과제 - If-else 를 활용한 간단한 가위바위보 게임 만들기
# 가위 1, 바위 2, 보 3

import numpy as np
# 어제 다운받은 numpy프로그램을 가져

print('Rock Scissors Paper Game')
print('[1] Scissors')
print('[2] Rock')
print('[3] Paper')
print('---------------')
print('Select >>')

user = int(input())
# 난수를 만들자
computer = np.random.randint(low = 1, high = 4)
print(computer)
# high를 4로 주는 이유는 4는 포함되지 않는다 (인덱스와 같은 개념. [0:2] 라는 값을 주었을 때 0,1의 값만 돌려주었던 것과 같은 논리)
# 검정색: 컴퓨터가 내는 가위바위보,,,

if user == computer:
    print('Tie!')
elif user == 1:
    if computer == 2:
        print("You lose!")
    elif computer == 3:
        print("You win!")
elif user == 2:
    if computer == 1:
        print("You won!")
    if computer == 3:
        print("You lose!")
elif user == 3:
    if computer == 1:
        print("You lose!")
    if computer == 2:
        print("You won!")
else:
    print("Invalid")

# Method 1
# 정석: 9개 다 만들기
if user == 1 and computer ==1:
    pass
elif user == 1 and computer == 2:
    pass
#이렇게 9개 만들면 됨

#Method2
if user == 1:
    if computer == 1:
        pass
    elif computer ==2:
        pass
    else:
        pass
elif user == 2:
    if computer == 1:
        pass
    elif computer ==2:
        pass
    else:
        pass
    # 등등,,,
else:
    pass

# Method 3 - the same as mine

# Method 4 - Cross Table
result = user - computer
# 비기면 result = 0,
if result == 0: #tie
    print("Tie!")
elif result == 1 or result == -2: # user win
    print("You won!")
else: #computer won
    print("You lose!")

# logic making process vary, there are millions of ways of making a logic
# programming is turning these logics into programming language
# You need to know how to convert but also to interpret these codes
# I need to be able to convert my logic into codes (First, I have to study Math)
