
import cx_Oracle
import pandas as pd

def get_column_names_of(table, cursor):
    # sql = f"""select column_name from user_tab_columns
    #                 where table_name = '{table.upper()}'
    #                 order by column_id"""
    # cursor.execute(sql)

    #other way of doing it (lines 8-11) -> Data Binding:
    sql = """select column_name from user_tab_columns 
    where table_name = :tbl_name
    order by column_id"""
    # not a formatted string/ table name is not bound with ''
    cursor.execute(sql, tbl_name=table.upper())
    # Data Binding 방식 이라고 부른다
    # cursor가 sql문장의: 변수 위치에 데이터 타입에 맞게끔 값을 치환해 줌.
    # SQL 문장이 완성되야 커서가 시작할 수 있기 때문에 : 라는 완성되지 않은 변수를 주고, 커서는 :을 찾아가고,
    # 그 위치에 데이터 타입에 맞게끔 ('')이 없어도 값을 치환해 준다
    # 값이 문자열이면 '문자열' 형태로 : 변수 위치에 치환됨.
    col_names = [row[0] for row in cursor]
    return col_names
    # for row in cursor:
    #     print(row[0]) # returned values are tuples with one component (we want to eradicate ',')
                      # -> so we added [0] -> returned the first values in the tuple
                      #(anyway there was only one component for each pairs of parenthesis)

def  select_all_from(table, cursor):
    # sql = f'select * from {table.upper()}'
    # # from 구문에서 테이블 이름은 ''로 감싸면 안되기 때문에
    # # data binding 방식을 사용할 수 없다.
    # cursor.execute(sql)
    # # 이 행들/튜플/을 리스트로 만들어서 데이터 프레임에 넣는 방법 1
    # data = cursor.fetchall() # returns a list # data = [row for row in cursor]
    # data_frame = pd.DataFrame(data)
    # # 테이터 프레임에 컬럼 이름을 설정
    # data_frame.columns = get_column_names_of(table, cursor)
    # return data_frame

    # sql = f'select * from {table.upper()}'
    # cursor.execute(sql)
    # # data = cursor.fetchall() # devolver un list
    # data_frame = pd.DataFrame(cursor.fetchall(),
    # columns = get_column_names_of(table, cursor))
    # 컬럼이름만 가지고 있는 커서 # 위의 커서와 아래 커서는 다르다
    # # cursor, #빈 데이터 프레임 -> cursor is only executed once,
    # when it reaches the last point, cursor had been consumed,
    # therefore does not return anything
    # return data_frame
    # why does it return an empty index???

    # def select_all_from(table, cursor):  # 함수를 정의할때 선언하는 변수 - 파라미터
    #     select_insert = f"""select * from {table.upper()}"""
    #     cursor.execute(select_insert)
    #     # from 옆에 table 있는 경우는 formative string(f'')을 쓸 수 밖에 없다 (data binding nono)
    #     # why? 문자열은 '' 주어야 하는데, execute()안에 들어가는 select 문은 ''가 이미 존재함 (또 ''로 감쌀 수 없음)
    #     # t = [row for row in cursor] # cursor는 oracle의 datatype을 python의 datatype으로 변환시켜준다 (ex. hiredate의 type변환)
    #     t = cursor.fetchall()  # cursor의 list를 리턴해주는 함수
    #     table_body = pd.DataFrame(t)
    #     table_body.columns = get_column_names_of(table, cursor)
    #     return table_body

# 이것도 가능!! *0*
    sql = f'select * from {table.upper()}'
    cursor.execute(sql)
    data_frame = pd.DataFrame(cursor)
    data_frame.columns = get_column_names_of(table, cursor)
    return data_frame

    # attempt 1 _ Not at all close
    # file_path = f'{table}.csv'
    # table = pd.read_csv(file_path)
    # return table

# 나는 이렇게 했다 -> 아니었다
# def select_salgrade_c(sal, table, cursor):
#     new_table = table[0:n] + table['salgrade']
#     sql = f'select grade from {table.upper()}'
#     cursor.execute(sql)
#     # DataFrame['colname'] = list, pandas.Series
#     # emp_df에 salgrade 컬럼을 추가
#     # emp_df['sal'] 개수만큼 반복:
#     # 선택한 sal값이 salgrade_df 어느 grade 에 속하는지를 찾음
#     for i in range(len(new_table)):
#         if sal >= 700 and sal <= 1200:
#             return sal == 1
#         elif sal > 1201 and sal <= 1400:
#             return sal == 2
#         elif sal >= 1401 and sal <= 2000:
#             return sal == 3
#         elif sal >= 2001 and sal <= 3000:
#             return sal == 4
#         else:
#             return sal == 5

    # -> salgrade_df의 행 개수만큼 반복하면서 LO, HI와 비교
    # -> DataFrame.iterrows() 함수 이용

if __name__ == '__main__':
    # 오라클 데이터 베이스 서버와 접속
    dsn = cx_Oracle.makedsn('localhost',1521, 'orcl')
                        # local host = IP 주소를 줘도 된다 (언제 사용? 내게 오라클이 없고, 사용해야할 때 다른 컴퓨터에 접근해서 사용)
                        # localhost = 같은 PC에서 돌고 있다
    with cx_Oracle.connect('scott','tiger',dsn) as connection:
        #Cursor 객체 생성
        with connection.cursor() as cursor:
            emp_columns = get_column_names_of('emp', cursor)
            # get_column_names_of 라는 함수가 있었으면 좋겠다 (테이블 이름, 커서 -> select 문장 같은 것 사용가능)
            print(emp_columns) # 리스트['empno', 'ename' ... ]

            emp_df = select_all_from('emp', cursor) #DataFrame
            print(emp_df)

            dept_df = select_all_from('DEPT', cursor)
            print(dept_df)

            salgrade_df = select_all_from('salgrade', cursor)
            print(salgrade_df)

            # How teacher did it
            # DataFrame에 새로운 컬럼을 추가
            # DataFrame['colname'] = list, pandas.Series
            # emp_df에 salgrade 컬럼을 추가
            # emp_df['sal'] 개수만큼 반복:
            sal_grade = []  # 급여 등급을 저장할 list -> 비어있는 배열을 선언
            for sal in emp_df['SAL']:
               # 선택한 sal값이 salgrade_df 어느 grade 에 속하는지를 찾음
            # -> salgrade_df의 행 개수만큼 반복하면서 LO, HI와 비교
            # -> DataFrame.iterrows() 함수 이용: 데이터 프레임의 (행 이름, 행)을 튜플 반복문 안에서 사용할 수 있게 해줌
                for name,row in salgrade_df.iterrows():
                #print(name, row)
                # 프린트를 name 이나 row만 해주면 -> 변화를 쉽게 알 수 있다
                # iterrows 가 행의 이름과 행 자체를 리턴해준다
                #  we could also put it like: for x in salgrade_df.iterrows(): print(x)
                # but x is an tuple of (행 이름, 행) -> therefore we have to put it like if x[1]['LOSAL']
                # That was why we decoded x into name, row above ^0^  -> 가독성 업업
                 if row['LOSAL'] <= sal <= row['HISAL']:
                    # 급여 등급을 찾은 경우, 리스트에 추가
                    sal_grade.append(row['GRADE'])
                    break # 반복문을 반복하지 않도록 break 해준다

                    # with, function, for, while loop 공부

            emp_df['SAL_GRADE'] = sal_grade # DF에 새로운 컬럼을 추가
            print(emp_df)

# 컬럼별로 반복도 가능가능

# SQL join - pandas.merge
        emp_dept = pd.merge(emp_df, dept_df, on = 'DEPTNO')
        print(emp_dept)

# pandas.merge(left,right, how, on, left_on, right_on ...)
        # left, right: 조인할 데이터 프레임
        # how: 조인 방식 (inner, left, right)
        # on: 조인할 때 기준이 되는 컬럼 이름
        # left_on : 왼쪽에 있는 컬럼 이름, right_on: 오른쪽에 있는 컬럼 이름
        # 조인의 기준이 되는 커럼 이름이 데이터 프레임마다 다르면,
        # left on = 'left 데이터 프레임 컬럼', right on = 'right DF column'

        # emp_df, dept_df 데이터 프레임의 left, right join 결과 비교

        print('\n left join')
        emp_dept = pd.merge(emp_df, dept_df,how = 'left', on='DEPTNO')
        print(emp_dept)
        # left join returns the same result as inner join

        print('\n right join')
        emp_dept = pd.merge(emp_df, dept_df,how = 'right', on='DEPTNO')
        print(emp_dept)
        # right join has one more row

        # self join/ emp table 에서 mgr & empno 가 일치하는 join을 만들어라
        # 1) inner 2) left 3) right join
        # I cant figure out what to give on 'on' parameter
        print('\n self join - inner')
        emp_dept = pd.merge(emp_df,emp_df, how='inner', left_on= 'MGR', right_on= 'EMPNO')
        print(emp_dept)

        print('\n self join - left')
        emp_dept = pd.merge(emp_df, emp_df, how='left', left_on='MGR', right_on='EMPNO')
        print(emp_dept)

        # why I kept on getting errors: I put 'colnames' (i.e. MGR, EMPNO) in lowercase letters

        print('\n self join - right')
        emp_mgr_right = pd.merge(emp_df, emp_df, how='right', left_on='MGR', right_on='EMPNO')
        print(emp_mgr_right)
        # 판다스에서는 merge해두고, 필요한 컬럼들은 [] 인덱스를 사용해서 뽑아서 쓴다
        print(emp_mgr_right[['EMPNO_x', 'ENAME_x','MGR_x', 'EMPNO_y','ENAME_y']])
