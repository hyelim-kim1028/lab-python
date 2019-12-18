import cx_Oracle
import pandas as pd

def get_column_names_of(table, cursor):
    sql = """select column_name from user_tab_columns
            where table_name = :tbl_name
            order by column_id"""
    cursor.execute(sql, tbl_name = table.upper())
    col_names = [row[0] for row in cursor]
    return col_names

def select_all_from(table, cursor): #함수를 정의할때 선언하는 변수 - 파라미터
    sql = f'select * from {table.upper()}'
    cursor.execute(sql)
    data_frame = pd.DataFrame(cursor)
    data_frame.columns = get_column_names_of(table, cursor)
    return data_frame

if __name__ == '__main__':
    # 오라클 데이터 베이스 서버와 접속
    dsn = cx_Oracle.makedsn('localhost', 1521, 'orcl')
            # local host = IP 주소 (local host 는 같은 PC에서 돌고 있는 것)
    with cx_Oracle.connect('scott','tiger',dsn) as connection:
        with connection.cursor() as cursor:
            emp_df = select_all_from('emp', cursor) # Dataframe
            print(emp_df)

            dept_df = select_all_from('DEPT', cursor)
            print(dept_df)

            salgrade_df = select_all_from('salgrade', cursor)
            print(salgrade_df)

            # add a new column on a data frame
            # DataFrame['colname'] = list, pandas.Series
            # emp_df에 salgrade 컬럼을 추가
            # emp_df['SAL'] 갯수만큼 반복
            sal_grade = [] # Create an empty list to add the grades
            for sal in emp_df['SAL']: # to find out which salgrade the chosen sal belongs
                for name, row in salgrade_df.iterrows():
                    #Iterate over DataFrame rows as (index, Series) pairs.
                    # that was why we were able to to decode x into name, row
                    if row['LOSAL'] <= sal <= row['HISAL']:
                        sal_grade.append(row['GRADE'])
                        break
            emp_df['SAL_GRADE'] = sal_grade
            print(emp_df)

    emp_dept = pd.merge(emp_df, dept_df, on = 'DEPTNO')
    print(emp_dept)

    # JOIN 부분부터!
    print('\n left join')
    emp_dept = pd.merge(emp_df, dept_df, how='left', on='DEPTNO')
    print(emp_dept)

    print('\n right join')
    emp_dept = pd.merge(emp_df,dept_df, how='right',on = 'DEPTNO')
    print(emp_dept)

    print('\n self-inner')
    emp_dept = pd.merge(emp_df,emp_df,how='inner',left_on = 'MGR', right_on = 'EMPNO')
    print(emp_dept)

    emp_dept = pd.merge(emp_df, emp_df, how = 'right', left_on = 'MGR', right_on = "EMPNO")
    print(emp_dept)

    emp_dept = pd.merge(emp_df, emp_df, how = 'left', left_on = 'MGR', right_on = 'EMPNO')
    print(emp_dept)