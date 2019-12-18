# with_as 구문을 사용하면 connection & cursor 구문을 간단히 할 수 있다
"""
ex04_with_as.py
- with ... as 구문을 사용하면 cursor.close() 와 connection.close()가 자동으로 호출되어서 생략가능하다
"""

import cx_Oracle
import lec08_database.oracle_config as cfg

with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as conn:
    # conn = oracle.connect() 와 같은 문장
    with conn.cursor() as cursor:
        cursor.execute('select empno, ename, deptno from emp')
        for row in cursor:
            print(row)

# SQL 문장 마지막에 semi-colon(;) 을 사용하면 에러가 난다 (cx_Oracle.DatabaseError: ORA-00911: 문자가 부적합합니다)
# PC 가 Oracle DB에 접속하는 과정을 connection을 맺는다 라고 표현



