import numpy as np
import random
from math import sqrt

# 빈 리스트 선언
scores = []

# 난수(0 <= x <= 100) 10개를 리스트에 저장
# for i in range(10):
#     print(i,np.random.randint(low = 0, high = 101))

random.seed(30)
for i in range(10):
    scores.append(np.random.randint(low = 0, high = 101))
print(scores)

# we can put an underscore (_) in place of i
# for _ in range(10):

# This is also possible:
# for i in range(10):
#     x = np.random.randint(0,101)
#     scores.append(x)
# print(scores)

# underscore in grey means 파이썬에서 권장하는 코드 작성법에서 조금 벗어난다 (에러는 아니다)

# x = np.random.randint(1,101)
# scores[0] = x
# 로 하면 인덱스가 애초에 없었기 때문에 에러가 발생한다
# 이 때, append() 를 사용해서 이어 붙여준다/ 넣어준다

# 리스트에 저장된 시험 점수 10개의 총점을 계산
sum2 = 0
for i in range(10):
    sum2 = sum2 + scores[i]
print(sum2)

#How teacher did it:

total = 0
for score in scores:
    total += score
print(f'총점 = {total}')
# total = 0 이 없으면 에러가 난다: total 이 없는 상태 (+= 는 왼쪽값과 오른쪽 값을 더해주는데 처음에 왼쪽값이 없는고야,,, 이럴수가)

#함수사용
print(f'총점2 = {sum(scores)}')
# 무엇 왜 난 안됨

#리스트에 저장된 시험 점수 10개의 평균을 계산
n = 10
average = sum2/n
print(average)

#also:
avg = total / len(scores)
print(f'평균 = {avg}')
print('평균2 = ',np.mean(scores))

# import statistics
# x = statistics.mean(scores)
# print("Mean is :", x)

#표준편차

# for i in range(10):
#     sd = sqrt((scores[i]-average)**2)
# print(sd)

sum_of_squares = 0
for score in scores:
    sum_of_squares += (score - avg) **2
    standard_deviation = sqrt(sum_of_squares/len(scores))
print(f'표준편차 = {standard_deviation}')
print(f'표준편차2 = {np.std(scores)}')
# 1) 시그마 xi - mean(x) squared (sum of saures )
# 2) 1) 의 평균을 루트 씌우는 것 까지

#최댓값
max = scores[0]
for i in range(10):
    if scores[i] > max:
        max = scores[i]
print(max)

# for i in range(10):
#     if int(scores[i]) > int(scores[0+i]):
#         max_val = int(scores[i])
# print(max_val)
# 나의 실수: scores[i]와 [0+i]를 비교하면 순서의 비교가 되어버림, 그래서 계속 이 코드는 가장 마지막에 있는 아이를 return 해 준것

# what teacher did (min y max juntos):
min_score = scores[0]
max_score = scores[0]
for score in scores:
    if score > max_score:
        max_score = score
    if score < min_score:
        min_score = score
print(f'min {min_score}, max {max_score}')

# 최솟값
min = scores[0]
for i in range(10):
    if scores[i] < min:
        min = scores[i]
print(min)

# Using functions
# max = max(scores)
# print("Max: ", max)
#
# min = min(scores)
# print("Min: ", min)

# 가장 작은/큰 숫자 2개를 select > then we have to order the numbers and we can easily pick these numbers using index
sorted_scores = sorted(scores)
print(sorted_scores)
print(scores)
# sorted 를 사용할 수 없는 경우도 있다.
# 원래 배열에서 몇번 째인지 알 수 없게 된다 (오리지널 인덱스가 사라져버린다)
# 하지만 원본 배열말고 새로운 리스트를 만들 경우, 오리지널 인덱스는 원본 배열에 저장 되어 있다

