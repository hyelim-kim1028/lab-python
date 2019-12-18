"""
November 26, 2019
가설(Hypothesis) 와 통계 추론 (Inference)
- 가설을 세우고, 통계적으로 테스트 해보겠다
- 어떤 경우에는 우리가 세운 가설을 받아드리고, 어떤 경우에는 받아드리지 않는가에 대한 것을 알아본다
- 가설을 세우고, 가설을 정정하는 과정

- 귀무 가설 (영가설, null hypothesis), H0
- 숫자가 없는 것이 Null인 상태 (Null = 영가설)
- 대립가설 (alternative hypothesis), H1

(예)
H0: 동전을 던졌을 때 앞면이 나올 확률 p = 1/2
H1: 동전을 던졌을 때 앞면이 나올 확률은 p != 1/2
(H0 와 H1 contrary to each other)

- 증명하고 싶은 사실을 가설로 세우고, 그 반대되는 가설을 만드는것
- 증명하는 방법은 H0 가 맞다 라고 하거나, H1이 틀리다 라는 것을 증명하면 된다 #양측검정

(예)
H0: 동전을 던졌을 때 앞면이 나올 확률은 p > 1/2
H1: 동전을 던졌을 때 앞면이 나올 확률은 p <= 1/2  #단측검정

- 가설을 채택하지 않는 것: 가설을 기각한다
- 가설을 채택하는 것: 가설을 채택한다 or 가설을 기각하지 않는다
- for the table, refer to the notes
- 가설을 기각하는 기준이 되는 것: 유의수준
- muy parecido al cross table of machine learning

제 1종 오류 (type I error) : 실제는 가설이 참인데, 가설을 기각하는 오류 (a = 유의수준) # a for alpha
제 2종 오류 (type II error) : 실제는 가설이 거짓인데, 가설을 기각하지 않는 오류
유의수준 (significance level): 제 1종 오류가 발생할 확률의 최대 허용 한계
                            (i.e. alpha = 0.05%(5%), 0.01%(1%), ...) # 틀릴 수 있는 한계
                            유의 수준에 따라서 가설을 기각할 것인지, 아닌지를 결정
검정력 (Statistical power) : 1 - beta # 귀무가설의 잘못을 찾아낼 확률
 - Beta: 가설이 거짓인데 기각하지 못하는 확률
# beta : 귀무가설이 거짓이될 확률 (검정력이란 베타의 반대로써: 1 - beta = 귀무가설이 참일 확률?)
"""
import math
from scratch06.ex_06 import normal_cdf, inverse_normal_cdf


def normal_approximation_to_binomial(n,p):
    """
    이항분포(n,p)를 정규 분포로 근사했을 때 평균, 표준편차

    :param n: 실행 횟수
    :param p: 성공확률
    :return:
    """
    mu = n * p
    sigma = math.sqrt(n * p * (1 - p))
    return mu, sigma

# 확률 변수가 어떤 구간 안(밖)에 존재할 확률
# P(X < b), P(X > a), P(a < X < b) 이런 값을 계산해보겠다
# 누적분포함수를 이용한다
# 어떤 값보다 작을 확률 CDF, 어떤 값보다 클 확률 1 - CDF
# scratch06에서 작성했던 normal_cdf 함수를 이용

#P(X <= high): 확률 변수 값이 특정 값보다 작을 확률 = cdf(high)
normal_probability_below = normal_cdf # 함수 이름
# 어떤 특정값보다 낮다

#P(X > low): 확률 변수 값이 특정값보다 클 확률 = 1 - P(X < low)
def normal_probability_above(low, mu = 0.0, sigma = 1.0):
    return 1 - normal_cdf(low, mu, sigma)

# P(low < X < high) : 확률 변수 값이 특정 범위 안에 있을 확률
# = P(X < high) - P(X<low)
def normal_probability_between(low,high,mu,sigma):
    return normal_cdf(high, mu, sigma) - \
        normal_cdf(low,mu,sigma)
        # aunque lo escribimos todos en una linea no pasa nada! pero cunado hagan en el otro, deben poner \

# P(X < Low or X > high): 확률 변수가 특정 범위 밖에 있을 확률 (low < high)
# 어떤 값보다 작거나, 어떤 값보다 큰 경우
# 1 - P(low < x < high)

def normal_probability_outside(low, high, mu, sigma):
    return 1 - normal_probability_between(low, high, mu, sigma)
    # 확률 변수가 결정이 되면, 어떤 값이 어떤 범위에 있다, 없다 > 확률들을 리턴해주는 함수
    # 그래서 누적 분포 함수사용

#확률이 주어졌을 때, 그 반대를 찾는 역함수 (the other side)

# 확률이 주어졌을 때, 상한 (upper bound) 또는 하한(lower bound) 또는 범위(lower ~ upper bound) 를 찾는 함수들
# 확률이 주어졌을 때, X값을 찾는 함수들

# P(X < x) = prob이 주어졌을 때, 상한 x를 찾는 함수
def normal_upper_bound(prob, mu, sigma):
    return inverse_normal_cdf(prob, mu, sigma)

# P(X > x) = prob이 주어졌을 때, 하한 x를 찾는 함수
# P(X < lb) = 1 - prob이 주어졌을 때, 상한 lb를 찾는 함수
def normal_lower_bound(prob, mu, sigma):
    """ prob - 클 확률"""
    return inverse_normal_cdf(1-prob,mu, sigma )

# hereafter lower bound as lb and upper bound as ub

# 95% 가 가운데에 들어가게끔하고 싶다
# P(lb < X < ub) = prob이 주어졌을 때, 평균을 중심으로 대칭이 되는 구간의 상한(ub)과 하한(lb)를 찾는 함수

def normal_two_sided_bounds(prob, mu, sigma):
    """
    prob = 경계안에 들어가는 확률, 그래서 우리는 양쪽 끝(tail)에 해당하는 확률을 먼저 구해야한다
    가정: 평균을 중심으로 대칭되는 구간을 찾겠다
    """
    # 양쪽 끝에 해당하는 확률
    tail_prob = (1 - prob)/2

    # 찾으려는 상한 (upper bound) 는 확률 tail prob 이상을 갖는 하한을 찾으면 됨
    # P(X > a) = tail_prob을 만족하는 하한 a를 찾으면 됨
    upper_bound = normal_lower_bound(tail_prob, mu, sigma)
    # 또는 P(X < b) = prob + tail_prob을 만족하는 상한 b을 찾으면 됨
    upper_bound = normal_upper_bound(prob + tail_prob, mu, sigma)

    # 찾으려는 하한(lower bound)는
    # 확률 tail_prob 이하를 갖는 상한을 찾으면 됨
    # P(X < b) = tail_prob 을 만족하는 상한 b를 찾으면 됨
    lower_bound = normal_upper_bound(tail_prob, mu, sigma)

    return lower_bound, upper_bound

def two_sided_p_value(x, mu = 0, sigma =1):
    """양측 검정에서 사용하는 p-value"""
    if x >= mu:
        return normal_probability_above(x, mu, sigma) * 2
    else:
        return normal_probability_below(x, mu, sigma) * 2

def estimate_parameters(N, n):
    """
    N번 실행하는 실험을 통해서 모집단을 추정해보자
    표본 (샘플)의 평균으로 모집단의 평균, 표준편차 추정
    :param N:
    :param n:
    :return:
    """
    p = n/N
    sigma = math.sqrt(p * (1-p)/N)
    return p, sigma

def a_b_test_statistic(N_a, n_a, N_b, n_b):
    """ return value signifies 표준 정규분포에서 p-value를 찾기 위한 / 계산할 수 있는 z값  """
    p_a, sigma_a = estimate_parameters(N_a, n_a)
    p_b, sigma_b = estimate_parameters(N_b, n_b)
    # a for experiment a & b for experiment b in A/B test
    # N_a = 1000, n_a = 200
    # N_b = 1000, n_b = 180
    # N = number of trial, n = number of clicks
    return(p_b - p_a)/math.sqrt(sigma_a**2 + sigma_b**2)
                            # z-value (표준변수) that will be used when calculating p-value



if __name__ == '__main__':
    # 동전을 던졌을 때 앞면이 나올 확률은 1/2(=0.5) testing(검정)
    # 동전을 1,000번 던지는 실험 - 이항 분포
    # 앞면이 나오는 기댓값 - 정규분포(np, sqrt(np(1-p))

    # 영가설(귀무가설)
    # H0: p = 1/2
    # 영가설이 참이라는 가정 아래에서, 정규 분포로 근사하기 위해서
    # 동전 앞면이 나오는 확률의 평균과 표준 편차는
    mu, sigma = normal_approximation_to_binomial(1000, 0.5)
    # 동전을 1000번 던져보고, 앞면이 나올 확률이 1/2 이다, 그리고 대략적으로 mu과 sigma 가 어떻게 될것인지에 대한 근사값을 알아보는
    # 당연히 평균은 500이라는 숫자가 나와야한다 (천번 돌렸으니까).
    # 이런 분포는 정규분포를 따른 다는 것을 알기 때문에... 앞면이 나오는 횟수의 기댓값 (결국은 그것이 앞면이 나올 확률)
    # 평균과 표준분표를 알아야 정규분포값을 알 수 있기때문에 처음에 찾아준 것이다

    # reiteration of what we had discussed ayer
    # H0: 동전의 앞면이 나올 확률 1/2 (p = 1/2)
    # H1: 동전의 앞면이 나올 확률은 1/2이 아니다 (p != 1/2)
    # 검증에서 H0 이 참이여도 증명이 되지만, 이게 안된다면, H1이 거짓이라는것을 밝힐 수도 있다
    # 거짓임에도 받아드리는 것 (Beta)/ 거짓이니까 받아드리지 않겠다 (검정력)
    # 유의수준(alpha): 영가설이 참인데 가설을 기각할 가능성 (i.e. 95%)
    # beta: 영가설이 거짓인데 가설을 기각하지 않을 가능성 -> 거짓임에도 거짓이라고 하지 못한, 실수할 확률 (i.e. 0.05/ 5%)
    # 검증력(Statistical Power) = 1 - beta => 크면 클수록, 거짓인 것을 기각을 잘 하는 모델 이다

    # H1: 동전의 앞면이 나올 확률은 1/2이 아니다 (p != 1/2)
    # 어떤경우를 1/2이 아니라고할까 499 도 1/2 이 아니고, 501도 아니고,... 양쪽에 걸쳐서 아니라고하는 것
    # 확률이 1/2 보다 크다, 1/2보다 작다, 두개의 합집합이라고 해도 됨,,, 다 됨 으엉엉

    # 1/2 이라고 가정을 했을때, 5%을 제외하고 찾은 lb & ub
    # low, high = normal_two_sided_bounds(0.95, mu, sigma)
    #    print(f'low= {low}, high={high}')  # (469, 531)
    # 만약, 동전 앞면이 나올 확률이 1/2이 아니라고 가정하면 어떻게 기각 또는 채택을 할것인가?
    # 1/2이 아닌 확률을 계산할 수는 없다 (우리가 계산할 수 있는 것은 확률변수의 값이 어떤 값보다 작거나, 크거나, 사이에 있는 것은 계산할 수 있지만, 아니라는것은 계산할 수 없다)
    # 동전 앞면이 나올 확률을 0.5 보다 크다고 가정한다 (여기서는 0.55) , 평균과 표준편차를 찾아보자

    mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)
    # n은 계속 1000번이였기 때문에 비교를 위해 일치시켜주었다
    print(f'p = 0.5 가정: mu_0 = {mu}, sigma_0 = {sigma}')
    print(f'p=0.55 가정: mu_1 = {mu_1}, sigma_1 = {sigma_1}') # 1/2이 아니라고해서 0.55 라고 가정을 해보았다
    # p = 0.5 라는 가정에서 95% 구간이, p = 0.55 라는 가정에서 나올 확률

    # 동전 앞면의 확률 p = 0.45 라고 가정
    mu_2, sigma_2 = normal_approximation_to_binomial(1000, 0.45)
    print(f'p = 0.45 가정: mu_2 = {mu_2}, sigma_2 = {sigma_2}')


    # 유의 수준 5%: #의미가 있는 수준  # 틀린 결과를 낼 수 있는 확률을 0.05 (이정도 틀리는건 감수하겠다)
    # H0이 참이지만 기각을 하는 오류를 5%는 감수
    # H0를 기각하지 않을 확률 95%의 상한과 하한을 찾음
    low, high = normal_two_sided_bounds(0.95, mu, sigma)
    print(f'low= {low}, high={high}')  # (469, 531)
    # low= 469.01026640487555, high=530.9897335951244 과 비슷한 한줄 출력하는 프로그램 *0*!
    # 동전을 n번 던지는 실험을 하면, 동전 앞면이 나오는 횟수가 얼만지는 모르겠고, 정규 분포에서 0.95% 범위안에 들어가야한다
    # low = 469 보다 크고 high = 530 작은 값 (동전 던지는 실험을 해서 470번이나 531번이 나오면, 그 값을 가지고서 이 동전은 앞면이 나올 확률이 1/2 이라고 95%는 말할 수 있다)
    # in (469,531) 있으면 유의수준 95%를 만족한다

    beta = normal_probability_between(low,high, mu_1, sigma_1)
    # p = 0.55라는 가정이 맞았다고 할 오류
    print('beta =', beta)
    power = 1 - beta
    # p = 0.55 라는 가정이 틀렸다고 검증할 수 있는 능력
    print('power =', power) # 틀린 가정을 맞았다라고 생각할 확률이 0.11, 틀린 가정을 틀렸다라고 할 확률 = 0.88

    # mu_2, sigma_2 의 beta & power
    beta = normal_probability_between(low, high, mu_2, sigma_2)
    print('beta =', beta)
    power = 1 - beta
    print('power =', power)

    # mu_1, sigma_1 일 때와 mu_2, sigma_2 일 때의 beta, statistical power 값이 같다.
    # beta = 0.11345199870463285, power = 0.8865480012953671
    # 즉, 귀무가설(H1) 이 거짓이라고 밝히는 검증력이 0.88 이라는 모델. P != 1/2 라고 가정했을 떄,
    # 특정범위 안에 두면, 크나 작으나 같은 검증력을 갖는다.

    # Pensamos en otra manera: 단측 검정 (한쪽만 보겠다) -> one-sided test
    # H0: p <= 0.5
    # H1: p > 0.5
    # 그러면 H1에 대한 검증력이 높아진다
    # p = 0.5 일 때 유의수준(5%)의 upper bound 구간

    high = normal_upper_bound(0.95, mu, sigma)
                # 우리가 유의수준은 5%로 줬기 때문에 p = 0.95
    print('유의 수준 5% 상한 =', high) #526
    beta = normal_probability_below(high, mu_1, sigma_1)
    # beta: 526보다 적을 확률
    print('단측 검정 beta =', beta) # 0.06362051966928262
    power = 1 - beta
    print('단측 검정 검정력 =', power) #0.9363794803307174

    print('================')

    # H0: p >= 0.5
    # H1: p < 0.5 (i.e. p = 0.45)
    lower = normal_lower_bound(0.95, mu, sigma)
    # 우리가 유의수준은 5%로 줬기 때문에 p = 0.95
    print('유의 수준 5% 상한 =', lower)  # 526
    beta = normal_probability_above(lower, mu_2, sigma_2)
    print('단측 검정 beta =', beta)
    power = 1 - beta
    print('단측 검정 검정력 =', power)

    # P-value
    # 우연히 나왔다 -> 가설을 기각해도 된다 -> 우연히 나온 확률이 얼마인가? 그걸 우리는 P-value 라고 부른다
    # H0이 참이라고 가정할 때, 실험에서 관측된 값보다 더 극단적인 값이 관측될 확률
    # 530 보다 더 많이 나올 확률을 계산해서 그 값은 유의수준과 비교
    # p-value (극단적인 값이 나올 확률)이 유의 수준(5%)보다 작다면 그 값은 우연히 발생한 값이라고 생각할 수 있을 것이다 -> H0 기각함
    #  (유의수준이라고 설정한 값보다 더 작다면, 굉장히 희귀하게 나타나는 것 (1000번중에 3번도 안나오는 값이라면) -> 그 값은 우연히 발생한 값이라고 생각할 수 있다)
    # P - value 가 유의 수준보다 크다면 그 값은 우연히 발생한 값이라고 말할 수 없다 -> H0을 기각하지 않음
    # 동전을 1000번 던지는 실험에서 동전의 앞면이 530번 나왔다.

    # 귀무가설 H0: p = 0.5, H1: p != 0.5
    # p_value = normal_probability_above(530, mu, sigma)
    p_value = two_sided_p_value(530, mu, sigma)
    # 0.057 > 0.05 p-value가 유의수준보다 크다
    # -> 530은 우리들의 유의수준에 들어올 값이 맞지만, 0.057보다 크니까 우연히 발생했다고 생각할 수 없으니 기각할 수 없다
    print(f'p_value = {p_value}')

    # H0: P <= 0.5, H1: p > 0.5
    print(normal_upper_bound(0.95, mu, sigma))

    # 동전을 1000번 던져서 앞면지 525번 발생
    # 앞면의 확률 p = 525/1000 = 0.525 -> 이 동전이 정상적인 동전인가 비정상적인 동전인가
    # p -value 를 계산해서

    p_bar = 525/1000
    # 어떤 정규분포를 따라가는지 모른다. 정규분포를 알려면 진짜 평균과 표준편차를 알아야한다 (진짜 -> 전체모집단의)
                                                        # (Mu, sqrt(np(1-p)) )
    # 지금은 we do not know the Mu & std of the graph
    mu = p_bar # replace mu with p_bar (모집단의 평균을 실험값으로 대체)
    # 표본의 표준편차로 모집단의 표준 편차를 추정
    sigma = math.sqrt(p_bar * (1 - p_bar)/1000) # 1000 number of trials
    # mu는 표본의 평균으로 모집단의 평균을 대체, sigma도 표본의 표준 편차로 모집단의 표준 편차를 대체
    bounds = normal_two_sided_bounds(0.95, mu, sigma) # 모집단 추정?
    print(f'bounds = {bounds}') # 0.4940490278129096, 0.5559509721870904
    # 0.5 라고 하는 값은 in between bounds
    # 실험을 통해서 찾은 95% 신뢰구간
    # In other words, 예측한 값이 아니라 진짜 P-value, 즉, 진짜로 앞면이 나올 진짜 확률은 위 구간에 포함된다고 95% 확신할 수 있다
    # we can be 95% confident that the P-value of H0 (the probability of head that would appear when we toss the coin) lies between 0.49 and 0.55 (?)
    # 신뢰구간을 찾아 주었다 한다면, 신뢰구간을 보고서 우리가 가설로 세운 값이 어떠한 구간안에 들어가는 정도를 X% 확신할 수 있다

    # 동전 1000번 던졌을 때, 540번 앞면이 나옴
    p_bar = 540/1000 # 표본 평균
    mu = p_bar # 모집단의 평균
    sigma = math.sqrt(p_bar * (1 - p_bar)/1000) # 모집단 표준 편차
    bounds = normal_two_sided_bounds(0.95, mu, sigma)
    print(f'bounds of 540 = {bounds}') # 0.5091095927295919, 0.5708904072704082
    # p = 0.5 인 가설은 신뢰 구간에 포함을 못 함.
    # lies in 신뢰할 수 없는 구간 (the numbers go beyond 0.5)
    # 0.5라고 확실할 수 없는 도전
    # 신뢰구간: 확률의 확률? 신뢰구간이란 신뢰할만한 구간의 확률을 말해주는?
    # 추정된 모집단에서 0.95가 어디있느냐
    #  p = 0.5인 가설은 신뢰 구간에 포함되지 못함

    #A/B 테스트: 똑같은 두가지 (디테일만 조금 바꾼?)를 두고 테스트
    # N_a = 1000, n_a = 200, N_b = 1000, n_b = 180 (150)
    # we will give n_b two values (180 & 150) and we will compare their differences
    z1 = a_b_test_statistic(1000,200,1000,180)
    print(f'z1 = {z1}') # - 1.14
    # 부호는 크게 중요하지 않다
    p_value_1 = two_sided_p_value(z1)
    print(f'p_value_1 = {p_value_1}') #0.254
    # p-value 0.05보다 크다 (p-value > 0.05) # 0을 기준으로
    # A 와 B 의 차이 (Function statistics_a_b(algo asi) returned the difference between b and a)
    # 가 우연히 발생할 확률이 유의 수준보다 높다
    # In other words, A와 B가 차이가 있다고 말할 수 없다 (차이가 없다)
    # 유의 수준이 적은 경우에만 받아드리겠다? (what is 유의수준 ? is it tolerance or significance)
    z2 = a_b_test_statistic(1000, 200, 1000, 150)
    print(f'z2 = {z2}')  # -2.94
    p_value_2 = two_sided_p_value(z2)
    print(f'p_value_2 = {p_value_2}') # 0.003
    # p-val < 0.05
    # -> A와 B의 차이가 우연히 발생할 확률이 유의 수준보다 낮다
    # -> A와 B의 차이가 있다고 말할 수 있다
    # -> A와 B의 차이가 있다는 가설을 채택
