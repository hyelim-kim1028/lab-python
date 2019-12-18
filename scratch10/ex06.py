import numpy as np
import pandas as pd

def squared_mean(data):
    """ 데이터의 제곱의 평균을 리턴 """
    squared_sum = 0
    for x in data:
        squared_sum += x ** 2
    return squared_sum/len(data)

def my_func(x):
    """tuple을 리턴하는 함수"""
    return x.min(), x.max(), x.mean(), squared_mean(x)


if __name__ == '__main__':
    df = pd.DataFrame({ #2개의 파라미터 1) pop & income in {} 2) index
        'pop': np.random.randint(1,10,4),
        'income': np.random.randint(1,10,4),
    }, index = ['a','b','c','d']) # index = 행의 이름
    print(df)

    # agg()/aggregate() function: Data Frame의 축(axis)을 기준으로 통계량을 집계(aggregate)하기 위한 함수
    # 통계량(statistics): sum, mean, 분산(var), 표준편차(std), min, max, median, ...
    # agg함수는 집계가 목적이기 때문에 데이터 타입이 숫자 타입이 행/열에만 함수가 적용됨 (집계하려면 값이 여러개가 있어야한다)
    # agg 함수는 pandas(numpy)에서 제공하는 집계 함수들 이외에도 사용자 정의 함수를 사용할 수 있음. 단, 함수는 Series를 parameter에 전달하면
    # 숫자(스칼라)를 리턴하는 함수여야함 (여러개의 값을 사용하고 1개의 값을 리턴해준다) -> 어디에다가 적용? 데이터 프레임!
    print('=== agg by column(axis = 0) ===')
    print(df.agg('mean', axis=0)) # No difference returned even though axis = 0 were given or not
                                  # why column becomes a standard of calcuation? The same data are put in the same column
    print('=== agg by row(axis = 1) ===')
    print(df.agg('mean', axis = 1))
    #dataframe.agg('function', 'function') -> agg allows functions to be applied to the dataframe adjacent in the front
    #axis = 0 is calculated by columns, axis = 1 is calculated by rows
    # If a column is no in number type, agg automatically skips it

    # apply squared_mean
    print(df.agg(squared_mean)) # each column is given to the function as parameteres
    print(df.agg(squared_mean, axis = 1))

    # apply: DataFrame의 축(axis)를 기준으로 함수를 적용
    # 제약사항이 없다 (aggregate은 숫자만 리턴해야한다는 제약사항이 있다)
    # 적용하는 함수는 pandas 객체를 리턴하면 된다 (숫자만 리턴해야 한다는 제약사항이 없음)
    # 판다스 객체: data frame, series, 숫자/문자열(scalar - 값 1개만 리턴)
    # aggregate는 apply의 특수한 경우: agg() 숫자 타입 스칼라만 리턴하는 함수를 적용하는 apply()의 특수한 경우
    # apply()는 agg()보다 더 일반적으로 유연하게 사용할 수 있지만, 집게와 같은 특수한 목적인 경우에는 agg함수보다 성능이 느림

    print('=== apply by column (axis = 0) ====')
    print(df.apply('mean')) # the result of agg('mean') and apply('mean') are not from

    print('===apply by row (axis = 1)')
    print(df.apply('mean', axis = 1))

    # aggregate에서 사용가능한 함수들은 apply에서 사용 가능하다
    print(df.apply(my_func))
    print(df.agg(my_func)) # the agg() was able to return my_func => ???

    # groupby에 있는 apply













































