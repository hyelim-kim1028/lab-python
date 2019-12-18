"""
file open 모드(mode)
    r: read mode
    w: write mode
    a: append
"""

# 없는 파일을 읽으려고 하면: FileNotFoundError
# with open('NoFile.txt', mode = 'r') as f:
#     pass
# read mode는 파일이 존재하지 않으면 에러를 발생시키고 비정상적으로 종료시켜버린다
# write mode는 파일이 없으면 새로운 파일을 생성시킨다 그래서 에러가 발생하지 않는다.
            # 파일이 있으면 기존 파일을 열어줌. 단, 기존 파일의 내용이 삭제됨 (덮어쓰기 overwrite)

try:
    with open('NoFile.txt', mode = 'r') as f:
        pass
except FileNotFoundError:
    pass
# 이렇게하면 정상적으로 작동

with open('NewFile.txt', mode = 'w', encoding = 'utf-8') as f:
   f.write('test 테스트...')
# NewFile 이라는 파일은 없지만 write mode -> just created a new file (no error occurred)

with open('NewFile.txt', mode = 'w', encoding = 'utf-8') as f:
   pass
# what we wrote in lines 22-23 had been deleted (overwritten)
# 아무일도 하지 않더라도 파일의 내용이 삭제됨

# append mode
# 파일을 열어둔 상태에서 파일 포인터의 위치를 무조건 파일의 끝으로 갖다 놓는 것
# 열고 닫으면 아무일도 일어나지 않고 ,,, 응?

with open('Append.txt', mode = 'a', encoding = 'utf-8') as f:
    f.write('test\n')
    # If there is no existing file with the name, it creates one
    # If there is a file with the name, 기존 파일의 가장 마지막에 file pointer 가 위치함
    # 새로운 내용은 파일 끝에 추가(append)가 된다

with open('Append.txt', mode = 'a', encoding = 'utf-8') as f:
    f.write('추가...')

# when you check the file, you can see the lines are included without any deleted contents
# (unlike the write mode where it overwrites over the previous files)














