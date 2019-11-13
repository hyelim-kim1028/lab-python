import numpy as np
# 빈 list(scores) 선언
scores = []
# 난수(0 <= x <= 100) 10개를 발생시켜서 리스트에 저장

import random
scores=[]
for i in range(10):
    scores.append(np.random.randint(low = 0, high = 101))
print(scores)


# 리스트에 저장된 시험 점수 10개의 평균을 계산해서 출력
import statistics
x = statistics.mean(scores)
print("Mean is :", x)

#리스트에 저장된 시험 점수 10개 중에서 최댓값, 최솟값을 찾아서 출력
max = max(scores)
print("Max: ", max)

min = min(scores)
print("Min: ", min)