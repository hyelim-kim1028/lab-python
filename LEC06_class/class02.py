"""
클래스 = 데이터 (변수 -> 필드) + 기능 (함수 -> 메소드)  => 데이터 타입
"""

#class : field + method
class Score:
    # 생성자를 호출했을 때 필드들을 초기화하는 함수 (필드를 초기화한다, 변수에다 값을 저장한다)
    def __init__(self, korean, english, math):
        self.korean = korean # field
        self.english = english #field
        self.math = math #field
    # 목적은 저기 있는 값들을 가지고 평균, 총점 등등을 계산해 주는 것 (descriptive stats?)
    # 그 기능을 method 라고 한다

    #총점, total
    def calc_total(self): #method
        return self.korean + self.math + self.english
            # just korean + math + english won't function
            # we make functions assuming that there are values within the fields already
    def calc_average(self): #method
        return self.calc_total()/3
    # self. 하면 조금 이따가 무조건 self가 첫번째 argument 가 된다

# score 클래스의 객체를 생성
score1 = Score(99,88,77)
# class 이름으로 함수를 호출하는 것을 생성자 호출 (-> __init__ 자동 호출?) 이라고 부르고,
# 이렇게 생성자를 호출하면 객체라는게 만들어진다
# 이닛이 있기 때문에 생성자가 호출
# 우리는 이렇게 만들어진 것을 객체라고 부른다
# 이렇게 값들이 만들어 지면 토탈이나 어버레지와 같은 기능들을 사용할 수 있는 상태가 되는 것

# math만 점수를 바꿔주겠다
score1.math = 79

print(score1.calc_total())
print(score1.calc_average())

score2 = Score(90,85,70) #객체를 생성해주세요 (생성자 호출)
Score.calc_average(score2) #this format is also possible
print(score2.calc_total())
print(score2.calc_average())




