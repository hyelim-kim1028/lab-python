"""

"""
import csv

# 문자열(string)을 아이템으로 갖는 리스트
row1 = ['test1','success','Monday']
row2 = ['test2','failure,kind of','Tue']
row3 = ['test3', 'success, kind of','Wed']
result = [row1, row2, row3] # result = list of three string lists
print(result)
# [['test1', 'success', 'Monday'], ['test2', 'failure,kind of', 'Tue'], ['test3', 'success, kind of', 'Wed']]

# 파일을 쓰기 모드로 열기
with open('test_result.csv', mode = 'w', encoding= 'UTF-8', newline = '') as f:
    # mode = 'w' for write
    # csv파일을 쓸 떄는 불필요한 라인이 써지지 않도록 하기 위해서 파일을 오픈할 때 newline = '' 파라미터를 추가!
    writer = csv.writer(f, delimiter = ',') # writer 객체를 생성을 하면 실제 파일에다 write 할 수 있다 (writerow 메소드)
    for row in result:
        # writer 객체의 writerow()메소드를 사용해서 한 줄씩 쓰기
        writer.writerow(row) # 파일에다 한줄 써준다...ㅎ0ㅎ

# 프로젝트 파일에 'test_result' 파일이 생성되어있다
# test1,success,Monday
# test2,"failure,kind of",Tue
# test3,"success, kind of",Wed
# R에서는 문자열이면 무조건 "" 로 묶어버렸다. 파이썬은 어떤것은 묶기도 하고 (중간에 쉼표가 들어가는 것) 어떤건 안 묶음
# csv라는 것은 쉼표로 컬럼들을 구문해주는 파일형식을 말하는데, 따옴표로 묶어주지않으면 안되니까,,,
# 사용하는 소프트웨어에 따라서 csv의 형식이 조금씩 다르다

print('\ncsv 모듈을 사용하지 않을 때')


# csv 모듈을 사용하지 않고 파일을 읽었을 때 어떤 문제점
with open('test_result.csv', mode = 'r', encoding = 'UTF - 8') as f:
    for line in f:
        print(line.strip().split(','))
        # 'failure, kind of' 라는 하나의 문자열이
        # '"failre' 가 'kind of"' 라는 두개의 문자열로 쪼개짐
        # 원래 데이터에는 없어야할 " 가 문자열에 포함됨

# ['test1', 'success', 'Monday'] # 문자열 모두에 '' 을 주었다 (작음 따옴표)
# ['']
# ['test2', '"failure', 'kind of"', 'Tue'] # 여기는 리스트가 4개짜리가 되었고, "" 가 앞뒤로 그냥 문자열로 취급되어 작은 따옴표로 들어가있음
# ['']                                     # 이렇게 되면 행과 열로 나누어진 테이블로 만들 수 없다
# ['test3', '"success', ' kind of"', 'Wed']
# ['']

# 만약에 우리가 이런걸 모두 take into consideration 하지 못 한다면, 모듈에 있는 csv
print('\ncsv 모듈을 사용할 때')
with open('test_result.csv', mode = 'r', encoding = 'UTF-8') as f:
    # csv reader객체 생성
    reader = csv.reader(f)
    for row in reader:
        print(row)

# csv 모듈을 사용할 때
# ['test1', 'success', 'Monday']
# []
# ['test2', 'failure,kind of', 'Tue']
# []
# ['test3', 'success, kind of', 'Wed']
# []
# 정상적으로  'success, kind of' 이렇게 처리되었다

# reader 객체의 read기능을 이용해서 한줄씩 읽음
# reader 객체를 생성하고, reader 객체의 메소드를 활동




























































