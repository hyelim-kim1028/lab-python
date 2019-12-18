from functools import reduce

import pandas as pd
import numpy as np
import cx_Oracle
from scratch09.ex10 import select_all_from

def peak_to_peak(x):
    return x.max() - x.min()
    # 같은 파일에 있을 때는 그냥 함수이름만 불러와서 사용
    # 다른 파일에서 사용할 때는 임포트한게 이름이 된다

if __name__ == '__main__':
    # with-as 구문을 사용해서 Oracle DB 서버에 접속
    dsn = cx_Oracle.makedsn('localhost', 1521, 'orcl')
    with cx_Oracle.connect('scott', 'tiger', dsn) as connection:
        # with-as 구문을 사용해서 cursor 객체를 생성
        with connection.cursor() as cursor:
            #scratch09 패키지에서 작성한 테이블 전체 검색 함수를 사용해서,
            #emp_df 데이터 프레임을 생성
            emp_df = select_all_from('emp', cursor)
            #emp_df를 csv파일로 저장
            emp_df.to_csv('emp_df.csv', index = False) # index = False (removes the row_index on csv file)
            # group_by
            # emp_df에서 부서별 평균 급여를 출력해보세요 (group by  deptno and sal.mean())
            print('\n Get the avg SAL grouped by DEPTNO ')
            grouped1 = emp_df.groupby('DEPTNO')
            grouped1_sal_mean = grouped1['SAL'].mean()
            print(grouped1_sal_mean)
            # emp_df에서 부서별 인원수를 출력해보세요
            print('\n # of employees by DEPTNO')
            grouped1_count = grouped1['EMPNO'].count()
            print(grouped1_count)


            # emp_df에서 부서별 급여 최소값 출력
            print('\n min SAL per DEPTNO')
            grouped1_sal_min = grouped1['SAL'].min()
            print(grouped1_sal_min)
            # emp_df에서 부서별 급여 최댓값을 출력
            print('\n max SAL per DEPTNO')
            grouped1_sal_max = grouped1['SAL'].max()
            print(grouped1_sal_max)
            # 위의 결과를 하나의 데이터 프레임을 출력
            # Trial 1
            # I wanted to do it at once, but concat does not give a result I wanted (concat is a row_merger)
            # grouped1_data_frames = [grouped1_sal_mean, grouped1_count, grouped1_sal_min, grouped1_sal_max]
            # emp_df_deptno = pd.concat(grouped1_data_frames)
            # print(emp_df_deptno)

            #Trial 2 UN EXITO!
            # This is not my code, this is a copied one. I have to study for this
            grouped1_data_frames = [grouped1_sal_mean, grouped1_count, grouped1_sal_min, grouped1_sal_max]
            df_merged = reduce(lambda left, right: pd.merge(left, right, on=['DEPTNO']), grouped1_data_frames)
            print(df_merged)

            # Teacher's Solution 1
            df = pd.DataFrame({
                'count':grouped1_count,
                'mean':grouped1_sal_mean,
                'min': grouped1_sal_min,
                'max':grouped1_sal_max
            })
            print(df)
            print(df.shape)

            # Teacher's Solution2: aggregate() or agg()
            # can apply multiple functions at once
            # 파라미터에 함수 이름을 전달하면, groupby 객ㅊ에 함수를 적용한다
            df = grouped1.agg(['count','mean','min','max'])
            print(df)
            # group by = grouped1
            # 함수이름을 '' 로 적용하는 경우는: 함수가 집계 함수인 경우 (Pandas.Series 또는 Pandas.DataFrame 클래스가 가지고 있는 메소드인 경우)
            # i.e. 가지고 있는 메소드들: count, mean, sum, ... 인 경우에는 함수 이름을 문자열로 전달한다
            # 개발자가 작성한 함수는 함수 이름을 파라미터에 전달함
            # print(grouped1.agg(mean)) # mean() 이라는 함수 이름을 못 찾음
            print(grouped1.agg(pd.Series.mean)) # 이게 진짜 mean() 함수가 있는 곳 -> 그래서 판다스 개발자가 편의상 'mean' 이렇게 넣으라고 배려해준거야 *0*!! 친절친절
            # 우리가 함수를 만들어 사용할 때는 원래 이런 방식 (agg(pd.Series.mean)을 써줘야한다 -> 예) def peak_to_peak

            #EXAMPLE
            # print(grouped1.agg('mean')) 코드와 같은 편의 기능 있음
            # peak_to_peak()함수는 편의의 대상이 아니다
            # df = grouped1.agg(['count', 'mean', 'min', 'max','peak_to_peak'])
            # Error: AttributeError: 'SeriesGroupBy' object has no attribute 'peak_to_peak'
            # 'SeriesGroupBy' object where Python finds the function
           #so this is what we do:
            df = grouped1.agg(['count', 'mean', 'min', 'max',peak_to_peak])
            print(df)

            # keyword-argument 로 넘길수도 있다/ 컬럼 이름들이 함수이름들로 표시가 되었다
            # lambda 를 넣어도 된다
            print(grouped1.agg(['count', 'mean', 'min', 'max',
                               lambda x: x.max() - x.min()]))



            # # emp_df에서 직책별 직원 수, 급여 평균, 최소, 최댓값을 출력
            # grouped2 = emp_df.groupby('JOB')
            # print(grouped2['EMPNO'].count())
            # print(grouped2['SAL'].mean())
            # print(grouped2['SAL'].min())
            # print(grouped2['SAL'].max())
            #
            # # can also use aggregate:
            grouped_by_job = emp_df.groupby('JOB')
            sal_by_job = grouped_by_job['SAL']
            print(sal_by_job.agg(['count','mean','min','max',peak_to_peak]))
            # agg() 함수가 만드는 dataframe의 컬럼 이름을 설정할 때는 keyword-argument 방식 또는 dict를 파라미터로 전달함
            print(sal_by_job.agg(Count='count', Average='mean', Minimum='min', Maximum='max',
                               Range=lambda x: x.max() - x.min()))
            #
            # # 위의 모든 작업을 매니저별로 수행
            # grouped3 = emp_df.groupby('MGR')
            # print(grouped3['EMPNO'].count())
            # print(grouped3['SAL'].mean())
            # print(grouped3['SAL'].min())
            # print(grouped3['SAL'].max())
            # # emp_df에서 부서별, 직책별, 직원수, 급여, 평균, 최소, 최댓값 출력
            # grouped4 = emp_df.groupby(['DEPTNO','JOB'])
            # print(grouped4['EMPNO'].count())
            # print(grouped4['SAL'].mean())
            # print(grouped4['SAL'].min())
            # print(grouped4['SAL'].max())
            grouped = emp_df.groupby(['DEPTNO',"JOB"])
            sal_by_dept_job = grouped['SAL']
            df = sal_by_dept_job.agg({
                'count':'count',
                'Average':'mean',
                'minimum':'min',
                'maximum':'max',
                'range': lambda x: x.max() - x.min()
            })

            print(df)
