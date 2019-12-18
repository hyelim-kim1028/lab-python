"""
확률과 분포
- 확률 변수 (random variable): 어떤 확률 분포와 연관되어 있는 변수
(예) 동전 1개를 던지는 확률 분포에서, 동전 앞면의 개수 X
      P(X=1) = 1/2 or P(X = 0) =1/2
      # 마치 함수를 쓰는 것과 같이 위처럼 할 수도 있다
      y = f(x)
          f(0) = ?
          f(1) = ?

(예2) 주사위 1개를 던지는 확률 분포에서, 주사위 눈의 개수 X
X = 1,2,3,4,5,6

기대값(expected value) /  sigma Xi P(Xi)
- 평균의 개념, 확률 변수의 확률에 확률 변수의 값을 가중 평균한 값
E(x) = sum(X_i * P(X = x_i))
     = (앞면이1 개일 때 앞면이 1개일 확률 + 앞면이 0개일 때 앞면이 0개일 확률...?) + ...
     (예) 동전 1개를 던질 때, 동전 앞면의 기댓값
     E = 앞면의 값(1) * 1/2 + 0 * 1/2 # 0 은 앞면이 하나도 없을 수도 있으니까
        = 0.5 (동전이 1개일 때 우리는 0.5 라고 기대하는게 맞다라고 하는 것)
     (예) 주사위 1개를 던질 때, 주사위 눈의 기댓값
     E = 1 * 1/6 + 2 * 1/6 .... 6 * 1/6 = 21/6 = 3.5
     -> 이산 확률 변수 (0 과 1의 변수 밖에 없는), 불연속적인 값들로 이루어진 변수를 이산확률변수라고 한다
     -> 170 ~ 171 까지,,,, 사이에는 무수히 많은 값들이 존재한다

"""

# random function produces arbitrary numbers, thus the returned values would change every time I run it
# do not expect the answers to have the same values all the times
# they had been hashtagged to show how a sample returned value would look like

# 동전 3개를 던질 때, 확률 변수를 동전의 앞면의 갯수
# X = 0,1,2,3
# 동전 3개를 10,000번 던지는 실험 -> P(X=0),P(X=1),P(X=2),P(X=3)
# -> P(X =0) = 1/8, P(X=1) = 3/8,P(X=2) = 3/8,P(X=3) = 1/8 -> refer to the notes
# Expected Value: ( 0*1 + 1*3 + 2*3 + 3*1) /8 = 1.5
# import random
#

# Initial plan -> and thougth following the previous functions that teacher made would help
# # coins = ['Head','Tail']
# # trials = 10_000
# # for X_i in range(trials):
# #     X.append(random.choice(coins))
# #     sum = sum(X_i * P(X = X_i))
# # return sum
# from collections import Counter
# so I came up with this:
# def experiment(type, n, t):
#     """
#
#     :param type: type : coin['Head','Tail']
#     :param n: number of coins (3)
#     :param t: number of trials = 10_000
#     :return: list
#     """
#     cases = []
#     for _ in range(t):
#         case = []
#         for _ in range(n):
#             rand = random.choice(type)
#             case.append(rand)
#         cases.append(tuple(case))
#     return cases
#
# coins = ['Head','Tail']
# experiment1 = experiment(coins,3,10_000)
# print('experiment1 =', experiment1)
#
# def how_many_heads(x):
#     counter = Counter[x]
#     print('counter = ', counter)
#     return counter['H']
#
# counter1 = how_many_heads(3)


# for X_i in range(trials):
#     X.append(random.choice(coins))
#     sum = sum(X_i * P(X = X_i))
# return sum


# teacher's solution
import random
from collections import Counter

experiments = [] # 동전 3개를 10,000번 던질 때, 동전 앞면의 갯수만 저장
coin = (1,0) # 1 as Head, 0 as Tail
trials = 10_000
for _ in range(trials):
    heads= 0 #동전 앞면의 갯수
    for _ in range(3): # 동전이 3개, 하나씩 3번 던집니당
        heads += random.choice(coin)
        # heads = 0 이니까, 1이 더하기 되어도 결국엔 head가 3번의 동전 던지기에서 몇번 나왔느냐가 저장된다
        # 1번 나오면 1, 2번 나오면 2, 3번 다 나오면 3이 저장되는 것 => 뭘해도 heads 의 값!
    experiments.append(heads)
print(experiments[0:10])
# [2, 1, 1, 1, 1, 3, 0, 0, 2, 2]

head_counts = Counter(experiments)
print(head_counts) #Counter({1: 3793, 2: 3702, 0: 1278, 3: 1227})

#Expected value
expected_value = 0
for x, cnt in head_counts.items():
    expected_value += x * cnt / trials
print('expected value =', expected_value)
# expected value = 1.4878

# dice -> coin(1,0) to dice(1,2,3,4,5,6) -> no need for_in range(3) ...
# we just did it

# Expected Value for Dice (주사위 눈의 기댓값)

dice = (1,2,3,4,5,6)
experiments = [random.choice(dice) for _ in range(trials)]
            # dice 에서 숫자를 하나 꺼내서 저장을 10,000번 하겠다! 라는 것
print(experiments[0:10]) #[1, 1, 3, 2, 2, 1, 4, 1, 2, 1]

head_counts = Counter(experiments)
print(head_counts)
# Counter({2: 1722, 6: 1710, 5: 1697, 3: 1641, 4: 1620, 1: 1610})
# 확률이 모두 1/6에 근접한다

expected_value = 0
for x, cnt in head_counts.items():
    expected_value += x * cnt/ trials
print('주사위 눈의 기댓값 = ', expected_value)
# 3.5033
# discrete numbers : 이산 확률 분포

# 연속 확률 분포 (ex.height)
# P(170.0 <= X <= 171.0)
# the summation of all probabilities = 1
# It's impossible to add all the continuous numbers since there is an infinity
# 그래서 생겨난 것이 적분





































