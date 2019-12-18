"""
emp.csv 파일을 읽어서 데이터프레임을 생성
데이터프레임을 사용해서:
1) 급여(sal)가 2000이상인 직원들의 모든 정보를 출력
select * from emp where sal > 2000 을 boolean 인덱싱을 사용해서 파이썬에서 구현하라
2) 부서번호 (deptno) 가 10번인 직원들의 모든 정보를 출력
select * from emp where deptno = 10
3) 급여가 전체 직원의 급여의 평균보다 많은 직원의 사번, 이름, 급여를 출력
select empno, ename, sal from emp where sal > avg(sal)
4) 30번 부서에서 일하는 직책이 SALESMAN 인 직원들의 사번, 이름, 급여, 부서번호를 출력
select empno, ename, sal, deptno from emp where deptno = 30 and job = 'SALESMAN'
5) 20,30번 부서에서 근무하는 직원들 중 급여가 2000을 초과하는 직원들의 사번, 이름, 급여, 부서번호 출력
select empno, ename, sal, depnot from emp where deptno in (20,30) and sal > 2000
6) 수당이 없는 직원들 중에서, 매니저가 있고, 직책이 'MANAGER' 또는 'CLERK'인 직원들의 모든 정보 검색
select * from emp where comm is null and manager is not null and job in ('MANAGER','CLERK')
7) 사원 이름에 'E'가 포함된 직원들의 이름만 출력 (string 클래스에 contains함수 -> str.contains() 이용)
select ename from emp where ename lik '%E%'

pandas 도 write.csv할 수 있다 (데이터프레임이 ㅁ나들어져있어야 write 할 수 있다)
- 데이터 프레임을 csv형식으로 파일에 write 하는 함수를 찾아서 실행해보기
"""

import os
import csv
import pandas as pd

file_path = os.path.join('emp.csv')
with open(file_path, mode='r', encoding='UTF-8') as f:
    reader = csv.reader(f)
    reader.__next__()
    df = [line for line in reader]

# emp.csv 파일을 읽어서 데이터프레임을 생성
# there is a header problem
file_path = os.path.join('emp.csv')
df = pd.read_csv(file_path, sep = ',', encoding = 'UTF-8', header = None)
# print(df)
# print(df.columns)

df = pd.DataFrame(df)
df.rename(columns={0: 'empno', 1: 'ename', 2: 'job', 3: 'mgr', 4: 'date', 5: 'sal', 6:'comm', 7: 'deptno'}, inplace=True)
print(df)
# problem: I only have 13 employees in my data when there has to have 14 of them

# 1) 급여(sal)가 2000이상인 직원들의 모든 정보를 출력

