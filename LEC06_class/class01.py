"""
클래스(class): 객체지향언어(i.e. C++,C#, java, python)
- 많은 언어들이 객체지향이라는 컨셉에서 설계가 되었다
- 여러가지 책에서 어렵게 설명한다. 실체 (object)의 설계도, 눈에 보이는 실체를 소프트웨어로 구성하기 위해서 사용하는 설계도 ...
- 프로그래밍을 하면서 만들고 싶은 대상: 계산기을 만들고 싶다면 계산기가 대상이 된다. 데이터를 분석하기 위해서는 여러가지 대상이 생긴다 (데이터를 저장하는 대상, 등등)
- 그 대상을 object라고 부른다.
- 이 대상은 data & function 으로 이루어져있다 (계산기는 숫자 (데이터) + 더하기,빼기,곱하기,나누기,등 (기능))
-  데이터는 변수로 선언
-  기능은 함수로 만든다
- 클래스는 데이터의 변수 선언과 기능인 함수 선언을 한꺼번에 가지고 있는 프레임
- 정리: 프로그램에서 만들려고 하는 대상(객체) 이(가) 가져야 할 속성(데이터) 과(와) 기능(함수) 을(를) 묶어서 하나의 데이터 타입으로 설계한 것
                                                                             # 기능을 묶은 "데이터 타입"
# 데이터 타입: 정수, 플롯, str, ...
- 데이터 타입은 변수에 저장 할 수 있는 타입

- 텔레비전의 소프트웨어를 을 만드는 내가 된다면,,,
- 티비가 가져야할 속성/데이터는 1.채널(텔레비전안에 채널이라는 속성을 저장하고 있어야한다) 2.음량/볼륨 3.외부입력 4.전원(상태관리) 등등
- 티비가 가져아할 기능: 채널 변경, 음량 변경, 전원 on/off
- 티비 라는 것이 클래스가 되고, 티비가 갖고 있는 속성과 함수들은 위에 나열한 것들이고,
- 클래스가 가지고 있는 함수들을 우리는 메소드(method) 라고 부른다
- method: 클래스가 가지고 있는 함수

필드(field): 클래스의 객체가 가지고 있는 데이터(변수) / 클래스에 선언되어져있는 변수
-> 여기서는 power, channel, volumne 이 필드 (필드 = 파라미터?)
"""

# 리모콘이라고 생각하고 만든다 (리모콘 그림 노트에 있다)

# class 를 만들어보자
# class 클래스이름:
#       """
#       클래스에대한 문서 만들기
#       """
class BasicTv:
    """
    BasicTv 클래스
    """
    # 데이터를 설계할 때에는 함수를 하나 만든다
    # 생성자가 호출됐을 때 실행되는 메소드 (함수)
    def __init__(self, power, channel, volume): #다른이름을 쓰면 안되고 항상 init을 사용해야한다
                        #전원, 채널, 음향
        print('BasicTv 생성자 호출') # with this the class works
        self.power = power # power in the paramter
        # parameter power to be saved in a variable self.power
        self.channel = channel # channel in the parameter
        self.volume = volume

    # 클래스 내부에서 정의하는 함수: 메소드
    # 텔레비전 소프트웨어에서 전원을 on/off하는 기능 만들어 보기
    def powerOnOff(self): #powerOnOff 에서 ()를 넣어주니까 자동으로 self를 만들어 주었다
        if self.power == True: # power = True (TV가 켜져있으면)
            self.power = False #TV가 켜져있는 상태에서 버튼을 눌렀으니까 => TV를 끔
            print('TV off')
        else: # TV가 꺼져있으면
            self.power = True  # TV가 꺼져있는 상태에서 버튼을 눌렀으니까 => TV를 켬
            print('TV on')

    #기능: 채널변경
    # 채널의 볼륨업 과 다운이 각각 다른 메소드면 좋겠다
    def channelUp(self):
        self.channel += 1
        print('Channel:', self.channel)

    def channelDown(self):
        self.channel -= 1
        print('Channel:',self.channel)

    # 볼륨 업/다운 기능
    def volumeUp(self):
        self.volume += 1
        print('Volume:',self.volume)

    def volumeDown(self):
        self.volume -= 1
        print('Volume:',self.volume)

# 리모컨이 꺼져있을 때 채널/볼륨이 바뀌지 않게 고쳐주기
# 음수 불가능하게 해주기
# 채널 개수가 정해져있고 -> 5에서 0으로 돌아게 그리고 0에서 다운하면 5로 돌아 갈 수 있게 바꿔주기 (순환)
# 볼륨은 최댓값에 도달하면 멈추고, 볼륨다운도 멈춘다 (0부터 5)


# porq los nombres de funciones se han subrayados de gris?
# 되도록이면 단어를 붙여서 만들지 말고, underscore 로 분리해서 만들고 no upper and lower case combis
# i.e. function should be lowercase

# 클래스 설계(정의)

#클래스의 객체 (인스턴스)를 생성해서 변수에 저장
# 생성자 (constructor) 호출
# 생성자를 호출하면 객체(object)가 생성된다
tv1 = BasicTv(power = False, channel = 0, volume = 0)
# ctrl 을 누른채로 BasicTv에 마우스를 클릭하면 init으로 돌아간다. 왜냐하면 클래스의 생성자 라고 인식하기 때문
# init 은 크래스 이름을 함수처럼 호출 했을 때 나타난다?

# power func practice
print(tv1)
print(tv1.power) #텔레비전이 꺼져있는 상태
tv1.powerOnOff() # 텔레비젼이 켜졌다 #method 는 tv1 과 같이 변수
# How it functions: go back to def powerOnOff(self) => tv1 became 'self' itself
# channel func practice
tv1.channelUp() # channel func must work only when TV is on
tv1.channelUp()
tv1.channelDown()
tv1.channelUp()
tv1.channelUp()
tv1.channelUp()
tv1.channelUp()
tv1.channelDown()
tv1.powerOnOff() # 텔레비젼이 꺼졌다 (마지막 채널: channel 4)
tv1.powerOnOff() # 텔레비젼이 다시 켜졌다
tv1.channelUp() # += 1 = channel 5 로 반환한다 (마지막으로 변경되었던 채널이 default = 0 으로 돌아가지 않고 남아있다)
# volume practice
tv1.volumeUp()
tv1.volumeUp()
tv1.volumeUp()
tv1.volumeUp()
tv1.volumeUp()
tv1.volumeUp()
tv1.volumeDown()
tv1.volumeDown()
tv1.volumeDown()
tv1.volumeDown()
tv1.volumeDown()
tv1.volumeDown()
tv1.powerOnOff() # 텔레비젼이 꺼졌다


# self = 주소값
# 생성자를 호출했을 떄 파이썬 이터프레트가 메모리 공간에 마련한 곳의 주소값을 셀프라고 한다
# 이 셀프는 우리가 변경하지 않는다 (절대로! 허용하지도 않는다) + 어디에다 만다는것도 우리가 할 수 없다
# 메모리 공간을 확보하고 __init__을 호출하면서 self 에다가 주소를 자동으로 넣어준다
# 그래서 tv1 = BasicTv(power,channel,volume) 에는 셀프를 넣어주는 것 그리고 여기에 넣은 값들은 위의 init__ 에 순서대로 들어간다
# init으로 올라간 값들이 self 를 따라서 주소값으로 찾아 들어가는 것

# print(tv1)
# returns the address of BasicTv object
# 여기서 직접 실행되니까 여기가 main 모듈 (그리고 이 메인 모듈이 오브젝 티비를 갖고 있다)

#주소값을 이렇게만 찾아갈 수 있어요:
# print(tv1.channel)
# print(tv1.power)
# print(tv1.volume)

# 클래스에서 변수를 선언할 때
# 밖에다가 변수를 선언할 수도 있다, 하지만 보통은 init 안에서 선언한다
# 개체가 만들어진 시점에 변수를 하나씩 추가 한다
# 이런 과정이 클래스의 설계를 가지고 객체를 설계한다

# 어렵다 ^0^!!!

# method 와 함수의 차이점: self
# method 는 첫번째 파라미터를  self 로 갖는다

# 우리가 텔레비전을 두개 이상 만들어 내면 주소값이 달라진다

# volvimos a intro
# volvimos a class01 despues de linea 38 en intro

# create a second TV
# 생성자는 클래스 이름과 똑같다
#tv2 = BasicTv(True, 100, 5)
# 말풍선에 self는 다른 파라미터들과 다르게 희미한 회색 빛깔을 띈다: 그건 우리가 주는게 아니다
# 이렇게 값을 주면, power 와, 채널과 볼륨을 갖는 티비 => 완전히 새로운 객체가 만들어진다

#tv2.channelDown()
# channel 99
# 방금 그 코드 그대로 들어가지만 주소 (-> self)가 바뀌어 있으므로 다른 값이 반환된다
# 기능은 같지만 객체들 마다 다른 데이터를 가지고 있으니까 다르게 작동한다

# 생성자 => 클래스라는 설계도를 가지고 공장에서 찍어주는 역할,,,? 그래서 뭐지 ㅠㅠ
# BasicTV 가 여기서 생성자
# 이 생성자를 변수에 넣어서 여러가지를 만들어 낼 수 있다 => 이 변수들, 객체들은 무한히 만들 수 있다
# 클래스와 이름이 똑같은 것 그게 생성자
# 우리가 만든 클래스에 객체를 생성할 때에는 tv1 = BasicTv(power = False, channel = 0, volume = 0) 요렇게 만든다,,,




