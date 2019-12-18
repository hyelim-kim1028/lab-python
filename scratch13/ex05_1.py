"""
Boston House
"""
from sklearn.datasets import load_boston
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.preprocessing import PolynomialFeatures



# 보스턴 집값 데이터 세트 로딩
dataset = load_boston() #bunch : similiar dtype with dictionary of Python (dictionary와 상속관계인 클래스)
print(type(dataset))
print(dataset.keys()) # feature names were stored as keys in dictionary format
print(dataset['DESCR']) #dataset.DESCR
    # returns a thorough description of the data set

# 데이터와 타겟을 구분
X = dataset['data'] # = dataset.data
y = dataset['target'] #dataset.target
# dictionary에서 data와 target을 읽어드리는 방법
print('X.shape',X.shape)
print('X first two',X[:2])
print('y.shape',y.shape)
print('y first two',y[:2])

features = dataset['feature_names'] #dataset.feature_names
print(features)

# When we create a dictionary in Python (i.e. d = {'my_name':'오쌤', 'my_age':16}),
# to invoke a value => print(d['my_name'])
# but in bunch class, we can use two methods to call a value: d['my_name'] & d.my_name
# Caution! dataset.feature-names (connection multiple words with minus sign(-) not dash is impossible)
# Using minus sign equals to feature - mean

# 데이터 탐색 - 그래프
# y와 각 feature들 (y ~ feature) 에 대한 산점도 그래프
fig, ax = plt.subplots(4, 4) #16개의 subplot 생성
ax_flat = ax.flatten()
for i in range(len(features)): #특성(변수)들의 개수만큼 반복
    axis = ax_flat[i]
    axis.scatter(X[:,i], y) # y ~ feature 산점도 그래프
            # feature, target (house price)
    axis.set_title(features[i])
plt.show()

 # LSTAT & RM 에 대해 analysis 진행

# 학습/ 검증 세트 진행
np.random.seed(1217)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.3)
print(f'X_train len: {len(X_train)}, X_test len:{len(X_test)}')

# 학습 세트를 사용해서 선형 회귀 - 단순 선형 회귀, 다중 선형 회귀
# price = b0 + b1 * rm: 주택 가격 ~ 방의 개수
X_train_rm = X_train[:, np.newaxis, 5] # 일차원 배열을 리턴해주지만 sklearn은 2차원 배열을 가정한다
                        # newaxis를 사용해서 새로운 컬럼?을 생성해줌으로써 2차원 배열로 만들어 준다
X_test_rm = X_test[:, np.newaxis, 5]
print(f'X_train_rm: {X_train_rm.shape}, X_test_rm: {X_test_rm.shape}')

lin_reg = LinearRegression() #Linear Regression 객체 생성
lin_reg.fit(X_train_rm, y_train) # fit(적합)/학습(training) -> b0, b1 찾음
# fitting이란 것은 가장 적절한 선 하나를 찾는 것 (절편과 기울기를 찾는다)
# 모델을 적합/학습 시킨다 라고 부른다
print(f'intercept: {lin_reg.intercept_}, coefficients: {lin_reg.coef_}')

# 검증 세트를 사용해서 예측 -> 그래프
y_pred_rm = lin_reg.predict(X_test_rm)
# 실제값은 scatter로, 예측값은(plot) 그래프로 그려본다
plt.scatter(X_test_rm, y_test)
plt.plot(X_test_rm, y_pred_rm, 'r')
plt.title('Price ~ RM')
plt.xlabel('RM')
plt.ylabel('Price')
plt.show()

# Mean Square Error 계산
# error = y - y_hat, error ^ 2 = (y - y_hat)^2
# mse = 1/n sigma (y - y_hat)^2
mse_rm = mean_squared_error(y_test, y_pred_rm)
rmse = np.sqrt(mse_rm)
print(f'Price ~ RM: RMSE =', rmse)

# R2 계산 (결정 계수/ coefficient of determinants) -> sqrt(mse)
r2_1 = lin_reg.score(X_test_rm, y_test)
r2_2 = r2_score(y_test, y_pred_rm)
print(f'price ~ RM: R^2 = {r2_1},{r2_2}')
# 전체 결정의 44퍼센트 정도는 잘 결정한다 라고 이해하면 된다

# price ~ LSTAT 선형 회귀: price = b0 + b1 * lstat
X_train_lstat = X_train[:, np.newaxis, 12] #학습 세트
X_test_lstat = X_test[:, np.newaxis, 12] #검증 세트

lin_reg.fit(X_train_lstat, y_train) #fit, train
print(f'Price ~ LSTAT: intercept = {lin_reg.intercept_}, coefficient = {lin_reg.coef_}')
# 반비례?

y_pred_lstat = lin_reg.predict(X_test_lstat) #예측, 테스트

plt.scatter(X_test_lstat, y_test) #실제값
plt.plot(X_test_lstat, y_pred_lstat, 'r') #예측값
plt.title('Price ~ LSTAT')
plt.xlabel('LSTAT')
plt.ylabel('Price')
plt.show()

# 얼마나 잘 설명하는가는 mse나 r2를 가지고 알 수 있다
mse_lstat = mean_squared_error(y_test, y_pred_lstat)
rmse = np.sqrt(mse_lstat)
# r2 = lin_reg.score(X_test_lstat, y_test)
r2_3 = r2_score(y_test, X_test_lstat)
print(f'Price ~ LSTAT: RMSE = {rmse}, R2 = {r2_3}')

# LSTAT을 보았을 때, 1차보다는 2차가 더 잘 어울릴 수도 있겠다 (그래프가 아래로 볼록하게 생김)
# 그래서 다른 선형관계식을 해보려고함
# Price ~ LSTAT + LSTAT^2 선형 회귀
# Price = b0 + b1 * lstat + b2 * lstat^2
# R2가 더 큰 녀석이 더 모델을 잘 설명해 준다

poly = PolynomialFeatures(degree = 2, include_bias= False)
# interaction_only: 제곱항이나 세곱항을 쓰지 않겠다
# f(x,y) = ax^2 + bxy + cy2 + dx + ey + f
            # interaction_only = True일 때, bxy의 경우 x,y에 관해 값이 변하는 값이니까 두고, x^2, y^2 과 같은 값은 사라진다
# include_bias : 제일 끝에 붙어주는 상수 (f) 값을 포함을 시킬것인가 말것인가 => 필요없다 (False)

# 학습 세트에 다항식 항을 추가 -> fit/train할 때 사용
X_train_lstat_poly = poly.fit_transform(X_train_lstat)
                        # 데이터에 다항식 항들을 컬럼으로 추가해 주는 클래스 객체
                        # 컬럼을 붙여주는 함수 #fit_transform을 꼭 쓰지 않아도 가능하다
                        # 변수가 2개만 되더라도 굉장히 복잡해 지기 때문에 (다항식 특성들 대로 컬럼들을 생성)

# 검증 세트에 다항식 항을 추가 -> predict/test할 때 사용
X_test_poly = poly.fit_transform(X_test_lstat)

# traing set, test set 모두 해줘야한다 (그래야 컬럼의 갯수가 맞으니까)

# fitting
lin_reg.fit(X_train_lstat_poly, y_train)
print(f'intercept: {lin_reg.intercept_}, coefficients:{lin_reg.coef_}')
# 2차 함수라서 there are two coefficients

y_pred_lstat_poly = lin_reg.predict(X_test_poly)

# A

#B

plt.scatter(X_test_lstat, y_test)
xs = np.linspace(X_test_lstat.min(), X_test_lstat.max(), 100).reshape((100,1))
            # X좌표의 최솟값과 최댓값을 찾아서 100개로 나눈다
xs_poly  = poly.fit_transform(xs)
ys = lin_reg.predict(xs_poly)
plt.plot(xs, ys, 'r')
plt.title('Price ~ lstat + lstat^2')
plt.show()

# # From A, when we run this code, multiple lines of pred appear
# y_pred_lstat_poly = lin_reg.predict(X_test_poly)
# plt.scatter(X_test_lstat, y_test)
# plt.plot(X_test_lstat, y_pred_lstat_poly, 'red')
# randomly yielded lines are randomly connected to each other
# ???
# then we have to sort X_test_lstat by size => B
# plt.title('Price ~ lstat + lstat^2')
# plt.show()

mse_poly = mean_squared_error(y_test, y_pred_lstat_poly)
rmse_poly = np.sqrt(mse_poly)
r2_poly = r2_score(y_test, y_pred_lstat_poly)
# lin_reg.score(X_test_lstat_poly, y_test)
print(f'Price ~ LSTAT^2: RMSE = {rmse_poly}, r2_poly = {r2_poly}')
# 44 -> 57로 더 많은 것들을 이야기해주는 그래프가 되었다!

# Price ~ RM + LSTAT의 상관관계를 찾는 선형회귀: price = b0 + b1 * rm + b2 * lstat
X_train_rm_lstat = X_train[:, [5, 12]]
X_test_rm_lstat = X_test[:, [5,12]]
# newaxis parameter 추가해 줄 필요가 없다. 왜냐하면, 이미 2차원 배열의 형태로 나와있기 때문에

lin_reg.fit(X_train_rm_lstat, y_train)
# lin_reg.fit(X_test_rm_lstat, y_test)
print(f'intercept = {lin_reg.intercept_}, coefficient = {lin_reg.coef_}')
# return two coefficients (because there are RM & LSTAT)
# rm은 양수, LSTAT은 음수 (하나씩 찾을 때와의 값과는 다른다, 변수들과의 상관관계가 생기니까)

y_pred_rm_lstat = lin_reg.predict(X_test_rm_lstat) #predict/test
print(f'실제값(y_true): {y_test[:5]}, 예측값(y_pred): {y_pred_rm_lstat[:5]}')

mse = mean_squared_error(y_test, y_pred_rm_lstat)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred_rm_lstat)
print(f'Price ~ RM + LSTAT: rmse = {rmse} & r2 = {r2}')

# Price ~ LSTAT^2의 값이 선생님것과 내것이 다르다 (????)
# 변수가 너무 많으면 overfitting의 문제가 생긴다


# A
# Price ~ RM + LSTAT * RM^2 + RM*LSTAT + LSTAT2
# price = b0 + b1 * rm + b2 * lstat + b3 * rm^2 + b4 * rm * lstat + b5 * lstat^2

poly = PolynomialFeatures(degree = 2, include_bias = False)

# 학습 세트에 다항식항(컬럼)을 추가
X_train_rm_lstat_poly = poly.fit_transform(X_train_rm_lstat)
print(X_train_rm_lstat_poly[:2])

# 테스트 세트에 다항식항(컬럼)을 추가
X_test_rm_lstat_poly = poly.fit_transform(X_test_rm_lstat)
print(X_test_rm_lstat_poly[:2])

lin_reg.fit(X_train_rm_lstat_poly, y_train) # fit/traint
print(f'intercept = {lin_reg.intercept_}, coefficients = {lin_reg.coef_}')
# there should be five coefficeints (since there are five columns)
# rm이 비례하는 관계였는데, 다항식에서는 -1.7의 계수을 주었다 => rm에 반비례한다
# 이건 과적합의 전형적인 예 -> 넣어서는 안될 항들을 넣었기 때문에 발생
# lstat은 반비례 관계였는데, 다항식에서 1.52의 계수를 주었다 => 정비례하게 됨
# rm과 lstat의 interaction(두 값들을 곱하다 보니)이 생겨서 다른 값들의 변화를 미침


y_pred_rm_lstat_poly = lin_reg.predict(X_test_rm_lstat_poly)
print(f'y_true: {y_test[:5]}, y_pred: {y_pred_rm_lstat_poly[:5].round(2)}')
                                        #numpy array

mse = mean_squared_error(y_test, y_pred_rm_lstat_poly)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred_rm_lstat_poly)
print(f'Price ~ RM + LSTAT + RM^2 + RM * LSTAT + LSTAT^2 : RMSE = {rmse}, R2 = {r2}')
# 하지만 RMSE & R2의 값은 오히려 정확도가 더 좋아진 것 처럼 보여준다
# 과적합됐다면 그랬을 듯, 이 데이터 세트에 딱 맞춰진 거니까

# B
# Price ~ RM + LSTAT + LSTAT^2
# price = b0 + b1 * rm + b2 * lstat + b3 + lstat^2
# lstat 은 2차항까지 고려하지만, rm의 제곱항은 고려하지 않은 모델

# 만들어진 데이터 프레임에 컬럼을 추가하는 방법을 이용하면 된다
X_train_last = np.c_[X_train_rm, X_train_lstat_poly]
X_test_last = np.c_[X_test_rm, X_test_poly]
print('X_train_last shape:', X_train_last.shape)
print(X_train_last[:2])
print('X_test_last sahpe:', X_test_last.shape)
print(X_test_last[:2])

lin_reg.fit(X_train_last, y_train)
print(f'Price ~ RM + LSTAT + LSTAT^2: intercept = {lin_reg.intercept_} coefficient = {lin_reg.coef_}')

y_pred_last = lin_reg.predict(X_test_last)
print('y_true:', y_test[:5])
print('y_pred:', y_pred_last[:5].round(2))

mse = mean_squared_error(y_test, y_pred_last)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred_last)
print(f'Price ~ RM + LSTAT + LSTAT^2: RMSE = {rmse}, R2 = {r2}')





