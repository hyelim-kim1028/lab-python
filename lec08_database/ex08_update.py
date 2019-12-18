"""
ex08_update.py

deptno 를 입력받아서 해당 부서의 위치loc 를 update 하는 SQL 문장만들기 + 실행
"""

import cx_Oracle
import lec08_database.oracle_config as cfg

with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as connection:
    with connection.cursor() as cursor:
        deptno = int(input('Enter the deptno>> ')) # 위치를 수정할 부서번호 입력
        loc = input('수정할 위치 입력받기>> ')

        sql_update = 'update dept2 set loc = :loc where deptno = :deptno'
        # :loc 와 :deptno 는 비워져있는 부분 (binding 이 되어야할 부분) -> data 가 들어가야 할 parameter 부분

        cursor.execute(sql_update,
                       loc = loc,
                       deptno = deptno)
        connection.commit()

# 파이썬을 공부하는 궁극적인 목표: DB를 가지고 빅데이터를 하는 것 (머신러닝 알고리즘을 사용해서) 등등

# select 에서는 commit 사용하지 않아도 된다
# insert, delete, update 와 같은 값이 변경되는 경우에만 commit사용

# Enter the deptno>> 90
# 수정할 위치 입력받기>> 테헤란로 123
# 공백을 포함했는데도 가능가능 ^0^!

