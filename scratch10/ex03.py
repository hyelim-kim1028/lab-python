import pandas as pd 


if __name__ == '__main__':
    #csv file을 읽어서 파일에서 데이터 프레임을 생성 
    emp_df = pd.read_csv('emp_df.csv')
    print(emp_df.iloc[0:5])
    # 부서별, 직책별 직원수를 출력
    grouped_by_deptno_job = emp_df.groupby(['DEPTNO','JOB'])
    count_by_dept_job = grouped_by_deptno_job['EMPNO'].count()
    print(count_by_dept_job)

    #How teacher did it:
    grouped = emp_df.groupby(['DEPTNO','JOB'])
    emp_by_dept = grouped['EMPNO']
    result_df = emp_by_dept.agg('count')
    print(result_df)

    unstacked = result_df.unstack()
    print(unstacked.shape)
    # 원래의 df를 풀어해쳐서 자세하게 보여줌

    # grouping 기준이 되는 컬럼의 값들이 index(행의 이름)으로 사용되지 않고, 컬럼으로 사용하려면
    grouped = emp_df.groupby('DEPTNO', as_index=False)
    print(grouped['EMPNO'].count())
    #groupby 기준이 2개 이상이여도 똑같은 규칙이 적용된다
    grouped = emp_df.groupby(['DEPTNO','JOB'], as_index=False)
    print(grouped['EMPNO'].count())

