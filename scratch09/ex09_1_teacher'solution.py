import pandas as pd
from numpy import mean

if __name__ == '__main__':
    # DF 생성
    file_path = 'emp.csv'
    emp = pd.read_csv(file_path, header = None)
    # comprobar el table
    print('shape: ', emp.shape) #13,8 # header = None 추가 후 (14, 8) #제대로 나옴
    print('head: ', emp.head()) # 0번 부터가 실제 데이터들인데 -> 데이터가 컬럼 이름으로 사용되고 있다
    # pandas.read_csv는 무조건 첫번째 행을 컬럼 이름으로 취급한다
    # 만약 csv파일에 첫번째 줄이 헤더가 아니고 실제 레코드인 경우에는, header = None 이라는 파라미터를 설정
    # 일반 텍스트편집기 보다 판다스가 더 빠르니, 변수가 많은 경우 판다스로 먼저 열어보고 -> 처음 몇개만 확인해서 -> header = None 을 추가할지 말지 결정

    # 테이터 프레임에 컬럼 이름을 설정
    emp.columns = ['empno', 'ename', 'job','mgr',
                   'hiredate', 'sal', 'comm', 'deptno']
    print(emp.iloc[0:2]) # 컬럼 이름 설정 확인

    print('\n급여가(sal)가 2000 이상인 직원들의 모든 정보')
    print(emp[emp['sal'] > 2000]) #Dataframe[조건식]

    print('\n부서번호가 10번인 직원들')
    print(emp[emp['deptno'] == 10])

    print('\n급여가 전체 직원의 급여의 평균보다 많은 직원의 사번 이름 금여를 출력')
    # select ename, empno, sal from emp where sal > (select avg(sal) from emp);
    print('\n Method_A')
    subset = emp[emp['sal'] > emp['sal'].mean()]
    print(subset[['empno','ename','sal']])
    print('\n Method_B')
    print(emp[emp['sal'] > emp['sal'].mean()][['empno','ename','sal']])

    print('\n 30번 부서에서 일하는 직책이 세일즈맨인 사번, 이름, 급여, 부서번호')
    # select empno, ename, job, sal, deptno from emp where deptno == 30 and job == 'SALESMAN'
    c1 = emp['deptno'] == 30
    c2 = emp['job'] == 'SALESMAN'
    subset = emp[c1&c2]
    # subset = emp[(emp['deptno'] == 30) & (emp['job'] == 'SALESMAN')]
    # 위 처럼 쓰는게 보기도 힘들고 (개인적으로) 좀 오래 걸려서 별루
    print(subset[['empno','ename','job','sal','deptno']])
    # boolean indexing 이 결국에는 where 절을 써주는 것

    print('\n 20,30번 부서에서 근무하는 직원들 중 급여가 2000을 초과하는 직원들')
    # select * from emp where deptno in (20,30) and sal > 2000;
    # select * from emp where (deptno = 20 or deptno = 30) and sal > 2000;
    print('\n Method A')
    c1 = emp['deptno'] == 20
    c2 = emp['deptno'] == 30
    # emp['deptno'] in (20,30)
    c3 = emp['sal'] > 2000
    subset = emp[(c1 | c2) & c3]
    print(subset[['empno','ename','sal','deptno']])

    print('\n Method B')
    # emp['deptno'] in (20,30)
    c1 = emp['deptno'].isin([20,30])
    c3 = emp['sal'] > 2000
    subset = emp[c1 & c3]
    print(subset[['empno', 'ename', 'sal', 'deptno']])

    print('\n 수당이 없는 직원들 중에서 매니저는 있고 직책은 매니저 또는 클럭')
    # select * from emp where comm is null and mgr is not null and job in ('MANAGER','CLERK')
    c1 = emp['comm'].isnull()  # isna = isnull # no commission received
    # emp['comm'] == np.na 이라고 하면 안됨 (사과가 없는데 사과를 찾을 수가 없다)
    # NaN = Not a number
    c2 = ~emp['mgr'].isna() # ~ not 연산자
    c3 = emp['job'].isin(['MANAGER','CLERK'])
    # c3 = (emp['job'] == 'MANAGER') | (emp['job'] == 'CLERK')
    subset = emp[c1 & c1 & c3]
    print(subset)
    # and (&), or (|), not(~)

    print('\n사원 이름에 E가 포함된 직원들의 이름')
    # SQL: select ename from emp where ename like '%E%';
    # the formual: subset = emp[emp['ename'].str.contains('E')] is the same as:
    # r = []
    # for x in list:   # make a list of True and False (and append if the component meets the condition)
    #     if x.contains('E'):
    #         r.append(True)
    # else:
    #     r.append(False)
    subset = emp[emp['ename'].str.contains('E')]
            # emp['ename']: 문자열을 아이템으로 갖는 시리즈
            # series 는 contains 라는 method 를 가지고 있는게 아니다
            # str.contains('E') -> 원소하나씩 꺼내서 문자열로 변환
        #앞쪽이 시리즈인 경우에 원소 하나하나 반복문에 넣어서 스트링에 메소드로 호출해 줄 수 있도록 -> pandas 에 특화된 문법이라고 생각해도 된다

            # SQL 에서는 _ 를 쓰면 한개만 하는 것: 정규표현식을 쓰면 파이썬에서도 구현가능

    print('\n print in DF')
    print(subset[['ename']]) #DF 로 출력  # 컬럼이름이 있느냐 없느냐의 차이
    print('\n print in series')
    print(subset['ename']) #Series 로 출력

    # DataFrame.to_csv(file_path): 데이터 프레임을 csv로 저장
    # to_csv() 함수는 행 이름 (row index) 를 파일에 쓰는게 기본값
    # -> si no quiera, 함수를 호출할 때 index = False 파라미터 추가
    emp.to_csv('emp2.csv', index = False)
    # 데이터 프레임안에 헤더를 추가했기 때문에 헤더가 같이 들어가 있다

    # version 도 유의해서 도큐멘트 읽어주세욤! ㅎ3ㅎ
    # NaN 가 있어서 정수로 변환이 실패 -> 그래서 mgr 이 float
    # 그냥 int에 넣어버리면 정수로 변환 가능가능 *0*


# 여기서 오라클로 감 