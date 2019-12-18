"""
pandas 데이터 타입
series 1차원 리스트. 인덱스가 한 개만 갖음.
DataFrame: 2차원 리스트, 인덱스가 행과 열 두개를 갖음
"""
import pandas as pd
import numpy as np

a = pd.Series([1, 3, 5, np.nan, 6, 8])
print(type(a)) # <class 'pandas.core.series.Series'>
# Series 라는 클래스 (데이터와 기능을 한꺼번에 가지고 있는 데이터 타입)
print(a) # 인덱스 + 데이터출력

# Series 에서 특정 인덱스의 아이템 선택 : Series[index]
print(a[0]) #a[0]의 데이터 타입: float64
# 인덱스 연산자([]) 안에서 번위 연산자를 사용할 수도 있음
print(a[0:3]) # 데이터 타입: series
# 인덱스 연산자 ([]) 안에서 리스트 연산자([])를 사용할 수도 있음
# print(a[0,2,4]) #이건 안됨, 시리즈는 인덱스 1개가 오는 것
print([[0,2,4]]) # 데이터타입: 시리즈

# dict 타입의 데이터에서 DataFrame 생성
df = pd.DataFrame({
    'no':[3,13,23],
    'name': ['김영광', '이은지', '조유경'],
    'gender': ['M','F','F']
})
print(df)

#2차원 리스트 타입([...],[...],[...])의 데이터에서 데이터 프레임 Data Frame을 생성
students = pd.DataFrame([
    [4, '김재성', 'M'],
    [14, '이재경', 'M'],
    [24, '조지원', 'F']
],columns = ['번호', '이름', '성별'])
print(students)
# 모양 그대로 데이터 프레임을 만드는 방법
# 컬럼에 이름을 따로 줄 수 있다

# students.columns = ['번호', '이름', '성별']
# print(students)
# # 컬럼에 이름이 들어가있다

# dictionary 는 키값을 바로 줄 수 있고, 키값이 행이 아니라 컬럼이라는 것을 주의해야한다
# 리스트에서는 컬럼에 이름을 줄 수 있는 방법이 없기 때문에 데이터 프레임을 만든 다음에 컬럼 속성을 변화하거나
# 데이터 프레임 함수에 보면 컬럼즈 property 함수에 직접 넣어주는 것

# DataFrame.iloc[row_index, column_index]
print(students.iloc[0,0]) # 행 번호 = 0, 컬럼도 = 0 의 아이템
print(students.iloc[0, 0:3]) # 0 번 row, 0,1,2 컬럼에 있는 아이템
print(type(students.iloc[0, 0:3])) # Series
# 출력형태를 보고 serires 인가 data frame 인가를 알아볼 수 있도록 해야한다

print(students.iloc[0:2, 0:2]) #data frame (부분집합)을 리턴
print(students.iloc[:, 1:3]) # 학생들 번호만 빠지고 모든 행을 리턴하였다 (범위연산자 : 앞뒤로 모두 빠지면 모든 행을 가리킨다)
print(students.iloc[1:3,:]) #범위 연산자만 사용하면 모든 행 또는 열
 # 훈련세트와 검증세트를 나눌 때 사용 가능가능 *0*!
 # 모든 컬럼을 선택하는 경우에는 아예 컬럼 자체를 생략해도 된다
print(students.iloc[1:3])
#앞은 생략하면 안된다
# print(students.iloc[,1:3]) # 안된다

#boolean indexing
# DataFrame[[boolean들의 리스트]] : 리스트에서 True인 값의 인덱스를 행 인덱스로 선택
print(students[[False, True, False]])
    #데이터프레임 이름 [인덱스] -> 인덱스로 찾겠다
    #행번호/ 이름을 리스트로 주겠다
    # 이 인덱스 연산자는 True에 매칭 되어있는 것만 반환해줌
condition = students['성별'] =='M'
print(condition) #[True, True, False]
print(students[condition])
print(students[students['성별'] == 'F'])
# 불리언 연산자 원리: 인덱스연산자 안에다가 불리언들의 리스트를 줘서 참인 인덱스만 df의 행에서 뽑아주는 것

# 옆으로 붙이는 것: join
# 아래로 붙이는 것: concat

# 데이터 프레임 이어 붙이기: concat
students.columns = ['no','name','gender']
print(students)

stu_df = pd.concat([df, students])
print(stu_df)
# index가 이상하다 -> 이건 인덱스가 아니라 레이블이라 그냥 붙여준 것, 레이블이 겹친다고해서 새로 인덱싱해주지 않는다
print(stu_df.iloc[0])
print(stu_df.loc[0])

stu_df2 = pd.concat([df,students], ignore_index=True)
print(stu_df2)

# 의미없는 중복되는 인덱스를 굳이 남겨둘 필요는 없다! 그럴때 사용하는 파라미터: ignore_index

#DataFrame.sort_values(정렬 기준 컬럼 이름)
#stu_df2 를 번호 순서대로
print(stu_df2.sort_values('no'))
print(stu_df2.sort_values('gender'))

# 두 개 이상의 조건으로 boolean indexing 하는 방법
cond1 = stu_df2['no'] % 2 == 1 # no 컬럼의 값이 홀수이면
print(cond1)
# [T,T,T,F,F,F]
cond2 = stu_df2['gender'] == 'F' #gender 컬럼의 값이 'F'이면
print(cond2)
#[F,T,T,F,F,T]
subset = stu_df2[cond1 & cond2] # & 연산자가 원소별로 & 되게해주는 (같은 비트, 성분들 끼리 연산해준다 해서 bit-wise operator 이라고 불름)
# boolean 인덱싱에서는 and, or 연산자는 사용할 수 없고, 각 성분별로 연산을 하는 bitwise 연산자 (&, |) 를 사용해야 함!
print(subset)













