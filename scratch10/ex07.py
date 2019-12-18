import numpy as np
import pandas as pd

# 각 그룹별로 치환하기 위해서 함수 만들기
def fill_group_mean(df):
    group_mean = df['data'].mean()
    print(group_mean)
    return df.fillna(group_mean)

if __name__ == '__main__':
    # Series 객체 생성
    s = pd.Series(np.random.randint(1, 10, 5))
    print(s) # 2줄이 반환되는데, 왼쪽은 인덱스, 오른쪽은 값이다
    s[3] = np.nan #원소 한개를 NA로 변경
    print(s)
    # df에 값이 안들어가 있는 경우가 종종있다
    # NA를 평균 값으로 대체하기 위해서, 평균으로 먼저 계산
    m = s.mean() #numpy, pandas의 집게 함수들은 NA를 제거하고 계산함
    print(m)
    # NA를 제외한 모든 값들을 더하고 그 값들의 len 만큼 나눈 값
    s = s.fillna(m) # 얘가 모든 NA들을 한꺼번에 다 바꿔준다
    print(s)

    df = pd.DataFrame({
        'province': ['서울', '경기', '충청', '전라', '강원', '경상', '부산'],
        'division': ['west'] * 4 + ['east'] * 3,
        # west = 서울, 경기, 충청, 전라, east = 강원, 경상, 부산
        # [ ] * n 은 리스트를 n만큼 늘린다는 뜻이고, 반복이다 + 는 파이썬 리스트의 더하기 이므로, 리스트들을 붙여준다
        'data': np.random.randint(1, 10, 7)
    })
    print(df)

    # 데이터 2개를 NA로 대체
    # df.iloc[0,2] = np.nan
    df.iloc[[0, 6], 2] = np.nan
            # [[list of two numbers] 대괄호 연산자->]
    print(df)

    # fill_group_mean() 호출
    # 데이터 프레임의 NA를 각 그룹별 평균으로 대체
    grouped = df.groupby('division') #DataFrameGroupBy 객체
    # GroupBy.apply(fn)는 함수 fn의 첫번째 파라미터에 dataframegroupby를 객체를 전달한다
    cleaned = grouped.apply(fill_group_mean)
    print(cleaned) # 부산은 3.5, 서울은 5.67 으로 division/west & east 별 평균을 구해서 NA를 대체해 주었다

    # 전 시간에서 했던 apply는 데이터 프레임의 어플라이 (컬럼/row를 함수의 파라미터로 준다)
    # 하지만 groupedby 의 apply는 함수에게 데이터프레임자체를 넘겨버린다
    # 그래서 함수도 dataframe을 가정하고 만들었다

































