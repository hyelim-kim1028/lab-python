"""
scratch06\ex_01
확률
- 사건 공간 (universe of events) - union of event1 and event2 (전체 집합)
- 사건 (event) : 동전을 던졌을 때 앞면이 나온다(event 1), 뒷면이 나온다(event 2)  (전체 집합의 부분 집합)
- 확률 (probability) (부분 집합이 몇개가 있을 수 있는가)
"""

import random
# Both numpy and original python have 'random' package
# here we are invoking the random package from original Python
from collections import Counter

# 사고 실험
# coin = ['H','T']
# print(random.choice(coin))
# dice = [1,2,3,4,5,6]
# print(random.choice(dice))

# 동전 한개를 10,000번 던지는 실험
# 앞면이 나올 확률과 뒷면이 나올 확률이 1/2 임을 증명하라

# what I did
# coin = ['H','T']
# coins = []
# for c in range(10001):
#     coins.append(random.choice(coin))
# print(coins)
#
# count = Counter(coins)
# print(count) # Counter({'H': 5022, 'T': 4979})
#
# what teacher did:
coin = ['H','T']
trials = 10_000 # We counting numbers we use ',' to make them easier to read, but in Python we use '_'
heads, tails = 0,0 #앞면과 뒷면이 나오는 회수를 저장할 변수
for _ in range(trials): #10,000번 반복
    random_coin = random.choice(coin) #동전 던진 결과(앞 또는 뒤)
                                         # 앞면의 개수와 뒷면의 개수를 증가 시킨다 -> 그래서 0부터 시작해서 저장
    if random_coin == 'H':
        heads += 1
    else:
        tails += 1
p_h = heads/trials #앞면이 나올 확률을 계산 = 앞면 횟수/ 전체 횟수
p_t = tails/trials #뒷면이 나올 확률을 계산
print('P(H) =',p_h)
print('P(T) =',p_t)

# 동전 2개를 던지는 실험 10000한 후,
# 1. 앞면(H)의 개수가 1개일 확률 2. 첫번째 동전이 앞면일 확률 3.앞면의 개수가 적어도 1개일 확률

#1
# what I did # why it became an infinite-loop? # no, it was a loop of 10, 000 * 10,000, so there were just too many numbers to calcuate
# coin = ['H','T']
# trials = 10_000
# both_h, both_t, one_each = 0,0,0
# result = []
# for _ in range(trials):
#     random_coin = random.choice(coin)
#     random_coin2 = random.choice(coin)
#     randomness = (random_coin, random_coin2)
#     result.append(randomness)
#     if random_coin == 'HH':
#              both_h += 1
#     elif random_coin == 'TT':
#             both_t += 1
#     else:
#             one_each += 1
# p_oe = one_each/trials
# print('P(O) = ', p_oe)

# 2nd thought:
# coin = ['H','T']
# coins = []
# coins2 = []
# both, tail, one_each = 0,0,0
# for c in range(10001):
#     coins.append(random.choice(coin))
#     coins2.append(random.choice(coin))
# count = Counter(coins)
# count2 = Counter(coins2)
# print(count,count2)
# for i,j in zip(coins,coins2)


# 여기서 그러면 어떻게 꺼내오지
#     if coins == 'H' and coins2 == 'H':
#         both += 1
#     elif coins == 'T' and coins2 == "T":
#         tail += 1
#     else:
#         one_each += 1
# p_oh = (both + one_each) / (trials * 2)
# print('P(OH) =', p_oh)
# p_atleast = both/(trials * 2)
# print('P(atleast) =', p_atleast)
# this code actually returned both, tail, one_each = 0, 0, 10001
# the reason why I thought it was returning a correct answer for number 1 was that I gave trials * 2 in its denominator
# shooked

# print(f'count = {count}, count2 = {count2}') # Counter({'H': 5022, 'T': 4979})
# # 앞면의 개수가 1개일 확률
# print('1 = ', (5030 + 5006)/(trials * 2))
# # 첫번째 동전이 앞면일 확률
# print('2 =', 5068 / (trials * 2))

# print(coins)
# print(coins2)



# hint from the class mate - run the for loops separately - have result1 = [], result2 = []
# coin = ['H','T']
# trials = 10_000
# both_h, both_t, one_each = 0,0,0
# result1 = []
# result2 = []
# for _ in range(trials):
#     random_coin = random.choice(coin)


# 2

# if 'H_' :
# __ += 1
# p_fh = first_head/trials

# 3
# if H: +=1 , else: T +=1

# teacher's solution
def experiment(type, n,t):
    """

    :param type: 실험 타입(동전 던지기 or 주사위 던지기)
    :param n: 동전/주사위의 개수
    :param t: 실험 회수
    :return: 리스트
    """
    cases = []  # 동전 던지기 실험 결과를 저장
    for _ in range(t): #실험 회수만큼 반복
        case = [] # 각 실험의 결과를 저장할 리스트
        for _ in range(n): #동전 개수만큼 반복
            rand = random.choice(type)
            # type i.e. coin = ['H','T'], dice = [1,2,3,4,5,6]
            case.append(rand) #1회 실험 결과에 저장
        # case 를 cases 에 넣어주면 -> 사건 공간이 된다
        #1회 실험이 끝날 때마다 각 결과를 tuple로 변환 후 저장
        cases.append(tuple(case)) #처음부터 튜플로 해주면 추가가 안대여,,, 그래서 비어있는 튜플로 시작할 수 없다,,, 됴르륵 튜플
        # Counter 클래스는 tuple의 갯수는 셀 수 있지만, list 는 몇개인지 셀 수 없다! 그래서 convert to Tuple (joderrrrrrr)
        # dictionary는 key와 value 모두 변경이 가능해서 셀 수 없다 (NO se puede contar: dictionary & list, se puede contar: tuple)
    return cases # 모든 결과가 다 나온다

coin = ['H','T']
coin_exp = experiment(coin, 2, 10_000)
# len(coin_exp) = 10,000
print('coin_exp[0:10]',coin_exp[0:10]) # 첫 10개의 실험 결과 확인


# 동전 던지기 실험 경우의 수
# coin_event_counts = Counter(coin_exp)
# 이 경우는 카운터를 사용할 수 없다 (unhashable type: 'list') => [[],[],[]] 이렇게 생겼던 coin_exp...
# hash => 정렬하는 알고리즘 (오/내림차순 할때)
# 리스트는 정렬할 수 없는 녀석 (리스트는 그 안의 원소들이 바뀔 수 있기 때문에) -> 원소가 바뀌면 순서가 바뀌는데 어떻게 정렬을 해 뺴애애애액
# 튜플 -> 원소가 고정이 되면 바뀌지 않는다 -> 이 녀석이라면 정렬을 해줄 수 있겠군,,, 믿음이가 후후
# hasable - 정렬이 가능한 (so unhashable type means something that can be ordered)

# Despues de cambiar a tuple, se puede contar
coin_event_counts = Counter(coin_exp)
print('coin event counts =',coin_event_counts)
# coin event counts = Counter({('H', 'H'): 2536, ('H', 'T'): 2525, ('T', 'T'): 2495, ('T', 'H'): 2444})
# pero ahora solo tenemos dos coins(ES), podemos decir que tiene algo, pero cuando tengamos mas elementos, seria dificil.
# Entonces, hacemos otra funcion a buscar un elemento en tupe i.e. para que en el tuple de (H,T), (H,H), (T,H), que hay un H?


# only for coins
def how_many_heads(x):
    counter = Counter(x)
    print('counter = ', counter)
    return counter['H'] # In the dictionary, what is value of the key 'H'?
# if we give x = (T,T) -> {T,T} -> no value such as 'H', then it would return NONE

# counter =  Counter({'H': 1, 'T': 1})
# counter =  Counter({'T': 2})
# counter =  Counter({'T': 1, 'H': 1})
# counter =  Counter({'H': 2})

# num_of_cases = 0
# for ev, cnt in coin_event_counts.items(): #dict 에서 값 찾듯이,,,
#     # coin event counts = Counter({('H', 'H'): 2536, ('H', 'T'): 2525, ('T', 'T'): 2495, ('T', 'H'): 2444})
#     # esta en la forma del diccionario
#     if how_many_heads(ev) == 1: # H 가 1 경우
#         # we gave event i.e. ('T', 'T') to the function <how_many_heads> and the tuple turns into a dictionary
#         num_of_cases += cnt  # 위의 경우를 더해준다
# p_h1 = num_of_cases/trials
# print('P(앞면이 1개일 확률) =',p_h1)

# 2
# the same the code above, but some twist (since the order becomes important)
# we are looking for HT,HH (where H comes in the first place)
# num_of_cases = 0
# for ev, cnt in coin_event_counts.items():
    # if ev == ('H','H') or ev == ('H','T'):
#     if ev[0] == 'H': #ev에서 첫번째 동전이 앞면일 확률!  # los dos se pueden usar
#         num_of_cases += cnt
# p_first_h = num_of_cases/trials
# print('P(Where H comes en el primer lugar) =',p_first_h)

#3
num_of_cases = 0
for ev, cnt in coin_event_counts.items(): # will return key and value
    if how_many_heads(ev) == 1 or how_many_heads(ev) ==2:
    # 혹은 앞면이 0개인것을 찾아서 1 - (앞면이 0개인 것) => 이런 사건을 여사건이라고 부른다
    # if how_many_heads(ev) == None:
        num_of_cases += cnt
p_h2 = num_of_cases/trials
#p_h2 = 1- (num_of_cases/trials)
print('P(at_least_1H) =',p_h2)

# 3-2 여사건 이용
num_of_cases = 0
for ev, cnt in coin_event_counts.items():
    # 혹은 앞면이 0개인것을 찾아서 1 - (앞면이 0개인 것) => 이런 사건을 여사건이라고 부른다
    if how_many_heads(ev) == 0:
        num_of_cases += cnt
# p_h3 = 1- (num_of_cases/trials)
# print('P(at_least_1H_2) =',p_h3)
# or
p_h3 = num_of_cases/trials
print('P(at_least_1H) = ', 1 - p_h3)

# 순서가 중요한 2번째가 아닌, 1번과 3번과 같은 문제를 다룰 때에는 문자가 아니라 숫자(0,1) 로 다루는게 훨씬 편하다
# 0,1을 확률? 만 계산하면 되니까
# 이렇게도 만들어보기!
# 위의 방법은 순서까지 고려할 수 있다 *0*!

# 간단히 선생님이 보여주심,,,ㅎ-ㅎ;;;

# 약속: H = 1, T = 0 -> coin[1,0] 이 됨 (H & T 아니고 0&1 이다)
coin2 = [1,0]
exp2 = experiment(coin2, 2, 10_000)
print(exp2[0:5])
# ex.[(1, 1), (1, 1), (1, 0), (0, 1), (1, 1)]

# 순서는 모르는 코드
coin2 = [1,0]
cases = []
for _ in range(trials):
    num_of_heads = 0
    for _ in range(2): #동전 갯수 # 앞면의 갯수: 0,1,2
        if 1 == random.choice(coin2): #1 = 'H' ; 앞면의 갯수만 세겠다 (1이 앞면) -> 앞면이야 카운트 늘려줄꺼다,,,1최고최고 만만세
            num_of_heads += 1 # TT = 0, HT,TH = 1, HH = 2 일테니,,, 여기서는 더해주는 1 (숫자 1)
    cases.append(num_of_heads)
print(cases[0:10])
coin_event_counts = Counter(cases)
print('P(H=0) =', coin_event_counts[0]/trials,coin_event_counts[0])
print('P(H=1) =', coin_event_counts[1]/trials,coin_event_counts[1])
print('P(H=2) =', coin_event_counts[2]/trials,coin_event_counts[2])


# coin2 = [1,0]
# cases = []
# for _ in range(trials):
#     num_of_heads = 0
#     for _ in range(2): #동전 갯수 # 앞면의 갯수: 0,1,2
#             num_of_heads += random.choice(coin2) #if 를 없애고, 1과 0으로 해서 더해주기
#     cases.append(num_of_heads)


# 주사위 2개를 던졌을 때, 두 눈의 합이 8일 확률
# 주사위 2개를 던졌을 때, 적어도 하나가 짝수가 나올 확률

dice = [1,2,3,4,5,6]
dice_exp = experiment(dice, 2, 10_000)
print(dice_exp[0:10])
dice_event_counts = Counter(dice_exp)
print('len = ',len(dice_event_counts)) # 36
print(dice_event_counts)

# teacher's solution

num_of_cases = 0
for ev, cnt in dice_event_counts.items():
    if ev[0] + ev[1] == 8:
        # if sum(ev) == 8: (sum(iterable type) -> iterable type = dict, list, tuple
         num_of_cases += cnt
print('P(8) =', num_of_cases/trials)

num_of_cases = 0
for ev, cnt in dice_event_counts.items():
    if ev[0] % 2 == 0 or ev[1] % 2 == 0:
         num_of_cases += cnt
print('P(even) =', num_of_cases/trials)


# my trials
# 두 수의 합이 8
# cases = []
# num_of_cases = 0
# for ev, cnt in dice_event_counts.items():
#     if ev == (4,4) or ev == (2,6) or ev ==  (6,2) or ev == (3,5) or ev == (5,3): # sum of elements in ev = 8
#     #     ev == in ((4,4), (2,6), (6,2), (3,5),(5,3)) # invalide syntax
#       # if sum(ev) == 8: # 두 아이들의 합,,, 을 해주고 싶었어
#          num_of_cases += 1
#     cases.append(num_of_cases)
#
# print('P(8) =', num_of_cases/trials)



# 주사위 2개를 던졌을 때, 적어도 하나가 짝수가 나올 확률
# if n % 2: # 이걸 사용해서 짝수를 define 하고 구하고 싶다!!

# dice = [1,2,3,4,5,6]
# cases = []
# for _ in range(trials):
#     num_of_odds = 0
#     for i in range(2): #주사위의 갯수
#         if dice[i] % 2:
#             num_of_odds += random.choice(dice)
#     cases.append(num_of_odds)
# print(num_of_odds[0:10])
# coin_event_counts = Counter(cases)
# print('P(even)) = ',1 - (num_of_odds/trials))

