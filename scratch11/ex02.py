"""
R을 활용한 머신 러닝 - 위스콘신 대학의 유방암 데이터 (csv)

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

if __name__=='__main__':
    # csv 파일에서 DataFrame을 생성
    dataset = pd.read_csv('wisc_bc_data.csv')

    #DataFrame 확인
    print(dataset.head())
    print(dataset.describe()) # 스케일링이 필요한 데이터 (컬럼간 편차가 심하다)
    print(dataset.info()) # 569 * 32

    #데이터 전처리
    # 1. n 차원상의 point와 레이블로 구분
    X = dataset.iloc[:,2:].to_numpy() #DataFrame > nd array
    # print(X)
    y = dataset.iloc[:,1].to_numpy()
    # print(y)
    print(X[0])
    print(y[0])
    # X는 n차원이라 대문자로 써주었고, y는 1차원이라 소문자로 써주었다
    # X is in uppercase because it's n-dimensional, on the other hand, y is in lowercase because it's 1-dimensional array? value?

    # 2. 전체 데이터 세트를 학습 세트와 검증 세트로 나누기 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
    print(len(X_train), len(X_test))

    # 3. 거리 계산을 위해서 각 변수들을 표준화
    scaler = StandardScaler()
    scaler.fit(X_train) #X_train 세트의 평균/표준편차 계산
    X_train = scaler.transform(X_train) # 학습세트 스케일링
    X_test = scaler.transform(X_test) # 테스트 세트 스케일링

    for col in range(4):
        print(f'train avg = {X_train[:, col].mean()}, train std = {X_train[:,col].std()}')
        print(f'test avg = {X_test[:,col].mean()}, train_std = {X_test[:,col].std()}')

    print(np.mean(X_train[:,0]), np.std(X_train[:,0]))
    print(np.mean(X_test[:, 0]), np.std(X_test[:, 0]))

    #4. 학습 예측
    classifier = KNeighborsClassifier(n_neighbors = 5)

    #분류기 학습
    classifier.fit(X_train, y_train)

    # 예측
    y_pred = classifier.predict(X_test)
    print(y_pred)


    #5.모델 평가
    conf_matrix = confusion_matrix(y_test, y_pred)
    print(conf_matrix)

    report = classification_report(y_test, y_pred)
    print(report)

    # 6. 모델 개선/향상
    errors = []
    for i in range(1, 41): # k 값이 변경 될때마다 X와 y를 새로 만들어줘야하기 때문에
        knn = KNeighborsClassifier(n_neighbors=i)
        knn.fit(X_train, y_train)
        pred_i = knn.predict(X_test)
        errors.append(np.mean(pred_i != y_test))
    print(errors)

    plt.plot(range(1,41), errors, marker = '*')
    plt.title('')
    plt.xlabel('k-value')
    plt.ylabel('mean error')
    plt.show()