"""
scipy 패키지의 stats 모듈에서 제공하는 확률 밀도 함수 (PDF: Probability Density Function),
누적 분포 함수(CDF: Cumulative Distribution Function)
scipy: https://www.scipy.org/ 
"""

import scipy.stats as stats
import matplotlib.pyplot as plt


xs = [x/10 for x in range(-30, 31)]
# -3 과 3사이의 0.1 씩 증가하는 (range가 소숫점을 짤라주지 못해서 x/10으로 해준것)
# 그래프를 그릴 x구간 (구간을 자르면 조금 더 부드러운 그래프가 나오니까!)

# 균등 분포(uniform distribution) 확률 밀도 함수 (probability distribution function)
ys1 = [stats.uniform.pdf(x) for x in xs]
 # for x in xs: x 좌표 xs 는 위에 선언한 곳에서 꺼내오면 된다
 # stats.uniform.pdf() => 확률 밀도 함수

# 균등 분포의 누적 분포 함수 (cumulative probability function)
ys2 = [stats.uniform.cdf(x) for x in xs]


plt.plot(xs, ys1, color = 'b', label = 'PDF')
plt.plot(xs, ys2, color = 'r', label = 'CDF')
plt.legend()
plt.title('Uniform Distibution PDF & CDF')
plt.show()

# 평균 = 0 이고, 표준 편차 sigma = 1 인 정규 분포(normal distribution) 확률 밀도 함수 (PDF)
ys1 = [stats.norm.pdf(x) for x in xs]
    # norm for normal distribution

# 표준 정규 분포 누적 분포 함수(CDF)
ys2 = [stats.norm.cdf(x) for x in xs]

plt.plot(xs, ys1, label = 'PDF', color = 'b')
plt.plot(xs, ys2, label = 'CDF', color = 'r')
plt.legend()
plt.title('Standard Normal Distribution PDF & CDF')
plt.show()










