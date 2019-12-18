"""
file.readline() 사용해서 csv 파일 읽기
"""

import os

def my_csv_reader(fn: str, header = True) -> list:
    """
    csv 파일의 데이터를 2차원 행열 형태로 리턴
    # 행열: 행과 열을 가지고 있다! *-*
    # file exam.csv is a list of scores - which is also in form of list [1,30,84,17,61] * 10
    # In the beginning, these numbers/scores are in string type
    :param fn: 읽을 csv 파일 이름 (예: data\\exam.csv)
    :param header: csv 파일의 헤더 존재 여부
    :return: csv file 에서 헤더는 제외한 데이터들로 이루어진 2차원 리스트
    """
# for x in range(2, n):
    # ...         if n % x == 0:
    # ...             print(n, 'equals', x, '*', n//x)
    # ...             break
    file_name = os.path.join('data', 'exam.csv')
    print(file_name)
    if header == True:
        count = len(open(fn).readlines())
        with open(fn, mode='r', encoding='utf-8') as f:
            for line in f: #여기가 잘못된건 알겠는데 어떻게 해결하는지를 모르겠다
                                # i.e. list면 (1, len(list)) 라고 주잖아,, 근데 이건 뭐라고 줘야대?
                # if n == (line == ''):
                #     break
                 for line in range(1, count):
                    print(line.split())
            # underline on the split() because the integer cannot be separated using split (whatttt but they are characters)
                    if line == '':
                        break
    else:
        with open(fn, mode='r', encoding='utf-8') as f:
            for line in f:
                print(line.split())
                if line == '':
                    break

print(my_csv_reader('fn', header = True))
# now: how am I going to print it?

# but I did not make a code to read a file from the scratch,,,?
# print(my_csv_reader('exam.csv',header = True))

def print_data(data: list) -> None:
    """
    2차원 행렬 형태의 리스트를 출력
    1 10 20 30 40 
    2 11 21 31 41 
    이렇게 보여주는 함수 (줄 마다 \n)? 
    :param data: 2차원 행렬 형태의 리스트를 출력 
    :return: None  
    """
    # print f''
    # if header == True:
    #     for i in range(1,i):
    #         print(''\n)
    # else:
    #     for i in range(0,i):
    #         print(''\n)

def get_sum_mean(data: list, col: int) -> tuple: #(id, sum, mean)
    """
    주어진 2차원 리스트 (data)에서 해당 컬럼(col) 의 데이터들의 총합(sum)과 평균(mean)을 계산해서 리턴하는 함수

    :param data: 2차원 행렬 형태의 리스트
    :param col: 컬럼 인덱스 (0,1,2,..) (4까지 있음)
    :return: 컬럼 데이터의 합과 평균
    """
    # sum =
    # mean = sum/len(header?)
    # return (id, sum, mean)


if __name__ == '__main__':
    #작성한 함수들을 테스트
    pass






