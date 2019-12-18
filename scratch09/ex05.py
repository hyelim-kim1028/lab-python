"""
gapminder.tsv 불러온 방법: 선생님 컴퓨터에서 파일을 다운 받은 후에, scratch09 에 대고 ctrl + c, ctrl + v 그리고 확인, 확인
gapminder.tsv 파일을 pandas 패키지의 read_csv() 함수를 사용해서 DataFrame 으로 변환
DataFrame의 행과 열의 개수 확인
DataFrame의 앞의 데이터 5개를 출력
DataFrame의 뒷쪽 데이터 5개 출력
DataFrame 에서 컬럼 이름들을 출력
DataFrame의 각 컬럼의 데이터 타입들을 출력
DataFrame에서 'country', 'lifeExp','gdpPercap' 컬럼들만 출력
DataFrame 에서 행 인덱스가 0, 99, 999번인 행들을 출력
DataFrame 에서 행 레이블이 840번부터 851번까지인 행들의 나라이름, 기대 수명, 1인당 GDP를 출력

<수업시간에 다루지 않은 내용>
DataFrame 에서 연도별 기대 수명의 평균을 출력하여라 (group by - mean)
DataFrame 에서 연도별, 대륙별 기대 수명의 평균을 출력하여라
"""
import os
import pandas as pd
import csv
import matplotlib.pyplot as plt

# gapminder.tsv 파일을 pandas 패키지의 read_csv() 함수를 사용해서 DataFrame 으로 변환
file_path = os.path.join('gapminder.tsv')
df = pd.read_csv(file_path, sep = '\t')
print(df)

# Teacher's solution
# gapminder = pd.read_csv('gapminder.tsv', sep = '\t', encoding = 'UTF -8')
# 꼭꼭 \t추가해줘야함니당 (기본이 , )

print('shape:', df.shape)   # DataFrame의 행과 열의 개수 확인
print('first five', df.head()) # DataFrame의 앞의 데이터 5개를 출력
print('last five', df.tail())# DataFrame의 뒷쪽 데이터 5개 출력

# 행 인덱스를 이용한 출력 / other way of using head, tail
#DataFrame.iloc[행번호/ rowindex, 열번호/columnindex]
# 만약 column index를 생략하면, 선택한 row index 의 모든 컬럼이 선택된다
print(df.iloc[0:5])
nrows, ncols =  df.shape
print(f'nrows =  {nrows}, ncols = {ncols}')
print(df.iloc[nrows - 5: nrows]) #  파이썬은 마지막 숫자는 포함하지 않으니까 이렇게 써준는게 맞아
# a:b 에서 a <= x < b ( 이렇게 때문에 -1을 안하는게 맞다)
print('headers', list(df)) # DataFrame 에서 컬럼 이름들을 출력
print('headers', list(df.columns))
print('column names', df.columns) # 컬럼이름들을 알아내면 변수처리해서 일하기가 쉬워진다
                                  # (아니면 인덱스 번호만 가지고 사용해야하는데, 그러면 내가 무슨 컬럼을 사용하는지 가독성이 떨어진다)
print('data types', df.dtypes) # DataFrame의 각 컬럼의 데이터 타입들을 출력
# DataFrame.dtypes: 각 컬럼의 이름과 데이터 타입을 저장하고 있는 프로퍼티

# pandas.read_csv() 함수는 파일의 문자열들을 타입에 맞게끔 변환하는 기능을 가지고 있음
# pandas 데이터 타입: object 는 문자열/string, int64(64비트 정수), float64(64비트 실수)
# 1 byte = 8 bits 이다
# 더 많은 용량을 사용해서 정수를 사용한다. 64 바이트 = 8 비트, 그러니까 파이썬은 정수, 실수 모두 8 비트를 사용해서 저장한다
# 보통 C와같은 다른 언어는 정수는 4비트를 사용해서 저장. 결론적으로 파이썬은 큰 정수까지 저장할 수 있는 타입이라고 생각해주면 된다


# DataFrame에서 'country', 'lifeExp','gdpPercap' 컬럼들만 출력
# country = df['country']
# lifeExp = df['lifeExp']
# gdpPercap = df['gdpPercap']
# print(country, lifeExp, gdpPercap)

# teacher's solution
# DataFrame[*column names]: 데이터 프레임에서 컬럼을 선택
# 행번호 주지 않고 컬럼 이름들만 주는 가장 간단한 방법
col_names = ['country','lifeExp','gdpPercap']
print(df[col_names])


# DataFrame.iloc: 특정행을 선택하는 방법
# DataFrame 에서 행 인덱스가 0, 99, 999번인 행들을 출력
print(df.iloc[0])
print(df.iloc[99])
print(df.iloc[999])

# teacher's solution
row_indices = [0, 9, 99]
print('row_indices =',[df.iloc[row_indices]])
# OR
print("row_indices' =",df.iloc[[0,9,99]] )

# DataFrame 에서 행 레이블이 840번부터 851번까지인 행들의 나라이름, 기대 수명, 1인당 GDP를 출력
print(df.iloc[840:852][['country','lifeExp','gdpPercap']]) # My code
print(df.loc[840:851, ['country','lifeExp','gdpPercap']]) # Teacher's solutionn # N:M 으로 인덱스를 주면 이름을 주는거니까 그대로 출력해준다
print(df.iloc[840:852, [0,3,5]]) # iloc 는 N:M 으로 인덱스를 줄 경우 이상 미만이라서 M + 1의 값을 줘야한다

#DataFrame.iloc[row index, column index]
#DataFrame.loc[row label, column label]
# loc에서 범위 연산자(:)가 사용되면, 이름(label)로 취급하기 때문에 양쪽 숫자 모두 포함
# iloc에서 범위 연산자(:)가 사용되면, 인덱스로 취급하기 때문에 뒤쪽 숫자는 미포함

# DataFrame 에서 연도별 기대 수명의 평균을 출력하여라 (group by - mean)
# print('life Exp according to year =',df.groupby(['year'].sum(lifeExp)))
# I think the problem with the code is that 'year' column is not in df?? como puede serrrrrrr
# year = df['year']
# print(df.groupby(year).sum(lifeExp))
# grouped.mean()
# df2 = pd.concat([df, 'year'])

# teacher's solution
df_by_year = df.groupby('year')
print(df_by_year) # solo sale: <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001BA4CDC1D08> -> DataFrameGroupBy 객체
print(df_by_year['lifeExp']) #<pandas.core.groupby.generic.SeriesGroupBy object at 0x0000019051596388> -> SeriesGroupBy 객체
print(df_by_year['lifeExp'].mean())

# DataFrame 에서 연도별, 대륙별 기대 수명의 평균을 출력하여라
# df.groupby(year).mean(lifeExp)
df_by_year2 = df.groupby(['year','continent'])
print(df_by_year2)
print(df_by_year2['lifeExp'].mean())

# 1차원 데이터를 series라고 부르고, series 의 집합이 데이터 프레임이 된다

# 연도별 기대수명 그래프
year_lifeExp = df.groupby('year')['lifeExp'].mean()
plt.plot(year_lifeExp)
plt.title('lifeExp by year')
plt.show()

# 선생님 파일에서는 내 파일의 df가 gapminder로 설정되어 있다

# 연도별 전세계 인구수 그래프
year_pop = df.groupby('year')['pop'].sum()
print(year_pop)
plt.plot(year_pop)
plt.title('pop by year')
plt.show()

