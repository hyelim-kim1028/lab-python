"""
1) csv파일 (stock_price.csv) write

이렇게 출력되는 파일
6/20/2019, AAPL, 90.91
6/20/2019, MSFT, 41.68
6/21/2019, AAPL, 90.86
6/21/2019, MSFT, 41.51

2) csv 파일을 csv.reader를 사용해서 파일의 내용을 리스트로 변환
 각 주식 종목에 주식 가격 평균을 계산해서 출력
3) csv파일을 csv.DictReader를 사용해서 파일의 내용을 리스트로 변환
각 주식 종목의 주식 가격 평균을 계산해서 출력 (컬럼 이름을 생성해주세요!)

csv — CSV File Reading and Writing:
https://docs.python.org/3/library/csv.html

"""

#1)
import csv

data = [
    ['6/20/2019', 'AAPL', 90.91],
    ['6/20/2019', 'MSFT', 41.68],
    ['6/21/2019', 'AAPL', 90.86],
    ['6/21/2019', 'MSFT', 41.51]
]

# 파일을 쓰기 모드로 열기
with open('stock_price.csv', mode = 'w', encoding= 'UTF-8', newline = '') as f:
    writer = csv.writer(f, delimiter = ',')
    for row in data: # in 데이터이름
        writer.writerow(row)
# newline = '' 은 write 할 때만 해주세욤!

# 2
# 파일을 읽기
with open('stock_price.csv', mode = 'r', encoding = 'UTF-8') as f:
    # csv reader객체 생성
    reader = csv.reader(f)
    # 파일에 한 줄씩 반복하며 읽어서 리스트에 추가
    df = [row for row in reader]
    print(df)
    # list 로 만들어주기ㅣ
    # [OrderedDict([('date', '6/20/2019'), ('company', 'AAPL'), ('price', '90.91')]), OrderedDict([('date', '6/20/2019'), ('company', 'MSFT'), ('price', '41.68')])]

# 종목별 평균 계산

# How I did (LOL)
print('avg price for AAPL =',((data[0][2]) + data[2][2])/2)
print('avg price for MSFT =',((data[1][2]) + data[3][2])/2)

# Teacher's solution
# AAPL 종목의 주식 가격들의 리스트
aapl_prices = [float(item[2]) for item in df
               if item[1] == 'AAPL']
# debes a poner float para ser el tipo numero
print(f'aapl_prices = {aapl_prices}, aapl_avg = {sum(aapl_prices)/len(aapl_prices)}')
# item 이 행이 된다
# mejor len(aapl_prices) que 2 porque en el mundo laboral, habria mucho mas variables
# entonces mas efficiente asi

msft_prices = [float(item[2]) for item in df
               if item[1] == 'MSFT']
print(f'msft prices = {msft_prices}, msft avg = {sum(msft_prices)/len(msft_prices)}')

# pr = []
# for i in df:
#     if i['stock'] == 'MSFT':
#         pr.append()
# 이런 코드를 list comprehension 으로 만든것

#3
# How I did
# with open('stock_price.csv', 'w', newline = '') as f:
#     fieldnames = ['date', 'company', 'price']
#     writer = csv.DictWriter(f, fieldnames = fieldnames)
#     writer.writeheader()
#     writer.writerow({'date':'6/20/2019', 'company':'AAPL', 'price':'90.91'})
#     writer.writerow({'date':'6/20/2019', 'company':'MSFT', 'price':'41.68'})
#     writer.writerow({'date':'6/20/2019', 'company':'AAPL', 'price':'90.86'})
#     writer.writerow({'date':'6/20/2019', 'company':'AAPL', 'price':'41.51'})
#
# with open('stock_price.csv', mode = 'r', encoding = 'UTF-8') as f:
#     reader = csv.DictReader(f)
#     df = [row for row in reader]
# print(df[0:2])

# teacher's solution
with open('stock_price.csv', mode = 'r', encoding= 'UTF-8') as f:
    # csv Dict Reader 객체를 생성
    # csv에 칼럼 이름이 없는 경우, 생성자에 fieldnames 파라미터를 설정하면 됨
    col_names = ['date', 'stock', 'price']
    reader = csv.DictReader(f, fieldnames=col_names)
    df = [row for row in reader]
print('df =',df)

aapl_prices = [float(item['price']) for item in df
               if item['stock'] == 'AAPL']
aapl_mean = (sum(aapl_prices)/len(aapl_prices))
print(f'aapl_prices = {aapl_prices}, aapl_mean = {aapl_mean}')

msft_prices = [float(item['price']) for item in df
               if item['stock'] == 'MSFT']
msft_mean = (sum(msft_prices)/len(msft_prices))
print(f'aapl_prices = {msft_prices}, aapl_mean = {msft_mean}')














