"""
ex01 과 ex02의 함수 만들어 보기
"""
import numpy as np

def train_test_split(X, y, test_size):
    """

    :param X: numpy.ndarray # array of n * m (row * column) #n차원의 점
    :param y: numpy.ndarray.1 x n # 원소의 개수가 n개인 1차원 배열
            # len(X) == len(y)라고 가정 -> len(X) = n = # of rows
    :param test_size:
            # 가정: test_size: 0.0 ~ 1.0 사이
    :return: test_size에 따른 X와 y 분리 (split X and y according to a given test_size)
    """
    length = len(X)
    # X 와 y 가 따로이지만 index가 같이 움직여야한다
    # 인덱스를 저장하는 배열
    indices = np.array([i for i in range(length)]) # index생성
    print('Before the shuffle:', indices)
    # index를 임의로 섞는다 (Randomly shuffle index)
    np.random.shuffle(indices)
    print('After the shuffle: ',indices)
    # shuffle되 인덱스를 가지고 X와 y를 나누어준다 => cut()
    cut = int(length * (1-test_size))
    # int로 묶어서 소수점을 버려준다
    X_train = X[indices[0:cut]] # Train set points
    y_train = y[indices[:cut]] # [:] 에서 0 생략 가능! # Train set label
    X_test = X[indices[cut:]] # Test set points
    y_test = y[indices[cut:]] # Test set label
    # cut이 train의 마지막 인덱스로, test이 첫번째 인덱스로 들어갈 수 있는 이유는, 파이썬은 인덱스의 마지막은 -1을 해주니까 가능하다
    return X_train, X_test, y_train, y_test

# scaling class 선언
class MyScaler:
    # def __init__(self, ncol):
    #     pass
        # 클래스가 가지고 있어야할 변수들은 __init__에서 선언
        # ncol: 평균 & 표준편차를 몇개 선언할 것인가
        # self.feature_means = np.zeros(ncol) # 컬럼의 갯수만큼 0으로 채운 array
        # self.feature_stds = np.ones(ncol) # 컬럼의 갯수만큼 1로 채운 array
        # Class가 하는 일은 메모리 공간 확보?저장? 생성자를 호출하면 init함수는 자동으로 호출
    # 기본값이 없으면 에러를 발생한다 => 그래서 사용하지 않을꺼야

    def fit(self, X): # always the first parameter is 'self'; the function should refer to oneself
        """ X의 각 특성(컬럼)들의 평균과 표준편차를 저장
            # fit = 평균과 표준편차를 계산해주는 함수!!!!!!!
            # 각각 특성/feature/변수의 평균/표준편차 계산; 컬럼의 갯수 만큼 평균 & 표준편차의 값이 반환되어야한다
        """
        # 컬럼별로 평균을 계산해서 저장
        self.feature_means = np.mean(X, axis=0) # axis=0 컬럼별 계산
                                # 만약 axis 를 주지 않는다면 X 전체 값의 평균을 구해준다 ; axis=0: by column, axis=1: by row
        # 컬럼별로 표준 편차를 계산해서 저장
        self.feature_stds = np.std(X, axis=0)
        print(self.feature_means)
        print(self.feature_stds)
            # 여기서 저장된 mean & std를 transform 에서도 사용가능하다

    def transform(self, X):
        """ X의 평균을 0, 표준 편차를 1 (z-score)로 변환해서 리턴;
            X = 변환해야할 데이터"""
        # X와 같은 크기를 갖는 배열을 생성
        dim = X.shape
        # 행(row)와 열(column)의 개수가 같은 배열을 생성
        transformed = np.empty(dim)
                # np.empty 값이 아무것도 들어가 있지 않은 배열을 만들겠다
        for row in range(dim[0]): #row 개수만큼 반복
            for col in range(dim[1]): #shape은 (row#,col#) 을 튜플로 리턴해주는 함수, thus, dim[1] here refers to the col#
                # x_new = (x - mean)/std
                transformed[row, col] = (X[row, col] - self.feature_means[col])/self.feature_stds[col]
                # 원본 X는 남겨두고, tranformed이라는 새로운 변수를 만들어서 사용 -> X이 훼손/변화되면 복구하기 어렵기 때문에
                # transformed 는 z-score standardization 을 따라서 변화시켜주는 것
        return transformed

class MyKnnClassifier:
    def __init__(self, n_neighbors = 5): #객체 생성
        pass

    def fit(self, X_train, y_label):#모델 훈련
        pass

    def predict(self, X_test): #예측
        pass

    # 더 필요한 함수들
    # 점들 간에 거리를 계산하는 함수, 최단거리 k개를 뽑는 함수, 다수결로 투표하는 함수(?), 예측값 리턴





if __name__ == '__main__':
    np.random.seed(1210)
    X = np.random.randint(10, size=(5,2)) #randint를 tuple로 줘서 행과 열을 출력할 수도 있다
    print(X)
    y = np.array(['a','b','a','b','a']) #labels
    print(y)
    # X and y are matched as indices & data set
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2)
    print(X_train)
    print(y_train)
    print(X_test)
    print(y_test)

    # 갑자기 힌트힌트 -> ex 02
    a = np.array([1,2,3])
    b = np.array([1,4,6])
    # 원소끼리의 비교는 (순서대로) numpy의 array이기 때문에 가능하고, Python의 기본 list는 list끼리 비교
    print(a != b)
    print(np.mean(a != b))

    scaler = MyScaler() #객체 생성
    scaler.fit(X_train) #객체가 가지고 있는 메소드 호출
    X_train_scaled = scaler.transform(X_train)
    print(X_train_scaled)

