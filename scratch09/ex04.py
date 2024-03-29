"""
pandas 패키지를 사용한 csv 파일 읽기
"""
import os
import matplotlib.pyplot as plt
import pandas as pd

file_path = os.path.join('..','scratch08', 'mpg.csv')
df = pd.read_csv(file_path)
print(df) # R스럽게 csv를 출력해주었다!
print(df.head(7)) # by default, 첫 5개의 데이터를 출력해준다
print('shape:', df.shape) # shape: (234, 11) 234개의 행, 11개의 컬럼 # 관측치: 234개 변수 11개
print('types:', df.dtypes) # returns the data type of each column
# In normal Python setting, csv.reader does not automatically convert string to number; the developer has to do it
# But when we import pandas; no hace falta a convertirlo, lo se hace automaticamente(?)
# DataFrame.dtypes: 각 컬럼(변수)의 데이터 타입
# Pandas의 데이터 타입: object(문자열), float(실수), int(정수)
print(df.describe()) # 기술 통계 요약 통계량/ returns the statistics of df

# df['colname']: DataFrame에서 특정 컬럼의 모든 데이터를 선택
# 예) displ 만 뽑아내고 싶다면:
displ = df['displ']
print(displ)

cty = df['cty']
print(cty)
# scatter plot of displ & cty
plt.scatter(displ, cty)
# plt.show()

# 행으로 읽어오고 싶은 때

print(df.loc[0]) # 한 행에 대한 정보다 가득^8^! # 행 하나 추출
print(df.iloc[0])
print(df.iloc[0:3]) # 쪼개서보기 쌉가능~ *-*!!  # row index 0 이상 3 미만인 행 선택

# loc 와 iloc 는 차이가 있다; dataframe 에서 행을 선택 할 때,
# df.iloc[행번호/인덱스], df.loc[행 레이블]
# iloc -> loc for location; i se significa index (i 번째 location) 그래서 숫자만 주세요
# loc -> 원래는 레이블을 붙이는데, 여기는 레이블이 따로 없으니까 그냥 해줌 (파이썬 자동생성 -> 숫자레이블)
    # like row.names
# 행이름이 없는 경우도 많은데, 판다스는 데이터 프레임을 생성할적에 모든 프레임에 이름을 준다 -> 인덱스 자체를 레이블로 자동으로 만들어줌

# 행번호보다 컬럼을 선택을 더 많이 함

# 데이터 프레임에서 여러개의 컬럼(변수)들을 선택
print(df[['displ','cty','hwy']])
        # [<- index 연산자[<- 리스트 기호]]
# is the same as
cols = ['displ','cty','hwy'] #[] -> list
print(df[cols]) # []: index operator

# 데이터 프레임에서 여러개의 행(관측값)과 컬럼(변수)들을 선택
print(df.loc[0:3, cols])
# 여기서 iloc 를 쓰면 에러가 난다 -> 컬럼의 이름들은 문자열이니까 iloc 는 못 쓴다 (iloc는 index -> 숫자만 가능!)
# df.loc[행의 이름/레이블, 컬럼의 레이블]
# loc에서는 마지막 인덱스가 포함이다! (오잉 ㅇㅅㅇ????) 왜냐하면 loc는 행과 열의 이름이니까, 이름을 다 invoke 해주는 것

# df.loc[row_labels, col_labels]
# df.iloc[row_indices, col_indices] # 근데 여기는 인덱스니까, 파이썬의 원래 룰 처럼 -1 한 만큼의 값을 리턴
print(df.iloc[0:3,0:3])











































