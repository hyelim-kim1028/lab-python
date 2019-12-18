"""
sigmoid function practice: Iris

"""
import math
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np


def logistic(x):
    return 1/(1 + math.exp(-x))

def predict(row, betas): # 이 부분 다시 한번 보기!
    """row의 x1, x2값과 betas의 b0, b1, b2를 사용해서 회귀식 y = b0 + b1 * x1 + b2 * x2를 만들고,
       회귀식을 로지스틱 함수의 파라미터에 전달해서 예측값(y_hat)을 알아냄 """

    # y_hat = betas[0] + betas[1] * row[0] + betas[2] * row[1]
    y_hat = betas[0]  # betas = b0, b1, b2.. ; i = x1, x2 ..
    for i in range(len(betas) - 1):
        y_hat += betas[i + 1] * row[i]
    return logistic(y_hat)
    # error = 예측값 - 실제값

def coefficient_sgd(dataset, learning_rate, epochs):
    """ 회귀식 y = b0 + b1 * x1 + b2 * x2의 계수들이 (b0,b1,b2)을
        stochastic gradient descent 방법으로 추정(estimate) """
    # gradient descent (2차함수 모양의 그래프에서 최저 포인트를 찾을 때: g<0: 오른쪽, g>0 왼쪽) : gradient 방향이거나 반대 방향으로 움직인다
    # 얼마나 움직일것인가를 결정하는 파라미터: learning rate
    # 회귀식에서 처음에 사용할 betas 초기값을 0으로 시작 (betas = b0, b1, b2 ... 잊지말자...)
    betas = [0 for _ in range(len(dataset[0]))] # first row of the df => 0
    for epoch in range(epochs): #epoch 횟수만큼 반복
        #sse = sum of squared errors (오차 제곱들의 합)
        sse = 0
        for sample in dataset: #데이터 세트에서 row 개수만큼 반복
            # A
            prediction = predict(sample, betas) #첫번째 샘플에 대한 예측값 #betas로 추정한 예측값
            error = sample[-1] - prediction # error = true - prediction
            sse += error**2 #sum of squared errors
            # 계수들(b0, b1, b2)을 업데이트
            # 이 값들을 기본으로 sgd을 해서 최소값을 찾아 들어가는 것?/ 각 대수들을
            # b_new = b + learning_rate * error * prediction * (1 - prediction) * x
                # b comes betas                                             # x values (b0 일 때는 x =1, b1 일 때는 x1의 값...)
            # 왜 이런 식이 나왔는지 알아보기
            # error값을 가지고 ->
            # sigmoid 분모 안에 exp(-b + b1x1 + b2x2) => b에 대해 미분하려고한다 (x는 값들을 아는 상수들이고, 변하는 변수들은 betas)
            # exp(b + b1x1 + b2x2) / (a/ab0) exp[-(b + b1x1 + b2x2)]
            # exp() * x (x의 값이 x1, x2로 바뀜 -> 편미분해줘서...)
            # b0에 대해 미분을하면 -1이 되니까 -1을 넣어준 것
            # B
            betas[0] = betas[0] + learning_rate * error * prediction * (1 - prediction)
            for i in range(len(sample)-1):
                betas[i + 1] = betas[i+1]+ learning_rate * error * prediction * (1 - prediction) * sample[i]
                # 처음 루프에서는 A에서 0에서 시작한다. 두번쨰 부터는 B에서 바뀐 베타 값들을 가지고 계산을 한다
                # 행에 있는 모든 샘플들에 관해서 각각 다른 베타를 적용해서 계산하고, 이 두 줄의 과정을 embracing loop (for epoch in range(epochs))이
                # 몇번이고 반복하면서 오차값이 줄어든다 (sample 10개를 모두 반복하는 것이 1개의 epoch/ 1 epoch = 10 samples)
                # stochastic: 1 epoch = 10 samples 해서 반복횟수가 많다/ batch: 반복횟수가 적지만 최솟값을 못 찾을 수도 있다/ mini-batch: stochastic 과 batch 의 중간
        print(f'>>> epoch = {epoch}, learning_rate = {learning_rate}, sum_squared_error = {sse}')
    # 모든 epoch가 끝난 다음에 최종 betas를 리턴
    return betas



if __name__ == '__main__':
    iris = load_iris()
    #print(iris.DESCR)
        # Number of Attributes: 4 numeric, predictive attributes (= ['data']) and the class (= ['target'])
    X = iris.data #iris['data']
    y = iris.target #iris['target']
    features = iris.feature_names #iris['feature_names']

    for i in range(len(features)):
        plt.scatter(X[:, i], y, label = features[i])
                # all the rows, i번째 column
    # y = 0,1,2 ~ species
    plt.legend()
    plt.show()

    # petal-length와 petal-width가 class(품종)을 분류할 때 상관관계가 높아 보임
    # (in my own words) 다른 컬럼들과 겹치는 면적이 적어서 더 독립적으로 보임
    X = X[:, 2:4] # selected all rows & second and third columns (pl, pw)
    print(X[:5])

    # Setosa 5개, setosa가 아닌 품종 5개를 샘플링
    indices = [x for x in range(0, 100, 10)] # or  indices = [10 * x for x in range(10)]
    sample_data = np.c_[X[indices, :], y[indices]]
                         # column은 이미 2개가 짤린 것을 집어 넣은 것 이기 때문에 전체를 선택했지만 2개의 컬럼만 보여준다
    print(sample_data)

    # sample 데이터 만큼 반복
    np.random.seed(1218)
    betas = np.random.random(3) #난수 b0, b1, b2를 생성
    print(betas) # the returned values correspond to b0, b1, b2

    for sample in sample_data: # sample_data에서의 row를 꺼내준다
        prediction = predict(sample, betas)
        # error = true_val - pred_val
        error = sample[-1] - prediction
            # sample[-1 = 마지막 컬럼]
        print(f'True Value: {sample[-1]}, Predicted Value: {prediction}, Error = {error}')
        # prediction이 얼마나 실제값에 가깝게 예측을 했는가
        # For the data y = 1, the error is small, but for the data y = 0,

        # From a random beta numbers, we found error rates -> using gradient descent, we move slowly to get the b0, b1, b2 to get the minimum mean error rates
        # this all starts from regression ( y = b0 + b1 * x1 + b2 * x2 ...)
        # 미분을 해주어야한다 ( sigmoid를 미분을 일단 해보자)

        # f(x) * g(x) 를 곱해서 전체를 미분을 하면 [f(x) * g(x)]' = f'(x)*g(x) + f(x)*g'(x)
        # (x * x^3)' = 1 * x^3 + x(3x^2) = 4x^3
        # x^n' = nx^(n-1)
        # [f(x)/g(x)]' = f'(x)*g(x) - f(x)*g'(x) /[g(x)]^2
        # 미분 필히 공부하기 오늘

        # sigmoid 함수 미분
        # (1/1+e^-x)' = -1 * (-e^-x) /(1 + e^-x)^2 = e^-x / (1+e^-x)^2
        #             = 1 + e^-x -1 / (1+e^-x)^2  = 1/(1+e^-x)(1 - 1/(1+e^-x))
        #             = f(x)(1 - f(x))
        # exponential 은 미분해도 함수가 바뀌지 않는다

        # 합성 함수의 미분법 (https://bhsmath.tistory.com/184)
        # 미분 연쇄 법칙 (https://blog.naver.com/mindo1103/90103548178)
        # df/dx = df/du * du/dx    # when u = x^2
        # d/dx(e^(x^2)) = d/du(e^u)*(du/dx)
        #               = e^(x^2) * 2x

        # coefficient_sgd()
        learning_rate = 0.3
        epochs = 100
        betas = coefficient_sgd(sample_data, learning_rate, epochs)
        print('beta =', betas)
        # 골라낸 10개의 샘플로 fitting을 하는 과정

        # 모델 성능 측정
        test_sample1 = np.r_[X[1, :],y[1]]
        prediction = predict(test_sample1, betas)
                                    # epoch를 돌린 betas
        print(f'True: {test_sample1[-1]}, predicted: {prediction}')
        # what does prediction say?

        # 다른 샘플 만들어보기
        test_sample2 = np.r_[X[51,:],y[51]]
        print(test_sample2)
        prediction = predict(test_sample2, betas)
        print(f'true: {test_sample2[-1]}, predicted: {prediction}')
        # 100개가 10번 반복이니까 1000번 반복된 베타를 가지고 이진분류 (1과 0을 분류)한 값

        # regression은 b0,b1,b2의 값들을 예측? 하려고 상요하는거고,
        # logistic regression은 그 예측한 값들을 가지고 0 혹은 1로 이진분류를 하는
        # beta를 계속 반복하는 이유 sse를 줄이기위해서
        # sigmoid함수 안에 선형회귀식이 들어가 있는 것

        # 알고리즘 내부에서 epoch를 모두 반복하지 않을 수도 있다
        # 2차함수에서 최솟값을 찾아가다가, epoch를 아무리 반복해도 최솟값근처 (임계값, tolerance)에서 방황하는 경우가 있다
        # If the program roams around? near the points within the range of tolerance(임계값), 이 때에는 더 빨리 끝낸다

        # today's key words: perceptron, 미적분, sigmoid function/curve, step function, regression, gradient descent

