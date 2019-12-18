import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X = 2 * np.random.rand(100, 1)
print(X)
# 숫자 100개를 2차원 배열 형태로 만든다
# 0.0~2.0 사이의 숫자들로 이루어진 100X1 행렬(2차원 ndarray)
# rand는 기본적으로 0 부터 1 사이의 숫자를 난수로 만들어 주는데, 2를 앞에서 곱하주었기 때문에 0에서 2 사이의 숫자를 생성
# rand는 uniformly distributed (거의 겹치는 것 없이 균일하게 나옴)
print('X_shape =',X.shape) # (100,1) => 100 rows & 1 column
# 행렬계산을 하기 때문에 2차원 배열의 형태로 만든다

y = 4 + 3 * X + np.random.randn(100, 1) # 1차원 선형식
# 만약 random 넘버를 붙여주지 않으면 1직선이 나오기 때문에,
# y = 4 + 3x 와 비슷한 자리에 있는 점들을 생성하기 위해 위와 같은 식을 써주었다 np.random.randn(100, 1)
# randn = 정규분포를 따르며 난수를 생성
print('y_shape =',y.shape)

plt.scatter(X, y)
plt.title('scatter X & y')
plt.show()

# 어떻게 에러가 가장 적은 직석의 방정식을 찾을 것 인가?
# y = b + a * X 를 만족하는 a와 X를 찾으려고 하는 것
# X에 100개의 점이 있고,

X_b = np.c_[np.ones((100,1)), X]
# shape 으로 바로 주게 되어 있어서 ones에 튜플로 ((100,1)) 줘야한다
# 컬럼의 붙여주는 기능 c_

# X_b = np.c_[np.ones((100,1)), X]은:
# np.ones는 행렬을 모두 1로 채우는 메소드, (100,1) 은 모양이다
# 행의 갯수는 100개, 컬럼의 갯수는 1개인 1로 채워진 행렬?
# 첫번째 파라미터 size, 두번째는 데이터 타입

# np.ones(100,1)의 에러 이유:
# ones는 shape, dtype = None 이런 파라미터를 가지고 있는데,
# (100,1) 로 값을 준다면, shape = 100이라고 dtype = 1이라고 준 것과 같다
# 그래서 튜플로 ((100,1))으로 다시 준것!

print('X_b_shape =', X_b.shape)
print(X_b[:5])

# linalg 모듈: linear algebra(선형 대수)의 약자
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
# y = X dot theta
# theta = (X^t dot X)^-1 dot X^t dot y
# ^-1 이 inverse (항등행렬이 나오게해주는 것)
print('theta_best',theta_best) # y절편과 기울기를 구해준다
# inner product (내적 곱셈) -> 중요한 컨셉! 공부하자 공부 ㅠㅠㅜㅜ 제발 마니마니

# 모든 점들의 곱의 합의 에러가 가장 적은 직선을 찾는것?

# 행렬식을 이용해서 찾은 theta 값과 LinearRegression 클래스에서 계산된 theta 비교
# import a package: from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression() #객체 생성
lin_reg.fit(X, y)
print(f'y절편: {lin_reg.intercept_}, 기울기: {lin_reg.coef_}')
# theta_best 와 LinearRegression 객체를 사용해서 얻은 값이 같다

# 이런것들이 안쪽에서 계산되기 때문에 이 값들을 가지고 예측을 할 수 있다
X_test = [[0],
          [1],
          [2]] # 컬럼이 1개짜리라도 2차원 배열로 만들어 줘야 사용할 수 있다

# 행렬식: y = X_b @ theta
X_test_b = np.c_[np.ones((3,1)), X_test] # 우리가 행렬을 만들어서 사용할 때에는 빈 컬럼에 1을 넣는 작업을 해줘야함
print(X_test_b)
y_pred = X_test_b.dot(theta_best)
print(y_pred) # 예측값이다

# Scikit-Learn 패키지를 사용한 예측
predictions = lin_reg.predict(X_test) #skitlearn은 자동으로 패키지가 행렬을 만들어서 빈 컬럼을 채워준다
print(predictions)

# 행렬식: y = X_b @ theta 을 이용한 예측값과 Scikit-Learn 패키지를 사용한 예측은 동일하고, y절편과 ~ 가 같을 수 밖에 없기 때문에

plt.scatter(X, y)
plt.plot(X_test, y_pred,'ro-')
plt.show()

# 오차들의 제곱의 합의 평균의 최소를 알려주는 선

#  y = b + (a1 * x1) + (a2 * x2)
# 변수 두개에 해당 하는 식 : 선이 아닌 평면을 리턴해 준다
