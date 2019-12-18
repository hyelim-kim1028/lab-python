"""
pandas groupby, aggregate, apply
"""
import numpy as np
import pandas as pd

# 데이터 프레임 생성
df = pd.DataFrame({
    'key1':['a','a','b','b','a'],
    'key2':['one','two','one','two','one'],
    'data1':np.random.randint(0,10,5),
    'data2':np.random.randint(0,10,5) #low, high, size
})
print(df)
# key 1을 사용해서'a'와 'b'로, key 2 를 사용해서 'one' 과 'two' 로 묶을 수 있다

# cursor를 함수나 비슷한 것에 ctrl + q를 하면 상세설명을 누를 수 있는데,
# 다시 한번 ctrl+q를 하면 옆에 새로운 페이지를 생성해서 설명을 보여주고,
# 그 상태에서 또 crtl + q 를 누르면 페이지가 사라진다

grouped1 = df.groupby('key1')
print(grouped1) # DataFrameGroupBy 객체
# 'a'와 'b'로 분리를 해놓은 객체이다
# (임시 데이터 프레임 객체이고 우리가 원하는 기준으로 데이터 프레임을 쪼개놓은 객체이다)
# 다시 말하면 그룹 연산을 적용하기 위해 만든 객체
# (평균, 최솟/댓값 찾기 등 여러개가 있어야 적용을 할 수 있는 연산들을 그룹 연산이라고 일컫는다)
# 함수를 적용해서 사용한다
# 그룹연산: count, sum, mean, median, var, std, min, max 등등

cnt = grouped1['data1'].count()
print(type(cnt))
print(cnt)

print(cnt['a'], cnt['b'])
print(grouped1['data1'].mean())
print(grouped1.mean())
# when we dont specify column, mean is applied to all columns in a table
# mean() is only workable in columns with data type number
# (the function automatically finds number data types and ignores string columns)

print(grouped1[['data1','data2']].mean())

# 행으로 뽑을 때는 loc & iloc[] 를 사용
# 컬럼은 df['data1'] or df[['data1','data2']]을 사용!

grouped2 = df.groupby('key2')
print('grouped2 = ',grouped2.mean())

# groupby는 한가지 이상의 변수에 관해서도 적용가능하다
# groupby의 기준(by)이 2개 이상의 컬럼이때는 리스트를 전달하면 됨.
grouped3 = df.groupby(['key1','key2'])
print(grouped3.count())
print(grouped3.mean())
print(grouped3['data1'].count())

people = pd.DataFrame(np.random.randint(0,10, (5,5)), # gave a tuple (5,5) in parameter 'size'
                                                      # (5,5) = (nrow,ncol) = creates 25 random numbers
                      columns = ['a','b','c','d','e'], # 컬럼에다 이름을 준다
                      index = ['Joe','Steve','Wes','Jimmy','Travis']) # 행에 이름을 준 것
print(people)
print(people.groupby(len).sum())
print(people.groupby(lambda x: x.startswith('J')).sum())


