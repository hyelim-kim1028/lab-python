"""
Named tuple:
"""

from collections import namedtuple

# 정형 데이터에서는 보통 데이터를 테이블 (데이터프레임)에 저장하고,
# 테이블에 있는 row 를 sample, record, observation, example 등 다양한 이름으로 부른다.
# 컬럼 부분에는 같은 타입의 데이터들이 들어간다. 숫자, 문자등 다양한 데이터 타입으로 들어간다.
# 특성, feature, 변수(variable) 등 다양한 이름으로 불리운다

# 이번 챕터에서는 row하나를 저장하는 것을 다룬다.
# i.e. 학생/환자 정보
from typing import NamedTuple

student_1 = (1, '홍길동', 10, 20, 30)
# 테이블 구조를 안다면, 위의 값들이 무엇을 의미하는지 알 수 있지만, 구조를 모른다면 파악하기 힘들다
# 데이터의 구조가 학생의 번호, 이름, 수학점수, 과학점수, 컴퓨터점수 라고 알고 있었다면 해석이 가능하다
print('번호:', student_1[0])
print('과학 점수', student_1[3])
print('과학 점수', student_1[-2])

# 튜플 타입의 단점:
# 해당 인덱스의 원소가 무슨 값을 의미하는지 파악하기 어렵다
# 어떤 특정 원소에 접근(read/write)하기 위해서 정수 인덱스만 사용해야 함.
# 딕셔너리의 장점은 (key:value) 이라는 포맷, 하지만 단점으로 값이 변환다. => 딕셔너리처럼 사용하면서 값이 변하지 않는 것을 만들고 싶었다
# dictionary/ stu_dict = {'no':2, 'name':'김길동','math':90, 'science':50, 'cs':100}  # key와 value가 쌍으로 들어가 있는 데이터 타입
# 매번 이렇게 써줘야한다는 단점도 있음 (키값을 갖는다는 장점이 있지만 매우 귀찮고, 오타가 에러로 연결될 확률이 높다) -> 반복할 때 효율성(efficiency)이(가) 떨어짐
# tuple과 dictionary 단점들을 해결하기 위해서 NamedTuple 클래스가 만들어짐 (#A)
Student = namedtuple('Student',('no','name','math','science','cs')) # 껎데기 or prototype이라고 불리운다
# 이런 포멧의 경우 'cs' 대신 'com-sci'와 같은 이름을 지정하면 에러가 난다 (Type names and field names must be valid identifiers)
# 왜냐하면 나중에 . 하고 변수이름을 불러올 때 -기호로 인지한다
# 여기서는 문제가 없으니까 나중에 에러를 불러올수 있음 (적절하지 않은 변수이름을 만들 수 있다)
# 그래서 이런 표기법이 마음에 들지 않아서 Python ver 3.6부터 namedtuple을 class처럼 선언하는 방식이 생김 -> #C

# By using namedtuple class, we can access the data using both index_number and colname
student_2 = Student(2, '허균', 100, 100, 100)
print(student_2)
print(f'번호: {student_2[0]}, {student_2.no}') #{studnet_2.no} 에서 . 찍으면 자동완성으로 colnames를 보여줌. # colname을 몰라도 접근 가능
print(f'수학 점수: {student_2[2]}, {student_2.math}')

# C (Python 3.6이상에서만 사용가능한 namedtuple 선언방식)
class Student2(NamedTuple): # Studnet2 클래스는 NamedTuple 클래스를 상속
        # for NamedTuple/ import > from typing import NamedTuple
    # field 선언 - 변수 타입 connotation을 반드시 추가해야한다
        # 일반적으로 함수나 클래스를 선언한 때는 타입 선언의 명시가 not obligatory 하지만 namedtuple must connotate its data type
    no: int
    name: str
    math: int
    science: int
    cs: int
#A 방식을 싫어하는 사람들을 위한 방법 #C
# 상속 (inheritance) > Student2는 NamedTuple을 상속받는다

student_3 = Student2(4, 'abc', 90, 88, 77)
print(student_3)
# Student2(no=4, name='abc', math=90, science=88, cs=77) # Type_name(colname = value, colname = value...)
# it's tuple, so we can access the info using index or .colname








