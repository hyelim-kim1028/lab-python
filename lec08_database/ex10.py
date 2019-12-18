"""
ex08.py
emp, dept 테이블에서 부서 번호를 입력 받아서 해당 부서 사원의 사번, 이름, 급여, 부서 번호, 부서 이름을 출력
"""

import cx_Oracle
import lec08_database.oracle_config as cfg

with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as connection:
    with connection.cursor() as cursor:
        #oracle_method
        sql_oracle = '''
                select e.empno, e.ename, e.sal, d.deptno, d.dname 
                from emp e, dept d 
                where e.deptno = d.deptno and 
                      e.deptno = :deptno 
        '''
        # deptno 를 입력받기로 했기 때문에 and 하고  e.deptno = :deptno  한 줄 더 써줬다 (ta-da it became executable!)
        # ANSI METHOD
        # sql_ansi = '''
        # select e.empno, e.ename, e.sal, d.deptno, d.dname
        # from emp e join dept d
        # on e.deptno = d.deptno and
        #    e.deptno = :deptno
        # ''' # just change: cursor.execute(sql_ansi, deptno = dept_no) and must work fine
        dept_no = int(input('Enter the deptno>> '))
        cursor.execute(sql_oracle, deptno = dept_no)
        for empno, ename, sal, deptno, dname in cursor:
            print(empno, ename, sal, deptno, dname)
        #     OR
        # for row in cursor:
        #     print(row)

