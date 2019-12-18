"""
ex07_databinding.py
data binding을 사용한 SQL 문장 실행
"""

import cx_Oracle
import lec08_database.oracle_config as cfg

# there are two ways to execute data binding

with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as connection:
    with connection.cursor() as cursor:
        deptno = int(input('Entra el numero del departamento >>'))
        dname = input('Entra el nombre del departamento>> ')
        loc = input('Entra la locacion del departamento>>')

        # METHOD1
        # sql1 = 'insert into dept2 values (:0, :1, :2)' # :0, :1, :2 -> 변수가 와야한 자리입니다~ 정도만 알려주는 것
        # For now, we are using colon (:) in Oracle, but it varies on the database system one is using
        # (i.e. Sql light 는 ? 을 사용)
        # they just mean that those values are empty, when inserting sth, the order becomes unimportant ->?
        # :0, :01, :3 - indices, place holders (are their orders important?)
        # cursor.execute(sql1, [deptno, dname, loc])
                        # list 첫번쨰 원소가 Values 의 첫번째, dname이 values의 두번째,,, 인덱스에 들어간다
        # SQL 문장에다 데이터들을 넣어주는 과정 (문자열과 데이터를 묶어준는 과정) 을 data binding 이라고 부른다


# :0, :1, :2 는 임의의 값들, 순서는 중요, 값은 노 중요

        #METHOD2
        sql2 = 'insert into dept2 values(:dept_no, :dept_name, :loc)' #we can also give the names of parameters
        # the method uses keyword argument
        cursor.execute(sql2,
                       # 키워드 이름 = 사용자가 입력받은 값 전달
                       dept_no = deptno,
                       dept_name = dname,
                       loc = loc)

        connection.commit()
        # https://en.wikipedia.org/wiki/Data_binding
        # 이렇게하면 (00,a'nd, city) 와 같이 중간에 작은 따옴표가 오고 바깥은 작은 따옴표로 묶어도 잘 된다

# data binding (  sQL 문장 안에 사용자가 입력한 값들이 필요하다면 SQL 문장을 만들 때 비워두었다가 (:을 사용) 완성된 SQL 문장을 실행하는 것)
# 문장와 데이터를 연결해 주는 것 ?

# 비정형데이터를 다루는 Mongo DB 가 많이 사용되기 시작하는 추세
# 지금까지의 대세를 oracle, 아니면 오픈소스였던 MS sql


