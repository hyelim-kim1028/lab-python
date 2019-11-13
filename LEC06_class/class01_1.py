class BasicTv:
    """
    BasicTv 클래스
    """
    # 클래스 내부에서 선언하는 변수: field
    # channel/volume 을 위해 새로운 변수 선언
    # the variables claimed outside are fixed values
    max_channel, min_channel = 5,0
    max_volume, min_volume = 5,0

    # 데이터를 설계할 때에는 함수를 하나 만든다
    # 생성자가 호출됐을 때 실행되는 메소드 (함수)
    def __init__(self, power, channel, volume):  # 다른이름을 쓰면 안되고 항상 init을 사용해야한다
        # 전원, 채널, 음향
        # los variables dentro de __init__, se producian con diferentes numeros/informaciones cada vez que se produzcan
        print('BasicTv 생성자 호출')  # with this the class works
        self.power = power  # power in the parameter
        # parameter power to be saved in a variable self.power
        self.channel = channel  # channel in the parameter
        self.volume = volume

    # 클래스 내부에서 정의하는 함수: 메소드
    # 텔레비전 소프트웨어에서 전원을 on/off하는 기능 만들어 보기
    def powerOnOff(self):  # powerOnOff 에서 ()를 넣어주니까 자동으로 self를 만들어 주었다
        if self.power == True:  # power = True (TV가 켜져있으면)
            self.power = False  # TV가 켜져있는 상태에서 버튼을 눌렀으니까 => TV를 끔
            print('TV off')
        else:  # TV가 꺼져있으면
            self.power = True  # TV가 꺼져있는 상태에서 버튼을 눌렀으니까 => TV를 켬
            print('TV on')

    # def controller(self):
    #     if self.power == False:
    #         self.channel = False
    #         self.volume = False
    #     else:
    #         self.channel <= 0
    #         self.volume <= 0

    # 기능: 채널변경
    # 채널의 볼륨업 과 다운이 각각 다른 메소드면 좋겠다
    def channelUp(self):
        # 텔레비젼이 켜져있는 상태에만 동작하도록
        if self.power == True:
            if self.channel < self.max_channel:
                # 현재 채널값이 채널의 최댓값보다 작으면
                self.channel += 1
                # print('Channel:', self.channel) #얘가 있으면 모든 값이 2번씩 출력된다
        # channel 이 max = 5 를 찍으면 -> 0 으로 바뀐다
            else:
                # 현대 채널값이 채널 최댓값과 같으면 0으로 순환
                self.channel = self.min_channel
            print('Channel: ',self.channel)

        # if self.channel == 5:
        #     self.channel += 1
        #     print('Channel: 0')

        # for loop 으로 만들어주나?
        # for c in self.channel(6):
        #     self.channel += 1
        #     print('Channel: ', self.channel)
        #     if self.channel == 5:
        #         print('Channel: 0')

    def channelDown(self):
        if self.power == True:
            if self.channel > self.min_channel:
                self.channel -= 1
            # print('Channel:', self.channel)
        else:
            self.channel = self.max_channel
            #현재 채널이 최솟값인 경우는 채널 최댓값으로 순환
        print('Channel: ', self.channel)

        # if self.channel == 0:
        #     print('Channel: 5')

    # 볼륨 업/다운 기능
    def volumeUp(self):
        # TV가 켜져있는 경우에만 음량 +1
        if self.power:
            if self.volume < self.max_volume:
               self.volume += 1
               print('Volume:', self.volume)
        # 순환시키는게 아니라 그냥 놔두면 된다 (else가 필요없다)

    def volumeDown(self):
        if self.power:
            if self.volume > self.min_volume:
                self.volume -= 1
            print('Volume:', self.volume)
        # if self.volume <= 0:
        #     print('Volume: 0')

# tv1 = BasicTv(power = False, channel = 0, volume = 0)
# ctrl 을 누른채로 BasicTv에 마우스를 클릭하면 init으로 돌아간다. 왜냐하면 클래스의 생성자 라고 인식하기 때문
# init 은 크래스 이름을 함수처럼 호출 했을 때 나타난다?

# power func practice
# print(tv1)
# print(tv1.power) #텔레비전이 꺼져있는 상태
# tv1.powerOnOff() # 텔레비젼이 켜졌다 #method 는 tv1 과 같이 변수
# # How it functions: go back to def powerOnOff(self) => tv1 became 'self' itself
# # channel func practice
# tv1.channelUp() # channel func must work only when TV is on


if __name__=='__main__':
    #클래스의 객체(인스턴스)를 생성해서 변수에 저장
#   # 생성자(constructor) 호출 -> 객체 (object) 생성
    tv3 = BasicTv(False,0,0)
    print('전원상태: ', tv3.power)
    tv3.channelUp()
    tv3.powerOnOff()#TV켬
    tv3.channelUp()
    tv3.channelUp()
    tv3.channelUp()
    tv3.channelUp()
    tv3.channelUp()
    tv3.channelUp()
    tv3.channelUp()
    tv3.channelDown()
    tv3.channelDown()
    tv3.channelDown()
    tv3.channelDown()
    tv3.channelDown()
    tv3.channelDown()
    tv3.channelDown()
    tv3.channelDown()



# 이렇게 ctr + c  ctrl + v 도 지친다,,,^^;;
for _ in range(10):
    tv3.volumeUp()

for _ in range(10):
    tv3.volumeDown()

for _ in range(10):
    tv3.channelDown()

# channelDown 코드 다시 한번 보기


