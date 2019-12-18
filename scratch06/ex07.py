"""
중심 극한 정리(Central Limit Theory)
- 모집단이 어떤 분포든지 상관없이, 표본의 크기가 충분히 크다면 모든 가능한 표본 평균은 모평균 주위에서 정규 분포를 따른다
- 전체 = 모집단 = population
- 표본 = sample
- there is an average of samples, and each of them becomes variables => so average of average of samples from a population
- 표본들의 평균은 정규 분포를 따르게 된다
- 만약 모집단이 평균 mu이고, 표준편차가 sigma인 정규 분포를 따른다면, 표본 평균의 분포는 평균이 mu 이고, 분산이 sigma/sqrt(n)인 정규 분포

베르누이 확률 변수(Bernoulli random variable):
    어떤 시행의 결과가 '성공', '실패' 중 하나로 나타나고, 성공의 확률이 p, 실패할 확률이 1 - p 라고 할 때
    그 결과가 성공이면 확률 변수는 1을 갖고, 결과가 실패면 확률 변수는 0을 갖는 확률 변수 x

베르누이 확률 질량 함수(PMF: Probability Mass Function)
    pmf(x) = p
    if x = 1, 1 - p
    if x = 0
        = (p ** x)((1-p)**(1-x))

이항 확률 변수(binominal random variable):
    n 개의 독립적인 베르누이 확률 변수들을 더한 것

(비유)
베르누이 확률 변수 -> 동전 한개를 던질 때 앞면의 수 ( 1 or 0)
# 앞면이 1개 나올 확률 1/2, 앞면이 0개 나올 확률 1/2
이항 확률 변수 -> 동전 n개를 던질 때 앞면의 수
- 동전이 2개일 때 (0,1,2), 3개일때(0,1,2,3)의 변수? 생성
- n이 커지면 커질수록 정규분포에 가까워진다
- 앞면의 기댓값은 정규분포를 따른다

베르누이 확률 변수의 기댓값 (평균)
항상 평균이 p 이고, 표준 편차 = sqrt(p(1-p))

중심 극한 정리: n이 적당히 크다면, 이항 확률 변수는 대략 평균이 n * p (hereafter, np) 이고, 표준 편차가 sqrt(np(1-p)) 인 정규분포의 확률 변수와 같다
                                # 왜 np? refer to the notes (I understood it)

-> 표본(sample)의 평균(np)와 분산(np(1-p))을 알아내면,  # 분산 = squared 표준편차
    모집단(population)의 편균(p)와 분산(p(1-p))를 예측할 수 있다.
"""
import math
import random
from collections import Counter
import matplotlib.pyplot as plt

from scratch06.ex_06 import normal_cdf, normal_pdf


def bernoulli_trial(p):
    """
    베르누이 확률 변수 1 또는 0을 확률 p에 따라서 리턴
    :param p: probability
    :return:
    """
    x = random.random() # random(): 0 이상 1미만의 난수 리턴
                        # https://docs.python.org/3/library/random.html
    return 1 if x < p else 0

def binomial(n,p):
    """1이 나올 확률이 p인 베르누이 시행을 n번 했을 때,
    1이 나오는 횟수를 리턴. 이항 확률 변수를 리턴 """
    s = 0 # 1이 나오는 횟수
    for _ in range(n):
        s += bernoulli_trial(p) # 1 이면 더해줄 것이고, 0이면 더하나마나 있을 것이고,,
    return s



if __name__ == '__main__':
    # examples to see how the functions(bernoulli_trial & binomial) work
    # for _ in range(10):
        # print(bernoulli_trial(0.7), end = '')
    # trials 에 값을 1~0 , 어떤 값을 주느냐에 따라서 1와 0의 비율이 달라진다
    #     print(binomial(10,0.5), end = ' ')
        # binomial(10,0.5) 에서
        # 이상적인 경우 앞면의 갯수는 5: 하지만 6 7 4 5 4 5 3 4 6 7 # 이 값들의 평균은 5에 가깞다

    trials = 10_000
    n = 100 # 동전을 던지는 횟수? -> 동전의 갯수
    p = 0.6 # 동전 앞면이 나오는 횟수
    # data = [binomial(1,0.5) for _ in range(trials)] #binomial(1,0.5) 동전 1개일때의...
    data = [binomial(n,p) for _ in range(trials)]  #정규 분포의 표준 편차를 그려주려고
    # data = [binomial(12, 0.5) for _ in range(trials)]
    # data = [binomial(500, 0.5) for _ in range(trials)]
    # data = [binomial(10_000, 0.5) for _ in range(trials)]  # binominal의 값이 커질 수록 종모양에 가까워진다
             # binomial의 두번째 파라미터에서 값을 바꿔주면 편향된 그래프를 보여준다
    print(data[0:10])
    # plt.hist(data) # la funcion hist() se pinta el histogram sin el proceso complicado con Counter y tal
    # plt.show() # casi se muestra que la mitad esta en 0 y de la otra mitad en 1

    # 이항 확률 변수와 그에 따른 확률값을 그리기 위해서 -> 히스토 그램을 직접 그리고 바도 줌
    # pero como que queremos a tener en porcentaje
    histogram = Counter(data) # Counter class returns dictionary like: Counter({1: 5033, 0: 4967})
    print(histogram)
    x_bar = [k for k in histogram.keys()]
    y_bar = [v/trials for v in histogram.values()]
    plt.bar(x_bar, y_bar)

    # 이항 확률 변수의 정규 분포 근사 (approximation)
    # 이항 확률 변수의 분포는 n이 충분히 크면 정규 분포가 된다
    mu = n * p # 평균
    sigma = math.sqrt(n * p * (1 - p)) #표준 편차
    # 정규 분포 그래프 그리기 위해서
    x_line = range(min(data), max(data) + 1) # range는 마지막 값을 넣어주지 않아서 +1 을 한 것 # we can also write it: range(0, n+1)
    y_line = [normal_cdf(x, mu, sigma) for x in x_line] # 확률 변수에 따른 누적 확률 값
    plt.plot(x_line, y_line) # 그래프가 올라가버리는 이유는 누적 함수이기 때문에
    # 지금 실행해서 이상하게 나오는 이유는 n값이 바뀌었기 때문에, n = 4 였을 때는 좀 이쁘게 나왔는데 100 정도 되니까 얘가 너무 올라가서 그래프가 작아져버림

    # 확률 밀도를 그리고 싶다면:
    # x_line = range(min(data), max(data) + 1)
    # y_line = [normal_cdf(x + 0.5, mu, sigma) - normal_cdf(x - 0.5, mu, sigma) for x in x_line]
    # plt.plot(x_line, y_line)

    # cdf 가 아닌 pdf 함수로 밀도를 그린다면
    # x_line = range(min(data), max(data) + 1)
    # y_line = [normal_pdf(x, mu, sigma) for x in x_line]
    # plt.plot(x_line, y_line)


    plt.show()
    # y - axis : 0 이 나올 확률, 1이 나올 확률


# 누적 분포를 안다면 -> 이어붙이면 벨 모양의 그래프를 완성 시킬 수 있지!

# invoking function from previous python files incurred an error: since I did not indent the trial codes
# For some reason the trial codes did not work in ex_06 when I indented them but now they work perfectly fine (now I don't understand Python more)
# In short, the error removed after the trial codes in ex_06 got indented


