"""
gapminder.tsv 파일을 읽어서 데이터 프레임 생성
"""
import os

import pandas as pd

df = pd.read_csv('gapminder.tsv', sep = '\t', encoding= 'UTF-8')
print(df.iloc[0:5])

# 오라클의 SQL과 비슷 *0*!!
# boolean indexing/slicing: column의 값을 이용해서 특정 레코드(행, row)들을 선택하는 방법
# DataFrame[컬럼의 값을 이용한 조건식]
df_afg = df[df['country'] == 'Afghanistan']
print(df_afg)

df_kor = df[df['country'] == 'Korea, Rep.']
print(df_kor)

# 대한민국(Korea, Rep.)의 인구와 1인당 gdp를 출력
# print(df['pop','gdpPercap'] ??? df[df['country'] == 'Korea, Rep.']) # my wild guess
print('pop,gdpPercap =', df_kor[['pop','gdpPercap']])

#df_kor이 없다고 생각하고 한줄로 쓰기
print(df[df['country'] == 'Korea, Rep.'] [['pop','gdpPercap']])
    # 이 데이터 프레임에                #인덱스 주기
# 나누어서 생각해줘야함: df(데이터프레임)[df['colname'] == 조건식 -> 데이터 프레임의 일부 행만 추출] [<-인덱스 연산자 ['colname','colname2': 컬럼의 이름들을 리스트로 주었다]]

# mpg.csv 파일을 읽어서 데이터프레임을 생성
file_path = os.path.join('..','scratch08','mpg.csv')
mpg_csv = pd.read_csv(file_path, encoding = 'UTF-8')
print(mpg_csv.iloc[0:5])

# cty컬럼의 평균을 계산
print('mean_mpg_cty: ', mpg_csv['cty'].mean())
print(mpg_csv['cty']) # 데이터타입: series # 0,1,2,3... 이 아이들은 인덱스! # 18, 21 ... 이 아아들은 실제 데이터 -> 시리즈
# column names don't exist
print(type(mpg_csv['cty'])) # <class 'pandas.core.series.Series'> #type 함수를 사용해서 데이터 타입을 알 수 있어요!

print(mpg_csv[['cty']]) # 데이터 프레임에서 커럼'들'을 뽑아내겠다
print(type(mpg_csv[['cty']])) #데이터프레임 #<class 'pandas.core.frame.DataFrame'>
# 이렇게한건 컬럼/들을 뽑아낸 것이기 때문에 하나의 시리즈 객체로 보지않고, 컬럼 이름이 있는 데이터 프레임으로 본다
# 대괄호 1개는 컬럼 1개만 뽑아주세요 -> 데이터타입: 시리즈, 대괄호 2개는 여러개의 뽑아서 만든 하나의 데이터 프레임 -> 데이터 타입: 데이터 프레임

mean_cty = mpg_csv['cty'].mean() #data type: float
print(type(mean_cty)) # <class 'numpy.float64'>
print('avg cty =', mean_cty)
mean_cty2 = mpg_csv[['cty']].mean() #data type: series
# column 이 1개짜리인 컬럼의 평균을 계산해준 것 (비교할 때 괄호 2개 사용 불가! [[]])
print(type(mean_cty2)) #<class 'pandas.core.series.Series'> # 왜 시리즈일까? 원소 1개짜리 시리즈...
print('avg cty2 =',mean_cty2)

# cty 컬럼의 값이 평균보다 큰 레코드를 출력
print(mpg_csv[mpg_csv['cty'] > mean_cty])
subset = mpg_csv[mpg_csv['cty'] > mean_cty]
# [[<- 행들을 뽑아내기 위한 조건식 ]] <- 행들을 뽑아내기 위한 괄호

# cty 컬럼의 값이 cty평균보다 큰 자동차들의 model, displ, cty, hwy를 출력
# select model, displ, cty, hwy from mpg where cty > avg(cty)
print(mpg_csv[mpg_csv['cty'] > mpg_csv['cty'].mean()][['model','displ','cty','hwy']])
print(subset[['model', 'cty', 'hwy']])

# 데이터 프레임과 시리즈와 같은 데이터 타입을 잘 정리/생각을 해야 나중에 안 헷갈린당

