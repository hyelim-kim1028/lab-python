"""
Linear Regression (선형회귀) : 어떤 값을 예측하기위해 사용
Logistic Regression(로지스틱 회귀) : 분류를 위한 알고리즘
"""
from sklearn.datasets import load_iris
# if: from sklearn import datasets
# then, iris = datasets.load_iris()
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split

iris = load_iris()
X = iris['data'] #iris.data
y = iris['target'] #iris.target
features = iris['feature_names'] # iris.feature_names
print(X,y)
print(features) # data와 target은 따로 저장되어 있고, feature_names는 data의 컬럼 이름만 리턴해 준다

# 데이터 프레임 생성
iris_df = pd.DataFrame(X,
                      columns = ['sepal_length', 'sepal_width',
                                 'petal_length', 'petal_width'])

# 데이터 프레임에 변수/컬럼을 추가
iris_df['species'] = y #iris target

print([iris_df.iloc[:5, :]])
print(iris_df.describe())

sns.pairplot(iris_df,  hue="species", palette="husl", vars = ['sepal_length', 'sepal_width','petal_length', 'petal_width'])
plt.show()
# petal length & width 만 알면 구분하기 쉽다
# Error occurred when we only gave hue parameter; we have to give vars = [list of other columns] (weird, it's supposed to work without vars https://seaborn.pydata.org/generated/seaborn.pairplot.html?highlight=pairplot#seaborn.pairplot)

# data(X) & target(y)을 학습/검증 세트로 분리
# iris 는 0,1,2로 정렬되서 나오기 때문에 꼭 섞어줘야한다ㅏㅏ
# 품종별로 완전히 나눠져 있으니까!
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1217)
                                                                    # random_state = seed
# 분야 알고리즘 중에서 logistic Regression을 선택
log_reg = LogisticRegression()

# 모델 적합(fitting)/학습(training) 시키기
log_reg.fit(X_train, y_train)

# predict
predictions = log_reg.predict(X_test)
print('y_true', y_test)
print('y_pred',predictions)
# y = ax + b 와 같은 관계식을 찾으려고하는 것이 아니라, classification을 하기를 원하는것

# 성능 측정: confusion matrix
print('cm', confusion_matrix(y_test, predictions))
# 30개 중에서 1번과 2번이 1개씩 틀렸다
print(classification_report(y_test, predictions))
# recall: sensitivity

# SGDClassifier: stochastic gradient descent

