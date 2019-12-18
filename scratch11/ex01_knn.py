"""
cmd > pip install scikit-learn / if the packaged had been already installed> pip install scikit-learn --upgrade
scikit-learn 패키지를 이용한 kNN(k Nearest Neighbor: 최근접 이웃)
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix,classification_report
from sklearn.model_selection import train_test_split
                                # train set 과 test set으로 split해주눈 함수
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler


class KNeighborClassifier(object):
    pass


if __name__ == '__main__':
    #1. 데이터 준비
    # CSV 파일에 컬럼 이름들이(헤더 정보)가 없기 때문에 컬럼 이름들을 정의
    col_names = ['sepal-length','sepal-width',
                 'petal-length','petal-width',
                  'Class']

    # csv 파일에서 DataFrame을 생성
    dataset = pd.read_csv('iris.csv',
                          header = None, names = col_names) # dataframe 생성

    # DataFrame 확인
    print(dataset.shape) #(row#,col#)
    print(dataset.info()) # 데이터 타입, row 개수, column 개수
    # pandas에서 object는 문자열!!!!!
    print(dataset.describe()) # describe: 요약된 통계정보
    print(dataset.head()) # first 5 data
    print(dataset.iloc[0:5])
    print(dataset.loc[0:4])
    print(dataset.tail()) # last 5 data
    print(dataset.iloc[:5])
    print(dataset.iloc[-5:]) # 마이너스는 거꾸로가는 것 (reversely counted)

    # 데이터 전처리:
    # 1. 데이터 세트를 데이터(포인트)와 레이블로 구분
    # x = 전체 행, 마지막 열 제외한 모든 열 데이터 -> n차원 공간의 포인트
    X = dataset.iloc[:, : -1].to_numpy() #Dataframe > numpy array
            # 행번호, 컬럼번호 => 행 전체 선택, 마지막칸만 제외하고 모두다 뽑는다
    print(X)
    # y = 전체 행, 마지막 열 데이터
    y = dataset.iloc[:, 4].to_numpy() #Dataframe > numpy array
    # scikick-learn 은 numpy의 array타입을 사용한다
    # 그래서 to_numpy()를 사용해서 데이터프레임을 array형식으로 변형시켜주었다
    # array형식으로의 변환에서 인덱스들이 빠지게된다 (col_names)
    # In array data type, only the number indices remain
    # x = point?, y = label > y has the correct answer

    # 2. 전체 데이터 세트를 학습 세트 (training set)와 검증 세트(test set)로 나누기
    # 보통 7:3 or 8:2 정도로 나누어준다
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2) #8:2로 나누어봄
                                    # shuffle both X and y arrays together
    print(len(X_train),len(X_test)) # 120, 30
    print(len(y_train), len(y_test))
    # len로 확인해본 결과 120:30 으로 train set와 test set를 8:2로 나누어 주었다
    print(X_train[:3]) # the order had been shuffled
    print(y_train[:3]) # ['Iris-versicolor' 'Iris-setosa' 'Iris-virginica'] # the three types of iris are randomly mixed

    # 3. 거리 계산을 위해서 각 특성(변수)들을 스케일링 (표준화) > z-score standardization 사용
    # Z-score: 표준화: 평균을 0, 표준편차를 1로 변환
    # 특성(변수): 'sepal-length','sepal-width','petal-length','petal-width',
    # 모든 변수를 평균을 0을 맞추고, 표준쳔차를 1로 만들어서 가중치를 없앤다
    scaler = StandardScaler() #Scaler 객체 생성
    # imported "from sklearn.preprocessing import StandardScaler" for StandardScaler
    scaler.fit(X_train) # scaling(표준화)를 위한 평균과 표준 편차 계산
    X_train = scaler.transform(X_train) # execute scaling(표준화 실행)
    X_test = scaler.transform(X_test) # 스케일링(표준화) 실행
    # 스케일링(z-score 표준화 수행 결과 확인)
    for col in range(4):
        print(f'train평균 = {X_train[:,col].mean()}, train표준편차 = {X_train[:,col].std()}')
                    # array에서 mean을 호출하면 numpy 함수에서 자동으로 계산해준다
                    # 모든 행을 다 선택하고 [:,]; col은 range에 돌아가면서 값이 바뀐다
    # mu와 sigma를 만들어주는 것이 fit()의 역할 -> 표준화값을 계산해주는 키값들
    # X-test는 (fit(X_train))의 값을 사용해서 계산해주기 때문에 정확하게 0과 1이 나오지 않을 수도 있다
    # X_test는 자신의 mu와 sigma를 따로 갖고 계산하는게 아니라, X_train의 그것을 가지고 계산하기 때문에 정확하게 0과 1이 나오지 않을 수도 있다

    for col in range(4):
        print(f'test평균 = {X_test[:, col].mean()}, test표준편차 = {X_test[:, col].std()}')

    # 이렇게 적어줄 수도 있어요
    # for col in range(4):
    #     print(f'train평균 = {X_train[:, col].mean()}, train표준편차 = {X_train[:, col].std()}')
    #     print(f'test평균 = {X_test[:, col].mean()}, test표준편차 = {X_test[:, col].std()}')

    #4. 학습/예측(Training/Prediction)
    # k-NN 분류기를 생성
    classifier = KNeighborsClassifier(n_neighbors=5)
     # KNeighborsClassifier > import 'from sklearn.neighbors import KNeighborsClassifier'
     # n_neighbors=5: 최단거리 5개 요소들을 뽑아서 결정함
     # 이 값은 홀수로 선택하는 것이 좋다 (짝수면 5:5로 겹칠 확률이 있기 때문에)
     # k 의 개수를 조절해 나가면서 정밀도 등을 체크함

     #분류기 학습
    # 정답지 만들기 (characteristics + classification se unieron)
    classifier.fit(X_train, y_train)
    # 예측
    y_pred = classifier.predict(X_test)
    print(y_pred)
    # y_pred에서 예측값들을 반환해준다
    # 실제값: y_test, 예측값: y_pred

    # 5. 모델 평가: confusion_matrix
    conf_matrix = confusion_matrix(y_test,y_pred)
    print(conf_matrix)
    # 완벽해,,,, (my first trial) > the samples were randomly selected so the number of samples may vary and even ther result

    report = classification_report(y_test,y_pred)
    print(report)
# 정확도(accuracy): 전체에서 맞은 것의 비율 (TP + TN)/(TP + FP + FN + TN)
# 정밀도 (맞은 것에 대한 정답) = TP/(TP + FP)
# 재현율(recall) = TP/(TP + FN) # 실제로 x인 녀석들 중에 우리가 맞춘값을 보는 것

    #6. 모델 개선(향상) - k값을 변환시킬 때 에러의 변화 관찰
    errors = []
    for i in range(1,31):
        knn = KNeighborsClassifier(n_neighbors=i)
        knn.fit(X_train, y_train)
        pred_i = knn.predict(X_test)
        errors.append(np.mean(pred_i != y_test))
    print(errors)

    plt.plot(range(1, 31), errors, marker = 'o')
            # x-axis,   y-axis,    # 점들의 모양 (shape of points)
    plt.title('Mean Error with K-Value')
    plt.xlabel('k-value')
    plt.ylabel('mean error')
    plt.show()





