#November 12, 2019
# utils package 안에 있는 mymath1, mymath2 모듈을 사용하고싶다
# logic:
#import numpy as np
#np.random.randint()
# np -> package, random -> module/file, randint -> function (더 작은? 걸로 들어가는 것)

import utils
# utils. (+ shift + space) showed nothing special
# from 패키지 import 모듈을 사용하면 이렇게 가져와서 사용가능
from utils import mymath1
from utils import mymath2
# 지금으로써는 이게 최선

print(mymath1.pi)
print(mymath2.divide(10,20))
# 모듈이름. 했을 때 밑으로 보여지는 아이들은 invoke-able 한 아이들이다

# C:\dev\lab-python\venv\Scripts\python.exe C:/dev/lab-python/LEC05_module/module04.py (경로 + 파일)
# 여기는 module04가 메인이다
# 그래서 python.exe 에서 있던 if 절안에 있는 아이들은 desaprecio
# 그리고 module04에서는 함수를 불러와서 사용가능 한 것

# 모듈이름들이 보이지 않았던 이유는 폴더의 구조적 이유 때문이다
# Whenever we created a package, there was a default file (__init__.py) followed by. without this, a package cannot be a package but a mere folder
# init.py is an empty folder but in order for a package to work as a package, one should have it
# if deleted, we can just make it with the same file name (__init__.py)








