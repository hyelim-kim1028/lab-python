"""
file.write 메소드를 사용한 csv 파일 작성
"""

import os
import numpy as np
# random number 사용하려고

#현재 폴더에 data 폴더 생성
# os.mkdir('data')
# when run twice, occurs an error (FileExistsError). To solve this problem, use:
try:
    os.mkdir('data')
except FileExistsError:
#현재 폴더에 data 폴더가 있으면 아무일도 하지 않음
    pass

file_name = os.path.join('data','exam.csv')
print(file_name)
# data\exam.csv
# 데이터 폴더 아래 exam.csv 를 사용하겠다 라는 뜻인데 there is no folder named data so we have to create one
# os.mkdir('data')

# 파일을 'w' /write 모드로 open 한다
with open(file_name, mode = 'w', encoding = 'utf-8') as output_file:
    # output_file: just a variable name
    output_file.write('id, 언어, 수리, 과탐, 사탐\n') # 쉼표로 구분되는 파일! csv 파일!!
    for i in range(1,11):
        line = f'{i},{np.random.randint(0,101)},{np.random.randint(0,101)},{np.random.randint(0,101)},{np.random.randint(0,101)}\n'
                #id, 언어                         , 수리                , 과탐                    , 사탐
        output_file.write(line)

#id, 언어, 수리, 과탐, 사탐1,17,100,17,21 -> put \n after 사탐
# output_file.write('id, 언어, 수리, 과탐, 사탐\n')



