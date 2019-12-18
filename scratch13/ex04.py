"""
y = b + a * x : Linear Regression
y = b + a1 * x + a2 * x^2 : non-linear regression -> 선형 회귀로 b, a1, a2를 결정할 수 있다
비선형회귀: 다항식이 포함되어 있다!!!

y = b + a1 * x1 + a2 * x2 + ... : 성형 회귀
y =  b + (a1 * x1) + (a2 * x2) + (a3 * x1^2) + (a4 * x1 * x2) + (a5 * x2^2) ...
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
# Polynomial(다항식) Features(특성들) => 변수들을 다항식으로 만들어 주는 아이

np.random.seed(1216)
X = 6 * np.random.rand(100, 1) - 3
# np.random.rand -> 0 <= r < 1
# 6 * np.random.rand => 0 <= r < 6
# 6 * np.random.rand(100, 1) - 3=> -3 <= r < 3
# -3 <= r < 3 의 숫자 100개 생성
print('X =', X[:5])

# target
y = 0.5 + 2 * X + X ** 2 + np.random.randn(100, 1)

# plt.scatter(X, y)
# plt.show()
# 이차 함수 모양의 그래프가 만들어 졌다
# 2차 함수가 오차를 가장 줄여줄 수 있는 그런 값이 될 것

A = np.array([[1],[2],[3]]) # 3X1 행렬(2차원 리스트)
print('A =', A)
poly_feature = PolynomialFeatures(degree = 2, include_bias= False) # polynomialfeatures이 알아서 조합해줘서 polynomial을 생성
A_poly = poly_feature.fit_transform(A)
print('A_poly = ',A_poly)
# degree: 몇 제곱까지 있는 것인가
# include_bias: 절편을 올리고 내리고 하는 것
# x의 제곱의 값을 추가한 새로운 행렬이 만들어 졌다
# 그럼 이 행렬을 LinearRegression에 a1 * x + a2 * x2^2을 넣어주면 첫번째의 계수와 두번째의 계수를 알려준다
# fit_transform 이 자동으로 추가해준다

B = np.array([[1,2], [3, 4]]) # 2X2 행렬(2차원 리스트)
print('B =', B)
B_poly = poly_feature.fit_transform(B) # x1^2, x1*2,x2^2 columns were added
print('B_poly =', B_poly) # 2 * 5 # 원래 가지고 있던 컬럼들은 그대로이고 (A), 컬럼의 갯수가 늘었다 (de x1^2, x1*2,x2^2)
# x1과 x2를 가지고 만들 수 있는 모든 아이들을 만들어서 (de x1^2, x1*2,x2^2)  컬럼들을 붙여준다
# degree = 2로 줬기 때문에 2의 다항식의 모든 변수들을 만들어 준 것

# 실제로 해야할 일: X(데이터)와 y(타켓); X에 제곱항들을 추가
X_poly = poly_feature.fit_transform(X)
print('X_poly =', X_poly[:5]) # 변수 2개짜리 데이터 프레임

lin_reg = LinearRegression()
lin_reg.fit(X_poly, y) # 바꾼 Polynomial들을 적합 시킴 (적합시키다: y-절편, a1의 기울기,,, 등등을 찾아나가는 과정)
print('intercept:', lin_reg.intercept_)
print('coefficients:', lin_reg.coef_)
# y = b + a1 * x + a2 * x^2 # 여기에 우리가 사용할 절편과 1차항의 계수 a1 & 2차항의 계수 a2를 찾은 것
# 결국 선형회귀로 귀결이 된다
# 그러기위해 편리한 클래스: Polynomical Features
# 원본 데이터 프레임을 정제해주는 역할 # preprocessing 안에 있다

X_test = np.linspace(-3, 3, 100).reshape(100, 1)
print(X_test[:5])
print(X_test[-5:])
X_test_poly = poly_feature.fit_transform(X_test) # X_test_poly를 넣어주어야 제곱항 같은 것도 계산이 가능하다
# 비슷한 간격으로 숫자 100개를 만들었다

y_pred = lin_reg.predict(X_test_poly) # 훈련, 테스트 세트 모두 같은 polynomial 로 만들어주고 predict을 돌려야한다 
plt.scatter(X, y)
plt.plot(X_test, y_pred, 'r')
plt.show()










