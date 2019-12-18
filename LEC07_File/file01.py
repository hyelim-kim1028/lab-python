"""
os module의 변수와 함수들

"""
import os

print(os.getcwd())
# C:\dev\lab-python\LEC07_File
# cwd = current working directory
# 파일들을 어디서 읽어오고 저장하는지 알아야하니까 중요!

# 절대 경로 (absolute path)
# 시스템의 루트(root)부터 전체 경로를 표시하는 방법
# C:\dev\lab-python\LEC07_File => root C:\ 부터 전부 표시하는 방법 -> 이건 windows 표기 방법
# /Users/user/Documents (MacOS 또느 Linux)
# separator windows 는 \, MacOs or Linux use /
# 상대 경로 (relative path):
# LEC07 -> working directory , but I want to go to lec06
# so what we do is from lec07 -> go to lab-python (..\) -> and then go back to lec06 (LEC06 - class\inheritance01.py)
# ..\LEC06 - class\inheritance01.py
#.\file01.py 와 file01.py 는 같은 뜻이다!

print(os.name) #os 종류 확인
#nt : one of the versions of windows
#Linux: posix
#Macos:

if os.name == 'nt': #Windows OS 인 경우
    file_path = '.\\temp\\temp.txt' # \\두개 써야대! (문자열에서 \ 는 특별한 용도로 사용이 된다)
# \n : 줄바꿈, \t: 탭
# / 는 그럴필요가 없다: 특별한 용도로 사용되지 않기 때문에
else: # Windows 이외의 OS 인 경우
    file_path = './temp/temp.txt'
print(file_path)

# 매번 파일을 다룰 때 마다 이렇게 할 수 없으니까
# 파일 구분자 (file separator) 를 해당 OS에 맞게 경로를 만들어줌
file_path = os.path.join('temp','temp.txt')
print(file_path)
# 그래서 os.path.join 은 os 에 따라서 returned value(?) phrase(?) 가 달라진다

print(os.path.isdir('.'))
# absolute (절대경로)
# True -> 현재 디렉토리 입니다
print(os.path.isdir('file01.py'))
# returned false since file01.py is a file not a directory
print(os.path.isfile('.'))
# returned flase since '.' directory is not a file
print(os.path.isfile('file01.py'))

# file & directory both belong to file class
# file is a narrower concept of file than directory (directory is also called as file since ever before)

with os.scandir('.') as my_dir:
    # 현재 디렉토리를 검색하겠다, 그리고 그 검색한 내용을 my_dir에 저장하겠다
    # my_dir is in a list form (different folders and files exists)
    for entry in my_dir:
        print(entry.name, '\t',entry.is_file())
# returns how many folders are in the directory (lec07 - file):
# file01.py 	 True
# __init__.py 	 True
# file name      is_file
# inserted '\t' and there is a space between the two

# scandir 도 리소스였다 그래서 with 구문을 사용
# 파일 객체는 사용하고 나면 무조건 닫아줘야함


# 파일(directory) 이름 변경:
# os.rename('temp','test')
# os.rename(원본 이름, 바꿀 이름)
# FileNotFoundError: [WinError 2] 지정된 파일을 찾을 수 없습니다: 'temp' -> 'test'
# Here, the file refers to the broad meaning of file (both directory and file)
# Cannot be run twice, once the name of the folder had been changed, it is impossible to run it again
# 원본 파일(디렉토리)가 없는 경우에 에러 발생
try:
    os.rename('temp','test')
except FileNotFoundError:
    print('temp 폴더가 없음')
# returns temp 폴더가 없음


# # file 이나 folder 을 삭제
# os.remove('test')
# # os.remove('폴더이름')
# # PermissionError: [WinError 5] 액세스가 거부되었습니다: 'test'
# try:
#     os.remove('test')
# except PermissionError:
#     print('삭제 권한 없음')
# # 엑세스 거부,,,, :(


# 디렉토리 만들기: os.mkdir
# os.mkdir(디렉토리 이름)
# os.mkdirs(디렉토리 이름)
# os.mkdir('test2')
# # os.mkdirs('test2\\temp') # test2 밑에 temp 를 만들려고 했는데 에러가 나벌임
# # 문제: 만드는건 되는데 삭제하는건 안댐
# # FileExistsError: [WinError 183] 파일이 이미 있으므로 만들 수 없습니다: 'test2'
# os.makedirs('test2\\temp')
# # FileExistsError: [WinError 183] 파일이 이미 있으므로 만들 수 없습니다: 'test2'

try:
    os.mkdir('test2')
except FileExistsError:
    print('test2 폴더가 이미 있음')

# rename: file or directory 이름을 바꾼다
# 파일 삭제: os.remove(삭제할 파일 이름)
# 디렉토리 삭제: os.rmdir(삭제할 폴더 이름)
# try:
#     os.rmdir('test')
#     print('temp 폴더가 삭제됨')
# except PermissionError:
#     print('삭제 권한 없음')
# 주석 처리 해줌: 왜냐하면 삭제 했는데 또 하면 exception 발생

# what is the difference between mkdir vs mkdirs?
# os.mkdir('test\\temp')
# this is not possible (filenotfound)
# 에러가 나는 이유는 test 폴더가 없기 때문에 그 하위 폴더를 생성할 수 없음
# os.makedirs('test\\temp')
# 하지만, 이렇게하면 정상실행된다 (폴더 내용을 확인하면 test -> temp 라는 하위 폴더 까지!)
# os.mkdir 을 사용하려면 중간단계 폴더가 만들어져 있어야 생성할 수 있다
# 생성되어있으니까 다시 하려면 에러가 날테니 try - except 로 묶는다

try:
    # os.makedirs('test\\temp')
    os.makedirs(os.path.join('test','temp'))
    print('test\\temp 폴더 생성 성공')
except FileExistsError:
    print('test\\temp 폴더가 이미 있음')

# mkdir 과 makedirs 를 구분해서 사용하자!
# try - except 는 안좋은 코드들! 왜냐하면 \\ 은 windows 에서만 사용하니까
# 그래서  os.makedirs(os.path.join('test','temp')) 이런 코드를 쓰는게 더 좋다

# https://docs.python.org/3/library/os.html
























































