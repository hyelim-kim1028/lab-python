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
    def __repr__(self):
        return f'(사번: {self.empno}, 이름:{self.ename}, 급여{self.salary}, 부서번호: {self.deptno})'
    # there was an error for indentation
    # emp_info(self) -> shift + F6 -> rename 창이 뜨면 -> 새로운 이름을 써주고 -> continue
    # -> 그럼 아래의 refactoring Preview 창에서 [do refactor] 버튼을 클릭해준다 (그렇게 emp_info 모두 __repr__으로 바뀜)



# class 06에서 이어지는 내용
# 같은 사람인지 다른 사람인지 비교 -> empno (내 생각: __eq__ -> self.empno == other.empno)
# sort 할 때는? 상황에 맞게끔 (__gt__를 활용해서 정렬)
# 상황에 따라 달라지는 만큼 클래스안에 메소드를 만들어 두면 우리가 만든 클래스는 그 메소드로 밖에 정렬을 하지 못한다
# 그럴바에는 gt 를 안만드는게 더 나음
# 다른 방식을 제공



gil_dong = Employee(1010,'홍길동',1000,10) #객체 생성
print(gil_dong.__repr__()) #직원 정보 출력 # 객체가 없으면 메소드를 호출할 수 없다
print(gil_dong.raise_salary(0.1)) #급여 인상
print(gil_dong.__repr__()) #인상시킨 다음에 다시 출력해주면 인상된 급여가 나온다 #직원 정보 출력'

scott = Employee(1011, 'Scott', 10000, 20)
print(scott.__repr__())
print(scott.raise_salary(-0.1)) #연봉 삭감 ...^0^;;;; 머야 ㅠㅠㅜㅜ 엉엉
print(scott.__repr__())

ohsam = Employee(1012, '오쌤', 500, 30)

Graceful_forest = Employee(1013, '金惠林', 20000, 20)

# 리스트 만들기
employees = [ohsam, gil_dong, scott, Graceful_forest]
print(employees)
# __repr__ 함수를 만들었기 때문에 [(사번: 1012, 이름:오쌤, 급여500, 부서번호: 30),
#                                (사번: 1010, 이름:홍길동, 급여1100.0, 부서번호: 10),
#                                (사번: 1011, 이름:Scott, 급여9000.0, 부서번호: 20)]
# 이렇게 출력된다
# 그래서 emp_info 에서 __repr__ 로 refactor 한 것!

# print(sorted(employees))
# TypeError: '<' not supported between instances of 'Employee' and 'Employee'
# 정렬의 기준을 주지 않았기 때문에 정렬을 할 수 없어서 에러를 준다

print(sorted(employees, key = lambda x: x.empno))
                        #           파라미터:리턴값
                        # 이게 정렬 기준이 된다
                        # 사번이 오름차순으로 정렬된다
# [(사번: 1010, 이름:홍길동, 급여1100.0, 부서번호: 10), (사번: 1011, 이름:Scott, 급여9000.0, 부서번호: 20), (사번: 1012, 이름:오쌤, 급여500, 부서번호: 30)]
# key 가 리턴해주는 값을 가지고 __gt__해주는 것
# sort 를 할 때 마다 정렬기준을 주는 것 -> using lambda expression!

print(sorted(employees, key = lambda x: x.salary))
#[(사번: 1012, 이름:오쌤, 급여500, 부서번호: 30), (사번: 1010, 이름:홍길동, 급여1100.0, 부서번호: 10), (사번: 1011, 이름:Scott, 급여9000.0, 부서번호: 20)]
print(sorted(employees, key = lambda x: x.ename))
#[(사번: 1011, 이름:Scott, 급여9000.0, 부서번호: 20), (사번: 1012, 이름:오쌤, 급여500, 부서번호: 30), (사번: 1010, 이름:홍길동, 급여1100.0, 부서번호: 10)]
# 이름: 알파벳이 빠르고, 오 > 홍 순서대로 나온다 (한자를 포함했을 때 영어>한자>한국어 순서대로 왔다)
print(sorted(employees, key = lambda x: x.deptno))
# 정렬방법 두가지: 1)  __gt__, __lt__ 처럼 클래스에 바로 주는 방법이 있고 (class06), 2) 상황에 따라 정렬 기준이 바뀔 때는 lambda를 사용
# ascending: default, descending: reverser = True

















