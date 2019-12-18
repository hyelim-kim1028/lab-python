import math
import matplotlib.pyplot as plt
import numpy as np

def odds(p):
    return p/(1-p)

def log_odds(p):
    """ odds에 log를 취한 값"""
    return math.log(odds(p))
# log odds = log(p/(1-p))

def sigmoid(t):
    """logistic: log_odds(odds에 log를 취한 값)을 알고 있을 때, 성공 확률 p값을 계산"""
    return 1/ (1 + math.exp(-t))    # 1/ (1 + e^-t)
    # p = 0~ 1사이의 값 (0이면 분자가 0이 되서 안되고, 1이면 분모가 0이 되서 infinit value)


if __name__ == '__main__':
    p = 0.8
    print(f'p = {p}, odds(p) = {odds(p)}, log_odds(p) = {log_odds(p)}')
    # p = 어떤 일이 일어날 확률
    # 앞면 (성공), 뒷면 (실패) 라고 할 때, odds = 성공/실패/ 성공과 실패의 비율
    # P(A ^ B ^ C) = P(A) * P(B) * P(C) ... 컴퓨터가 계산할 떄에는 오차의 비율이 계속 커진다
    # underflow: a condition in a computer program where the result of a calculation is a number of smaller absolute value than the computer can actually represent in memory on its central processing unit (CPU).
    # log 함수
    # log(a, b, c) = loga + logb + logc
    # 2^3 = 2^(1+2) = 2^1 * 2^2
    # 지수의 특징: a^(x+y) = a^x + a^y
    # x + y = loga(a^x * a^y)
    # log[P(A^B)] = log[P(A) * P(B)] = logP(A) + logP(B)
    # 컴퓨터의 특성상 더하기 빼기가 곱하기 나누기보다 오차율이 적다

    # e = 2.718...
    # log(p/(1-p)) = t
    # p/(1-P) = e^t
    # p에 대해 정의:
    # p = e^t * (1-p)
    # (1 + e^t) * p = e^t
    # p = e^t / (1 + e^t)
    #   = e^t * e^-t / (1 + e^t) * e^-t
    #   = 1/ (1 + e^-t) => sigmoid function
    # log odds 를 알면 x(target?)가 될 확률을 알 수 있다

    t = 1.39
    probability = sigmoid(t)
    print('probability =',probability)


    #odds 함수 그래프
    xs = np.linspace(0.01, 0.99, 100) # 0.01부터 0.99사이의 숫자 100개 생성
    print(xs)
    ys = [odds(x) for x in xs]
    plt.plot(xs, ys)
    plt.ylim(bottom = 0.0, top = 10.0)
    for i in range(1,5):
        plt.axhline(y = (2 * i), color = '0.5') # y = 2,4,6,8 위치에 보조선
        plt.axvline(x = (0.2 * i), color = '0.5') # x = 0.2, 0.4, 0.6, 0.8 위치에 보조선
    plt.title('odds')
    plt.show()

    # log_odds 그래프
    ys = [log_odds(x) for x in xs]
    plt.plot(xs, ys)
    plt.axhline(color = '0.5')
    plt.axvline(color = '0.5')
    plt.axvline(x = 0.5, color = '0.5')
    plt.axvline(x =1, color = '0.5')
    plt.title('log_odds')
    plt.show()

    # log_odds 그래프를 반전시킨 것이 sigmoid 함수이다
    # t 값은 sin limite (puede ser desde minus infinite a plus infinite)
    # sigmoid는 t를 독립변수로 생각한다
    # 그러면 x범위를 바꿔줄 필요가 있다 (0 ~ 1까지는 전체적인 내용이 모두 안나올 수 있다)

    # logistic (sigmoid) 함수 그래프
    xs = np.linspace(-10, 10, 100)
    ys = [sigmoid(x) for x in xs]
    plt.plot(xs, ys)
    plt.axvline(color = '0.5')
    plt.axhline(color = '0.5')
    plt.axhline(y = 0.5, color = '0.5')
    plt.axhline(y = 1.0, color = '0.5')
    plt.title('logistic(sigmoid) function')
    plt.show()
    # t = 0, p = 0.5
    # log_odds 가 0이 되는 경우는 확률이 0.5; 확률이 0.5면 log_odds가 0이다
    # f(x) = 1 / (1 + e^-t)

    # logistic 함수는 선형회귀와 어떤 연관성이 있을까?
    # column x1(petal_len), x2(petal_width) 그리고 y(species, binary)를 가진 dataframe이 있다
    # In 선형 회귀, we can write a formula of getting b0, b1, b2 as: y = b0 + b1 * x1 + b2 * b2
    # predicted/target value: y (0,1)
    # y would have a value i.e. 0.999, 1.999 ... -> we put this value 't' in logistics function, and the sigmoid returns the value between 0 ~ 1
    # we approach the problem using linear regression (-> y = b0 + b1 * x1 + b2 * b2 ) and put it to sigmoid function (sig(y))
    # sig(y) would look like: 1 / (1 + exp[ sigma bixi])
    # returned value will be between 0 to 1
    # when sig >= 0.5, 1 = p; sig <= 0.5, 0 = p
    # The above proving is based on when everything is true; but in real life, we do it to minimize the sum of the squared errors
    # 오차들의 제곱의 합을 평균을 내서 최소화되도록 찾아서 b0, b1,b2... 를 찾는것이 logistic 의 원리






    # self-study
    # what is sigmoid?
    # 이런 그래프가 의미하는 바는 무엇인가, 어떤 수학적 근거로 이런 코드가 짜여졌는가

    # https://deepai.org/machine-learning-glossary-and-terms/sigmoid-function
    # sigmoid function is a way of understanding the ouput of a node or "neuron"
    # r example, a neural network may attempt to find a desired solution given a set of inputs.
    # A sigmoidal function will determine the output and that output will be used as the input for the following node.
    # This process will repeat until the solution to the original problem is found.

    # https: // towardsdatascience.com / sigmoid - neuron - deep - neural - networks - a4cd35b629d7
    # https://towardsdatascience.com/sigmoid-neuron-learning-algorithm-explained-with-math-eb9280e53f07












