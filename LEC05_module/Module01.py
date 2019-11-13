# November 11, 2019
# chapter 06 들어가기

"""
Module: 확장자 .py를 갖는 파이썬 파일 (.py)
      : 변수, 함수, 클래스들이 정리된 스크립트 파일
Package: 파이썬 modules를 관련된 기능들끼리 모아서 저장한 폴더 (directory)
       : 패키지의 형태는 정말 개발자가 관리하기 나름
i.e. numpy 라는 package 안에 여러가지 파일들 (modules) 로 이루어져있다
- 패키지 안에 파일이 한개일 수도 있다

# 파이썬이 제공하는 기본 모듈들을 사용할 수도 있고, 우리가 만들어서 사용할 수 있는데
# import를 사용하면 외부 모듈을 가져다가 사용할 수 있다
# 기본 패키지/ 모듈 이외의 기능들을 사용할 때 import 구문을 사용함
import 모듈이름
from 모듈이름 import 기능(변수, 함수, 클래스 이름)
from 패키지 이름 import 모듈이름
"""

# 파이썬은 여러가지 수학 함수들과 상수들을 정의한 math 모듈이 있음
import math
# 폴더 + 파이썬 아이콘 : 모듈/파일1개, 폴더: 패키지
# math.py 파일 안에 정의된 함수들과 상수들을 사용할 수 있음
from scipy._lib._ccallback_c import sine_t

print(math.pi) #import 하지 않으면 사용하지 못 한다 (import 를 하지 않으면 name error 보여줌)
# print(pi) - Eventhough we had imported the package,we always have to put the package name -> OR NameError
# . math file 을 찾아가겠다 '.' 은 참조 연산자 라고 한다
# math가 가리키고 있는 곳에 있는 변수나 함수를 찾아가는 것
# 패키지가 다 실행이을 해서 호출을 해줘야 사용할 수 있으니까 import 가 실행해주는 것
# 그 이후에는 math 가 가지고 있는 여러가지 변수나 함수를 사용할 수 있는데, 그 때 사용해주는 것이 '.' 과 같은 참조 연산자
# 계속 똑같은걸 반복해서 실행하면 메모리를 너무 많이 차지하지 않는가?
# 그래서, 제일 처음 import 를 만날 때 딱 한번 파일을 오픈해서 해당 내용들을 실행을 해놓고 그 다음에 그 안에 있는 것들을 찾아가서 사용할 수 있게끔 한다
print(math.sqrt(2)) #모듈에 정의된 함수 사용 (root 2 값을 사용)

import numpy
# folder icon = directory
# we are calling all the files in the folder
# numpy.random.randint()

# from 모듈 import 변수 혹은 함수 이름
# from 디렉토리 import 디렉토리 파일 이름
from math import sqrt, pi, sin #같은 모듈이면 ',' 로 여러가지를 불러오는 것도 가능
# from math import pi
# from math import *  #math 의 모듈 안에서 모든 변수 이름, 함수 이름들을 가져오겠다
print(pi)
# 이 경우에는 math.pi 라고 쓰지 않는다 -> 이게 귀찮아서 imported pi
# print(math.sqrt())
print(sqrt(2))
# 이렇게는 안된다 => 우리가 가져온건 pi만 가져왔지, sqrt는 아니니까
# 전부 다 가져오고 싶으면 *
# pi = 3.14 #내가 임의로 math의 변수에 값을 주면
# pi, sin 모두 math 안에 있었다
print(sin(pi/2)) #1 이 아니라 0.99999 -> math 안의 모든 아이들이 다른 값을 주게 된다
print(sin(90))

# math안에 어떤 변수들이 있는지 모두 다 알고 있지 않는 한 파이썬 공식 문서를 보면
# 이렇게 하면 오류가 나올 수 있으니, * 보다는 각각을 불러오는 방법을 사용하라
# 각각 불러오면 내가 무엇을 불러왔는지 아니까 -> 더 조심하게될 것
# 조금 귀찮더라도 from import 를 쓸 때에는 하나씩 써주는게 에러를 방지할 수 있는 방법

# import ... (모듈이름, 패키지 이름) as 별명
import numpy as np
# Hereafter, we will name numpy as np
from math import pi as PI
# Hereafter, we will name pi as PI

# 파일을 한번 열었으면 늘 닫는 코드 (try 구문의 finally 와 같이) 가 있어야한다
# 닫지 않으면 다음에 다시 열 때 문제가 될 수도 있다















