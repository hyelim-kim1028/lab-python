"""
연속 확률 분포 (uniform distribution)
1) 확률 밀도 함수 (probability density function, pdf)
- 특정 확률 변수 구간을 적분한 값(확률 밀도 아래 area/면적)으로 확률을 계산할 수 있는 함수
  P(a <= x < b) # 확률 변수 구간 -> 떨어지는 값으로 계산할 수 없어서, 구간을 잡아서 여기 사이에 있는 값이다 라고 밖에 얘기를 못 할 때
  곡선 아래의 (적분, y = f(x)) 의 면적이 우리가 구하고 싶은 확률이 된다
  P(a <= x < b) = Integral from a to b [pdf(x)dx]

2) 누적 분포 함수 (cumulative distribution function, cdf)
- 확률 변수의 값이 특정 값보다 작거나 같을 확률을 나타내는 함수
cdf(x) = P(x <= b)
P(a <= x < b) = P(x < b) - P(x <= a)
# 0 ~ 1     1보다 작을 확률 - 0 보다 작을 확률
# 0 ~ 0.1    0.1 에서 작을 확률 - 0 보다 작을 확률
# 0 ~ 0.01  0.01 에서 작을 확률 - 0보다 작을 확률
# 사각형에서의 가로 길이를 줄이는 중
# pdf(x)dx = F(x)
"""
import matplotlib.pyplot as plt

def uniform_pdf(x):
    """
    uniform distribution(균등 분포) 확률 밀도 함수

    :param x:
    :return:
    """
    return 1 if 0 <= x < 1 else 0


def uniform_cdf(x):
    """
    균등 분포 누적 분포 함수
    :param x:
    :return:
    """
    if x < 0: # x 가 0보다 작을 때
        return 0
    elif 0 <= x <1: # x 가 0보다 크거나 같고, 1보다 작을 때
        return x
    else:  # x 가 1보다 클 때
        return 1


import math
SQRT_TWO_PI = math.sqrt(2 * math.pi)
# SQRT as square root

# 정규 분포(normal distribution)
def normal_pdf(x, mu = 0.0, sigma = 1.0):
    """
    # the value in parenthesis() is a default value
    평균이 mu(0) 이고, 표준편차가 sigma(1)인 정규분포
    확률 밀도 함수
    :param x:
    :param mu:
    :param sigma:
    :return:
    """
    return math.exp(-(x - mu) ** 2/ (2 * sigma ** 2))/(SQRT_TWO_PI * sigma)
    # formula for the normal distribution, please refer to the notes how the formula looks like

def normal_cdf(x, mu = 0.0, sigma = 1.0):
    """
    평균이 mu이고, 표준편차가 sigma인 정규 분포의 누적 분포 함수 (cumulative distribution function)
    math.erf() function (error function) 을 이용해서 구현
    :param x:
    :param mu:
    :param sigma:
    :return:
    """
    return (1 + math.erf((x-mu)/(math.sqrt(2) * sigma))) /2

def inverse_normal_cdf(p, mu = 0.0, sigma = 1.0, tolerance = 0.00001):
    """
    누적 확률 p를 알고 있을 때 정규 분포 확률 변수 x =?
    표준 정규 분포가 아니라면 표준 정규 분포로 변화 (표준 정규 분표란 표준 = 0, 시그마 = 0)
    :param p:
    :param mu:
    :param sigma:
    :return:
    """
    if mu != 0.0 or sigma != 1.0: # 표준정규분포가 아닐 때
        return mu + sigma * inverse_normal_cdf(p, tolerance= tolerance)
        # 재귀함수를 사용하는 중 # 굳이 이렇게 쓸 필요가 없다고 하셨다,,, 난 이게 재귀함수인지도 모르겠다
    # tolerance -> 실수가 오차가 있는데, 어디까지 허용할 것인가에 대한 값
    low_z, low_p = -10.0, 0 # random numbers were given / 누적확률이 0이되는 값이 얼마인가? (영원히 0과 만나지 않는다) => -10에서 0에 근접 라는 값을 준 것
    high_z, high_p = 10.0, 1.0 # 10에서 1.0에 근접이다
    while high_z - low_z > tolerance: # we will narrow down the range of high/low_z
        mid_z = (low_z + high_z) / 2.0
        mid_p = normal_cdf(mid_z) # 중간 값에서의 누적 확률
        if mid_p < p: #이 누적 확률이 우리가 찾으려고하는 확률 (p) 보다 작을 때
            low_z = mid_z
        else:
            high_z = mid_z #구간을 줄여나가기를 반복해서 찾고자 하는 확률(p)의 근사값을 구한다
    return mid_z # 표준정규분포일때의 리턴

# 정렬알고리즘 중 binary search 라고 하는 알고리즘이 있다 (이진정렬 알고리즘)


if __name__ == '__main__':
    # -2 <= x <= 2 까지의 구간을 0.1씩 나눔
    xs = [x/ 10 for x in range(-20, 21)]
    print(xs) # [-2.0, -1.9, -1.8, -1.7, -1.6, -1.5, -1.4, -1.3, -1.2, -1.1, -1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
    ys = [uniform_pdf(x) for x in xs]
    print(ys) # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # do not indent the
    plt.plot(xs, ys)
    plt.title('Uniform Distribution PDF')
    plt.show()

    ys2 = [uniform_cdf(x) for x in xs]
    plt.plot(xs,ys2)
    plt.title('Uniform distribution CDF')
    plt.show()

    # cdf
    # x의 값이 얼마 이하인 값을 모두 더한 값


    # x 의 범위를 늘려보자
    xs = [x/10 for x in range(-50,51)] # changing the +- value would result in conversion of x-axis
    # mu = 0, sigma = 1
    ys1 = [normal_pdf(x) for x in xs]
    # normal_pdf 를 만족하는 x들


    # mu = 0.0, sigma = 2.0
    ys2 = [normal_pdf(x, sigma = 2.0) for x in xs] # 표준편차 늘려보기

    # mu = 0.0, sigma = 0.5
    ys3 = [normal_pdf(x, sigma = 0.5) for x in xs]

    # mu = -1.0, sigma = 1.0
    ys4 = [normal_pdf(x, mu = -1.0) for x in xs]

    plt.plot(xs, ys1,'-', label = 'mu = 0, sigma = 1')
    plt.plot(xs, ys2,'--', label = 'mu = 0, sigma = 2')
    # higher the sigma, lower the height, wider the graph (면적이 넒어진다, 그래서 전체 area를 맞추기 위해서 height 가 낮아진 것)
    plt.plot(xs, ys3, ':', label = 'mu = 0, sigma = 0.5')
    # lower the sigma, higher the height, narrower the graph( 동일한 면적을 줘야한는데 폭이 좁아지니까 높이가 높아진다)
    plt.plot(xs, ys4, '-.', label = 'mu = -1.0, sigma1')
    # 기준이 x = 0에서 x = -1 로 옮겨감
    plt.legend()

    plt.title('Normal Distribution PDF (sigma 0.5 & 1.0 & 2.0)')
    plt.show()

    # mu (좌우), sigma (밀도? 몰려있는 정도?) 를 adjust 할 수 있다


    # mu = 0, sigma = 1 인 CDF
    ys1 = [normal_cdf(x) for x in xs]
    # mu = 0, sigma =2 CDF
    ys2 = [normal_cdf(x, sigma = 2) for x in xs]
    # mu = 0, sigma = 0.5
    ys3 = [normal_cdf(x, sigma = 0.5) for x in xs]
    # mu = -1, sigma = 1
    ys4 = [normal_cdf(x, mu = -1) for x in xs]


    plt.plot(xs,ys1,'-', label = 'mu =0, sigma =1')
    plt.plot(xs, ys2, '--', label = 'mu = 0, sigma = 2')
    # 편차가 늘어나니까, 확률이 늘어나는 속도가 완만하다 (PDF에서 산포도가 늘어나면 곡선이 완만해지는 것과 같은 것)
    plt.plot(xs, ys3, '.', label = 'mu = 0, sigma = 0.5')
    # 갑자기 훅하고 늘어난다 (거의 0으로 변함이 없다가, 확률들이 누적되기 시작함, 짦은 시간안에 1에 도달함) -> 데이터가 몰려있다
    plt.plot(xs,ys4, '-.', label = 'mu = -1, sigma = 1')
    # ys1 과 같은 모양을 갖지만, mu = -1 이므로, 왼쪽으로 -1 만큼 옮겨간 그래프를 보여준다

    plt.legend()
    plt.title('Normal Distribution CDF')
    plt.show()

    # 위의 그래프에서는 확률 변수의 값을 알고 있을 때, 누적 확률의 값을 알 수 있다
    # 하지만 만약에 우리가 확률을 알고 있을 때 확률 변수의 값을 알고싶다면?
    # 역함수 (refer to the notes)

    # inverse_normal cdf 를 사용해서 누적확률이 0.9, 0.99, 0.999 인 확률 변수 x를 찾아보고, 표준 정규 분포표와 비교해보기
    x1 = inverse_normal_cdf(0.9)
    print('x1 =', x1)
    x2 = inverse_normal_cdf(0.99)
    print('x2 =', x2)
    x3 = inverse_normal_cdf(0.999)
    print('x3 =', x3)
    # 또 return 을 안줘서 안나옴 ^0^ 제발 좀 잘 하자, 실수도 실력이다 혜림아ㅏㅏㅏㅏ!!!!!!!!!















































