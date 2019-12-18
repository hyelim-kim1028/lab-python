# package 들간의 dependency를 조절하기 귀찮은 경우에 상용 패키지 사용 (i.e. 아나콘다)

import csv
import cx_Oracle

if __name__ == '__main__':
    # DSN: Data Source Name
    dsn = cx_Oracle.makedsn('localhost',1521, 'orcl')
        # 여기있는 정보들은 Oracle 에서 가져오는 것 (호스트이름, 포트, SID) 순서
        # 접속할 데이터 베이스의 서버 정보 불러오기

    # 데이터 베이스를 사용하기 위해서 서버에 접속 (connection)
    with cx_Oracle.connect('scott', 'tiger', dsn) as connection:
                        # user_id, password, server_info
        # 커서 객체 (SQL문을 데이터 베이스 서버에서 실행) 생성
        with connection.cursor() as cursor:
            # SQL 문장을 작성
            sql_select_emp = 'select * from emp'
            # SQL 문장을 데이터 베이스 서버에서 실행
            cursor.execute(sql_select_emp)
            # SQL 문장 실행 결과 처리  # 튜플들! -> list -> df 로 만드는 과정이 필요
            emp = [row for row in cursor] # 커서에 있는 row' 들을 리스트에 저장하겠다 (row)
            # 실제 데이터들만 저장하고 컬럼 이름들은 안된다
            print(emp[0:2])
            print(len(emp))

    # connection 클래스 & 커서 클래스 를 알고 있는게 중요하다
    # indentation -> \t 1개 만큼! (들여쓰기 중요)
    # 리스트 emp의 내용을 파일에 csv형식으로 저장
    # 변수 선언
    file_path = 'emp.csv'
    with open(file_path, mode = 'w', encoding = 'UTF-8', newline = '') as f:
        # csv writer 객체를 생성
        writer = csv.writer(f)
        for item in emp: # 리스트의 각 아이템마다 반복
            writer.writerow(item) # 아이템을 csv파일에 한 줄씩 쓰기
