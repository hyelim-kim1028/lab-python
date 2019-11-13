"""
클래스 작성, 객체 생성, 메소드 사용 연습
"""

# 회사원의 Db 구축하고 읽어드리는 것
# 완전 똑같이 해야 읽어 드릴 수 있다 (en theoria). 하지만 여기서는 그냥 연습 ^^

class Employee:
    """
    사원 정보와 급여 인상 메소드를 가지고 있는 클래스
    field: empno, ename, salary, deptno
    field: 변수를 만들어라

    method: raise salary (self, pct) #pct for percent
    """
    def __init__(self, empno, ename, salary, deptno): #파라미터 주기
        self.empno = empno #필드 초기화
        self.ename = ename
        self.salary = salary
        self.deptno = deptno
    def raise_salary(self,pct): #메소드: 첫번째 파라미터는 self
                                # self는 주어같은 것: 누구의 (self)의 무엇을(기능) 해줄 것인가?
        """
        인상된 급여를 리턴
        return the raised salary
        :param pct: 급여 인상율 (0.1 = 10%, 0.5 = 50%)
        :return: 인상된 급여
        """
        # return self.salary + (self.salary * pct)
        self.salary = (1 + pct) * self.salary  # this formula is the same as: self.salary *= 1+pct
        return self.salary
        # 150% = 내 현재 연봉 + 50% 인상된 연봉
    def emp_info(self):
        return f'사번: {self.empno}, 이름:{self.ename}, 급여{self.salary}, 부서번호: {self.deptno}'
    # there was an error for indentation

gil_dong = Employee(1010,'홍길동',1000,10) #객체 생성
print(gil_dong.emp_info()) #직원 정보 출력 # 객체가 없으면 메소드를 호출할 수 없다
print(gil_dong.raise_salary(0.1)) #급여 인상
print(gil_dong.emp_info()) #인상시킨 다음에 다시 출력해주면 인상된 급여가 나온다 #직원 정보 출력'

scott = Employee(1011, 'Scott', 10000, 20)
print(scott.emp_info())
print(scott.raise_salary(-0.1)) #연봉 삭감 ...^0^;;;; 머야 ㅠㅠㅜㅜ 엉엉
print(scott.emp_info())

