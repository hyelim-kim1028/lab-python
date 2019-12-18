"""
ex05_insert.py
"""

import cx_Oracle
import lec08_database.oracle_config as cfg

# 데이터베이스 서버와 연결 설정
with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as connection:
    # Create a cursor object that can execute and analyze SQL sentence
    with connection.cursor() as cursor:
        sql_insert = "insert into dept2(deptno, dname, loc) values(91,'강의장 10','서울')"
        # we can also write it this way: "insert into dept2 values(91,'강의장 10','서울')" since we are utilizing all the columns
        #  바깥을 큰 따옴표로 묶은 이유: 안에 작은 따옴표를 사용 (밖에도 작은 따옴표를 사용하면 갑자기 문장이 끊겨서 문법적인 오류가 발생)
        # 아니면 \ back slash 사용할 수도 있지만 번거로우니까 ㅠㅠ!
        cursor.execute(sql_insert)
        connection.commit()

        sql_select = 'select * from dept2'
        cursor.execute(sql_select)
        for row in cursor:
            print(row)
# It "seems like" it's been inserted -> have not yet done commit!!
# commit 하지 않으면 PC 와 DB 가 공유되지 않고, 고로, 다른 PC 와도 공유되지 않는다 그래서 여기서는 변경된 것 처럼 보이지만 DB 에서는 보이지 않는 것
# DML (Data Manipulation Language) - insert, delete, update
# DML 결과를 영구적으로 반영하기 위해서는 반드시 commit 을 해야한다
# commit 을 할 때에는 connection 에서 해준다
# after inserting the line connection.commit() in line 16, the data is shown in both Pycharm and SQLd

# commit 은 원하는 시점에 해준다 *0*

