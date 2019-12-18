"""
ex03_select.py

for-in 구문을 사용한 select 결과 처리
for 변수 in 커서:
    실행문

for - in 구문에서 cursor.fetchone()의 결과를 변수에 저장/전달 한다
"""
import cx_Oracle
import lec08_database.oracle_config as cfg

# 늘 뼈대 만들기 import - connection 설정 - cursor 설정 - cursor 닫기 - connection 종료

# while 구문을 활용한 코드는 file 에서 readline() 을 사용한것과 같다
# file 에서 for ... in .. 에서 파일을 주면 자동으로 readline() 을 호출해준것과 같은 logic

# connection 설정
connection = cx_Oracle.connect(cfg.user,
                               cfg.pwd,
                               cfg.dsn)

# cursor 설정
cursor = connection.cursor()

# SQL 문장 실행 (DEPT로)
cursor.execute('select * from dept')

# select 결과 처리
for row in cursor:
    print(row)

# while 구문 보다 for .. in.. 구문이 훨씬 쉽다
# 파일에서: with 를 사용하면 자동으로 닫아준다 -> 여기서도 역시 with .. as .. 구문을 사용하면 close() 부분 두 줄을 생략할 수 있다

# cursor 해제
cursor.close()

# connection 종료
connection.close()















