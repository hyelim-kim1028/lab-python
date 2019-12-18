# file in order: ex01 > oracle_config > ex02

"""
ex02_select.py
Oracle 데이터 베이스 서버에서 select 구문 실행, 결과 확인
"""
import cx_Oracle
import lec08_database.oracle_config as cfg

# 데이터 베이스 서버와 연결 설정 - 접속 (로그인)
connection = cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn)
#                    connect 함수(user id, password, dsn)

# 데이터 베이스도 사용이 끝난 다음 로그아웃 (케넥션 연결 해제) 해야한다 #connection.close()
# 동시에 DB 에 접속할 수 있는 connect 을 관리한다

# 접속한 데이터베이스 버전 정보
print('DB version:',connection.version)
# DB version: 11.2.0.1.0
# conncet 가 정상적으로 이루어졌다면 다른 아이들 버전도 정상적으로 읽어와야한다
# The command was able to log-in

# SQL 문장을 실행시키지 위해서는 cursor 객체를 생성해야한다
# 여기서는 SQL 의 실행 결과를 담고 있는 아이를 커서라고 일컫는다
cursor = connection.cursor()

# 전체 검색 문장
# SQL 문장 실행:
cursor.execute('select * from emp')
# SQL 문장을 만들 때 끝에 ';' 을 넣지 않는다
# cursor 란 DB의 처음을 가르켜주고, DB를 한줄 한줄 읽을 수 있는 도구
# 마지막에 아무것도 없어지면 -> ?더 이상 읽을 것이 없습니다 라는 식의 문구를 반환시켜줄 수도 있다
# 마지막까지 자동으로 읽게하기위해서 -> while True 를 사용한 무한루프 만들기 :)!

# A.
# while True:
#     row = cursor.fetchone()
#     if row is None: # select 의 결과가 더 이상 없다
#         break
#     print(row)

#B.
row = cursor.fetchone() #select 의 결과에서 한 행(row) 의 데이터/레코드를 읽음
while row:  #읽은 행(row)의 데이터가 있는 동안에
    print(row) #각 행의 데이터/레코드가 tuple 형태로 출력됨
    row = cursor.fetchone()

# A and B return the same results!
# 패치하고 -> 출력하고 -> 패치하고 -> (있으면) 출력하고 -> fetch 가 None 이 되면 루프가 멈춘다

# (7369, 'SMITH', 'CLERK', 7902, datetime.datetime(1980, 12, 17, 0, 0), 800.0, None, 20)
# return the values in tuple format
# each row in a db is counted as one tuple





# cursor 도 모든 사용을 끝냈으면 객체 사용 후 리소스 반환
cursor.close()

# 데이터베이스 서버와 연결 종료
connection.close()
