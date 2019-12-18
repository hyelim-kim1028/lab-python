"""
과제
lec08_databse 패키지의 내용들을 참고해서, 오라클 데이터베이스에 연동,
오라클 데이터베이스에서 emp 테이블의 모든 레코들을 검색해서 불러오기 -> 2차원 리스트

2차원 리스트를 csv모듈을 사용해서 csv 파일로 저장
"""
# 오라클 데이터베이스에 연동
import cx_Oracle
print(cx_Oracle.version)
import lec08_database.oracle_config as cfg
import csv

# 데이터 베이스 서버와 연결 설정 - 접속 (로그인)
connection = cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn)
print('DB Version: ',connection.version)

# 오라클 데이터베이스에서 emp테이블의 모든 레코드들을 검색해서 불러오기

cursor = connection.cursor()
cursor.execute('select * from emp')

emp = []
row = cursor.fetchone() #select 의 결과에서 한 행(row) 의 데이터/레코드를 읽음
while row:  #읽은 행(row)의 데이터가 있는 동안에
    print(row) #각 행의 데이터/레코드가 tuple 형태로 출력됨
    row = cursor.fetchone()
    emp.append(row)

print(emp)

# # 2차원 리스트를 csv모듈을 사용해서 csv 파일로 저장
with open('emp.csv', mode = 'w', encoding= 'UTF-8', newline = '') as f:
    writer = csv.writer(f, delimiter = ',') # writer 객체를 생성을 하면 실제 파일에다 write 할 수 있다 (writerow 메소드)
    for row in emp:
        writer.writerow(row)

with open('emp.csv', mode = 'r', encoding = 'UTF - 8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# cursor 사용 후 리소스 반환
cursor.close()

#데이터베이스 서버와 연결 종료
connection.close()

