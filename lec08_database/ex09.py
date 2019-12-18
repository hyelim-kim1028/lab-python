"""
ex_09
1) emp table 에서 부서 번호를 입력 받아서 해당 부서의 직원들의 사번, 이름, 부서번호 출력
select empno, ename, deptno from emp where deptno == input(deptno)

2) emp 테이블에서 사원이름을 입력 받아서 해당 글자가 이름의 포함된 직원들의 사번, 이름, 부서번호, 급여 출력
select empno, ename, sal from emp where ename = '%(a letter from):ename%' -> 이걸 어떻게 해주지
"""
import cx_Oracle
import lec08_database.oracle_config as cfg

# 1.
with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as connection:
    with connection.cursor() as cursor:
        sql1 = '''select empno, ename, deptno
                  from emp
                  where deptno = :deptno '''
        # ''' 줄을 바꿔도 괜찮아요 '''
        dept_no = int(input('Enter the deptno>> '))
        cursor.execute(sql1, deptno = dept_no)
        # for row in cursor:
        #             print(row)
        # return the values in tuple format
# we can also write it this way:
        for empno, ename, deptno in cursor:
            print(empno, ename,deptno)
            # returns the values in a separated form but not a tuple
            # 성분 분해 (unpack the components)

 #2번 이어서
        print('===================')

        sql2 = ''' select empno, ename, sal 
                   from emp 
                   where upper(ename) like :keyword 
        '''
        # :keyword (or any value) since we do not know which would come
        name = input('검색할 이름 입력>> ')
        name = name.upper()  # give upper or lower () to equalize the format
                             # 입력한 문자열을 대문자로 변환
        name = '%' + name + '%' # where 구문에서 like 사용하려고
        cursor.execute(sql2, keyword = name)
        for empno, ename, sal in cursor:
            print(empno, ename, sal)

# 1번의 나의 고뇌의 흔적들:
#         sql_select = 'select empno, ename, deptno from dept2 where deptno == :deptno'
#         for row in cursor.execute(sql_select, deptno == deptno):
#             print(row)
        # cursor.execute(sql_select,
        #                deptno=deptno)
        # for row in cursor:
        #     print(row) # 음 어디서의 문제일까
        # 출력하는 값이고 변경하는 값이 아니라 empno, ename, deptno 는 : 를 안주고, for 구문을 사용해서 출력하려고 하는데 생각처럼 되지 않는다
        # question: where should I give the variables that was not inserted but has to be executed?!
        # but i don't think using the for loop is an answer (confused)

#2)
# with cx_Oracle.connect(cfg.user) as connection:
#     with connection.cursor() as cursor:
#         sql2 = 'select empno, ename, sal from dept2 where ename = :%ename%'
#         ename2 = input('Enter the name of an employee>> ')
#         cursor.execute(sql2, ename = ename2)
#         for row in cursor:
#             print(row)


# 2번을 향한 나의 고뇌의 흔적:
#         for row in cursor.execute(sql_select2, ename = ename):
#             print(row)
        # cursor.execute(sql_select2,
        #                ename = ename)

        