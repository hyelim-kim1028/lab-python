import pandas as pd
import numpy as np

def squares(x):
    return x ** 2

def doubles(x):
    return x * 2

# list  에도 적용이 된다

if __name__ == '__main__':
    result1 = squares(3)
    result2 = doubles(3)
    print('array = ',result1, result2)

    array = np.array([1,2,3])
    result1,result2 = squares(array), doubles(array)
    print(f'squares = {result1} \ndoubles = {result2}')

    # Python's list 의 *2 는 리스트 자체를 두번 반복, 하지만 numpy 에서 * 2는 각 원소들을 2배씩 곱해준 것
    # squares 는 각 원소들을 제곱해준것

    df = pd.DataFrame({
        'a':[1,2,3],
        'b':[4,5,6]
    })
    print(df)
    # a와 b는 컬럼의 이름이고, 컬럼으로 들어간다
    print(squares(df))
    print(doubles(df))
    # numpy의 array를 기준으로 각 원소들마다 **2 (제곱)으로 적용이 된다
    # 우리가 만든 함수가 모두 적용이 된다
    # 리스트의 리스트로 만들었다면 적용되지 않는다

    # 비교해보기 위해서 리스트의 리스트를 만들어서,
    a = [[1, 4], [2, 5], [3, 6]]
    # print(squares(a))
    # print(doubles(a))
    # occurs an error: TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'

    # 우리가 만든 함수를 데이터 프레임에 적용
    result = df.apply(squares, axis = 1)
    print(result)
    # apply: Superficially, the data frame is transmitted to a function and calculated
    # Que esta pasando en dentro: 데이터 프레임의 행 또는 열을 함수의 매게변수로 줘서 계산해준다
    print(np.sum([1,2,3]))
    result = df.apply(np.sum, axis = 0)
    print(result)
    # df의 각 컬럼별 모든 컬럼들을 더해준 값을 리턴해준다

    print(np.sum([1, 2, 3]))
    result = df.apply(np.sum, axis=1)
    print(result)
    # Each sum is calcuated for its sum
    # 판다스가 가지고 있는 데이터 프레임에는:
    # DataFrame.apply(function, axis)
    # axis = 0: apply function to each column
    # axis = 1: applied to rows

    # agg(aggregate)는 집게 함수들만 사용 가능
    # apply는 집계함수 이 외의 함수들도 사용 가능
    emp = pd.read_csv('emp_df.csv')
    print(emp.agg(np.mean)) # agg는 자기가 알아서 데이터 타입 = 숫자들을 찾아서 계산 (집계 함수는 숫자 타입을 컬럼만 자동으로 선택)
    # print(emp.apply(np.mean)) # apply는 그냥 다 넘겨버림, string도 그냥 넘겨서 집계함수를 사용하면, 에러가 나기도하고, 안나기도 한다
    # apply 함수는 모든 컬럼 또는 행을 함수의 파라미터에 전달하기 때문에, 집계 함수(mean, sum, ...) 가 제대로 동작하지 않을 수도 있음

