import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.datasets import load_diabetes

# X, y = load_diabetes(return_X_y=True)
# print(X[:5])
# print(X.shape, y.shape)

datasets = load_diabetes() #데이터세트를 자동으로 가져온다
X = datasets.data
y = datasets.target # 레이블, 예측값
print(X.shape, y.shape) #row와 column 갯수 반환
features = datasets.feature_names #변수의 이름들
print(features)
print('X[0] =',X[0]) #첫번째 행 -> 데이터프레임 확인
# 모든 특성(컬럼)들이 평균=0, 표준 편차=1 로 전처리가 되어 있는 데이터 세트.
print('y[0] =',y[0])

# dataframe & np의 ndarray냐의 구분을 확실히 해주어야한다!!!

# even age & sex are in number
# According to a document of Scikit-learn, the diabetes data is a normalized dataframe where 평균 = 0, 표준편차 = 1? 로 변환 끝 (다시 확인)

# 선형 회귀(linear regression)
# y = b + a * x
# y = b0 + b1 * x1 + b2 * x2 + ... # bmi 와 혈압의 상관관계도 알 수 있다


# # y ~ age, y ~ sex, y ~ bmi, ...
# X_transpose = [column for column in zip(*X)]
# # X_transpose = np.transpose(X)
# # print('X_transpose shape:', X_transpose.shape)
# print('X_transpose[0] =',X_transpose[0])
# transpose: 다중회기분석에서 사용! 왜 여기에 와 있는지 모르겠음

# 1개의 figure에 10개의 subplot를 그려서, 변수들과 당뇨병(y)의 대략적인 관계를 파악.
fig, ax = plt.subplots(3, 4) # 화면분할 (행, 컬럼)
for row in range(3): #0,1,2 #행번호
    for col in range(4): #0,1,2,3 # 컬럼번호
        axis = ax[row, col] # 서브플럿을 찾아서
        idx = 4 * row + col # 그림을 그린다
        if idx > 9:
            break
        # x = X_transpose[idx]
        x = X[:, idx] # [행번호 전부, 컬럼번호] # x 좌표가 모든 행의 대해서 컬럼별로 읽어준다
        axis.scatter(x, y)
        axis.set_title(features[idx])
plt.show()

# subplot(3,4)의 이중컬럼을 더 간단하게 그리기

# 이해를 돕기 위한 배열을 만들어 보자
array = np.array([[1,2],
                  [3,4]])
print(array) # 2 X 2 행렬(2차원 배열)

# 우리가 [1,2], [3,4] 의 배열에서 원소들을 하나씩 꺼내고 싶을 때:
# 원래는 반복문을 2번써서 꺼내준다
for row in range(2):
    for col in range(2):
        print(array[row, col], end = ' ') #옆으로 출력
print()

array_flatten = array.flatten()
# flatten 이라는 method를 사용하면 반복문을 하나만 사용할 수 있다
for i in range(4):
    print(array_flatten[i], end = ' ')
print()
# flatten 은 차원을 줄여서 쭉 펼쳐진 형태로 보여주는 것

# 이 개념을 subplt[3,4]에 적용
fig, ax = plt.subplots(3,4)
print(ax)
# [<matplotlib.axes._subplots.AxesSubplot object at 0x0000012EF160F648>
#   <matplotlib.axes._subplots.AxesSubplot object at 0x0000012EF1875B88>
#   <matplotlib.axes._subplots.AxesSubplot object at 0x0000012EF18B0608>
#   <matplotlib.axes._subplots.AxesSubplot object at 0x0000012EF18EB108>]
# 요렇게 생긴게 4개가 있는 ax: 3*4 형태의 2차원 배열
ax_flat = ax.flatten()
for i in range(len(features)): # features/ 변수들의 이름 = 컬럼의 갯수
    subplot = ax_flat[i]
    subplot.scatter(X[:, i], y)
    subplot.set_title(features[i])
plt.show()

# bmi 와 y (당뇨병 수치)의 선형 관계식 찾아보기 : y = b + a * bmi
# bmi = X[:, 2]
bmi = X[:,np.newaxis, 2] # bmi is the second column of the table
# scikit-learn의 LinearRegressions은 훈련 데이터 세트가 반드시 2차원 배열 세트만 사용하기 때문에 newaxis를 삽입해주었다
print('bmi = ',bmi[:5]) # ndarray type
print('bmi.shape',bmi.shape)
# np.newaxis = 를 사용한 후에, np.newaxis 는 행을 컬럼? 으로 한다구??
# newaixs 는 아무것도 안들어간 축만 하나 만들겠다는 뜻... 그럼 2차원 배율을 만들 수 있다

# bmi 를 학습(training)/검증(test) 세트로 분리
bmi_train = bmi[:-40]
bmi_test = bmi[-40:]
y_train = y[:-40]
y_test = y[-40:]

# 선형 회귀 모델(linear regression model) 객체 생성
regr = linear_model.LinearRegression()
            # 가장 간단한 선형회귀 모델

# training set를 학습시킨다 (fit)
regr.fit(bmi_train, y_train) # 직선의 방정식이 결정된다 (y절편과 기울기a가 나오기 때문에 아래에서 예측 가능)
    # y  = b + a * bmi 선형 관계식에서 y절편b와 기울기 a를 결정 (a와 b를 결정하는 것을 우리는 '학습시킨다' 라고 일컫는다)
    # 65번째 라인: 이거 바로 이 라인이 잘 못 되어서 error
    # 2darray 인데 1darray 를 사용해서 에러가 났다!
    # 1가지 변수더라도 train만 써주면 1-dimension 어레이라서 사용할 수 없다
    # 2d여야한다!!
    # bmi 는 1줄로된 1차원이었다 => [[1]] or [[1 ] [[2   ]]
    # 이렇게 [] 를 두개씩 해준다면 2-dimension 이 된다
print('coefficients:', regr.coef_) #기울기 (50/0.05)

# 예측 / 검증 세트로 테스트 # x값에 관해서 y값이 어떻게 되는지
y_pred = regr.predict(bmi_test)
print(y_pred)

plt.scatter(bmi_test, y_test) # 실제 값
plt.scatter(bmi_test, y_pred) #예측값 # 'ro-' 를 줘서 빨강색 동그마이인 직선으로 바꾸었는데 나는 안됨 ㅠㅠㅜ 고민!
# linear line, 이름에 걸맞게 직선으로 표시한다
# 이 직선의 방정식을 찾는 방법이 경사하강법 (descendent gradient)
# 오차들의 제곱의 합을 최소화시킬 수 있도록 직석을 찾아 나가는 과정 => 선형회기
plt.title('Diabetes vs BMI')
plt.xlabel('BMI')
plt.show()

# y ~ s5 선형 관계식을 찾고, 그래프를 그림
# 모델을 새로 만들고, 그 모델에다 새로운 트레인 세트를 준다
s5 = X[:, np.newaxis, 8]
    # 2차원 배열 형태로 's5' 컬럼을 선택

# bmi를 학습/검증 세트로 분리
s5_train = s5[:-40]
s5_test = s5[-40:]
# 위와 동일하기 때문에 굳이 나눌 필요가 없다!
# y_train = y[:-40]
# y_test = y[-40:]

# 선형 회귀 모델 객체 생성
regr = linear_model.LinearRegression()

# training set을 학습 시킨다 (fit)
regr.fit(s5_train, y_train)
print('coefficients:', regr.coef_) #직선의 기울기

# 예측/검증 세트로 테스트
y_pred = regr.predict(s5_test) #예측값 찾기
print(y_pred)

plt.scatter(s5_test, y_test) #실제값
plt.scatter(s5_test, y_pred) #예측값
plt.title('Diabetes vs S5')
plt.xlabel('s5')
plt.show()

# y절편과 x의 값들을 움직여 가며 최소의 에러률을 가진 값을 찾는 것

# X라는 데이터 프레임에서 1개의 변수를 가지고 선형회귀식을 찾아본다.
# newaxis는 늘 넣어야한느 이유는 2차원 배열을 억지로 만들어야해서 빈 컬럼을 그냥 넣은 것
# Linear Regression은 x자리에 들어오는 리스트가 2차원 리스트가 들어와야한다 (컬럼이 몇개든)
# [[], [], ... []] 이렇게 생긴 아이만 동작함
# 컬럼 여러개를 선택한다면 이미 2차원 배열이라 괜찮지만, 위 처럼 컬럼을 1개만 선택할 때에는 조심!

