# November 12, 2019
# we were working on mymath1 y de repente lo creamos

"""
module03.py
"""
# we made utils package (folder directory)/ 유틸즈 패키지 안에 있는 mymath1 모듈 (파이썬 파일)의 기능들을 변수, 함수 들을 사용하고 싶다
# import 모듈이름 혹은 from 모듈이름 import 변수/함수, ...  혹은  from 패키지이름 import 모듈이름

# import mymath1 #이렇게만 하면 안된다 - 모듈이름은 패키지 안에 들어있다 (어떤 폴더 밑에 어떤 이름으로 있느냐가 전체 이름)
# C:\dev\lab-python\venv\Scripts\python.exe C:/dev/lab-python/LEC05_module/module03.py (경로 + 파일)
import utils.mymath1
# mymath1 은 module03 을 실행시켰다 그리고 module03 의 결과값들도 모두 출력됐다
# import 의 동작 원리: 최초로 동작할 때, 모든 파일들을 열어서 메모리에 올려 놓음. 그러니까 최초에 모두 한번은 실행된다.
# 이러한 원리 때문에 테스트가 끝났으면 지우거나 실행되지 않게 막아버려와 이렇게 실행되는 것을 막을 수 있다

# after we put a line "print(__name__)" on mymath1.py and did 'ctrl + shift + f10',
# en mymath1.py salio "__main__" y en module03 se salio "utils.mymath1"
# porq module had imported utils.mymath1 (자기 파일 이름을 반환해줌)
# "__name__" es una palabra prometida en Python a invocar su origen

#import utils.mymath1  /
from utils.mymath1 import pi
# pi 를 찾으려면 pi로 한번에 갈 수 없고, 패키지의 파일들을 처음부터 한줄 한줄 실행해줘야한다
# 그래서 둘 다 메모리 사용량은 같다

# import 문이 from utils.mymath1 import pi 이럴 때는 3번!
print('pi =', pi)
# 1) utils.mymath1.pi 2)mymath1.pi 3) pi

# import 문이 import utils.mymath1 일 때에는 1번 을 사용해줘야함
# print('pi=',utils.mymath1.pi)




