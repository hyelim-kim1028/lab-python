"""
조건부 확률 (conditional probability)
P(A): 사건 A가 일어날 확률
P(B): 사건 B가 일어날 확률
P(A,B) 사건 A와 사건 B가 동시에 일어날 확률 (A와 B의 교집합 확률)
P(A|B): 사건 B가 일어났을 때, 사건 A가 일어날 (조건부) 확률
        P(A|B) = P(A,B) / P(B)
        P(B|A) = P(A,B) / P(A)
- 만약 A와 B가 독립사건이면, P(A,B) = P(A)P(B)
    P(A|B) = P(A,B) / P(B) = P(A)P(B) / P(B) = P(A)
    즉, 독립사건이란 조건부 확률의 가능성이(?) 없다는 것

# EXAMPLE:
A: 첫 = H, B = 두 동전이 모두 H =>P(B|A)
A 가 일어난 경우, B도 일어날 가능성 = 1/2
P(B|A) => 두 동전이 모두 H 인 경우, A가 성립할 가능성 = 1

# 조건부 확률 예시: 자녀가 2명이 있는 가정:
A: 첫째가 딸인 경우
B: 두 자녀가 모두 딸인 경우
C: 두 자녀 중 최소 1명이 딸인 경우
P(A): 2/4 = 1/2
P(B): 1/4
P(C) = 3/4
P(A,B) = 1/4 = P(B,A)
P(A,C) = 2/4 = 1/2 = P(C,A)
P(B|A) = 첫째가 딸인데, 두 자녀 모두 딸인 경우 = 1/2
is the same as: P(B,A) / P(A) = 0.25/0.5 = 1/2
P(C|A) = P(첫쨰가 딸 일 때, 최소 한명이 딸) = 1 -> 독립이 아니다
    = P(C,A) / P(A) = 0.5 / 0.5
P(B|C) = P(적어도 한 명이 딸 일 때, 두 자녀 모두 딸인 경우) =
       = P(B,C) / P(C) = 1/4 / 3/4
"""
import random

kid = ('boy','girl')
trials = 10_000
older_girl = 0 #첫째가 딸인 경우
both_girl = 0 #두 자녀 모두 딸인 경우
either_girl = 0 # 두 자녀 중 적어도 한명이 딸인 경우
for _ in range(trials):
    older = random.choice(kid)
    # random > alt + random > enter > select random package
    younger = random.choice(kid)
    # 한 집에 두명의 자녀가 태어났다,,,!!! ㅋㅋㅋ
    if older == 'girl':
        older_girl += 1
    if older == 'girl' and younger == 'girl':
        both_girl += 1
    if older == 'girl' or younger == 'girl':
        either_girl += 1

#횟수 세기
# 첫째가 딸일 때, 두 자녀 모두 딸일 확률
p1 = both_girl/older_girl
print('P(첫째가 딸일 때, 두 자녀 모두 딸일 확률) = ', p1)
# 적어도 한명이 딸일 때, 두 자녀 모두 딸일 확률
p2 = both_girl/either_girl
print('P(적어도 한명이 딸일 때, 두 자녀 모두 딸일 확률) =', p2)



