"""
ex06_insert.py
사용자 입력을 받아서 database에 insert
"""

import cx_Oracle
import lec08_database.oracle_config as cfg

with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as connection:
    with connection.cursor() as cursor:
        # connection 의 결과를 커서에 저장하겠다
        deptno = int(input('부서번호를 입력하세요>>'))
        dname = (input('부서이름을 입력하세요>>'))
        loc = (input('부서의 위치를 입력하세요>>'))

#이렇게 입력받은 정보를 가지고 SQL insert 문장을 만들고싶다:
        # indentation error!! 주의 (with connection 안쪽으로 오게 해주세요 *0*!)
        sql_insert = f"insert into dept2 values({deptno},'{dname}','{loc}')"
                #f'' -> formatted string , 앞뒤를 중괄호 {} 로 묶어준다
                # 이렇게 하는 방법은 사용자가 입력한 문자열에 따옴표('')나 큰따옴표("")가 포함되어 있는 경우에는 SQL 에러가 발생할 수 있다
                # 이래서 이 방법은 권장하지 않는다
                # 그래서 data binding 이라는 기법을 권장한다
        cursor.execute(sql_insert)
        connection.commit()
        # cx_Oracle.DatabaseError: ORA-00984: 열을 사용할 수 없습니다
        # prob with line 23: cursor.execute(sql_insert)
        # we had to put '' on characters!!! (OMG so stupid myself) -> que detallesta

# when we inserted (0, 'I'm a boy', burp)
# Error: ORA-01756: 단일 인용부를 지정해 주십시오
# because even though we wrote "I'm a boy", this is how Oracle received:
# 1) 'I' and  2) m a boy'

# there is a concept called 'data binding' to deal with this kind of issue:
# SQl 문장에다가 변수의 값들을 자동으로 만들어 주는 것 ..? 
# 그래서 위에서 sql_insert 만든 것 과 같은 방법은 결코 좋은 방법이 아니다




