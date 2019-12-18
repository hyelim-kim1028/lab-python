"""
matplotlib.pyplot module 을 사용한 데이터 시각화
https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.html
- there is a button below named Terminal
- terminal > pip list > pip show matplotlib
- location: 패키지가 설치되어있는 파일 (설치가 되어있지 않으면 보여주지 않는다)
"""

# plotting을 위한 패키지 임포트
import matplotlib.pyplot as plt
# numpy - np, pandas - pd, pyplot - plt 이렇게 많이 쓴다

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# plt.plot()
# # first paramter is *args which means unlimited variables come as the first parameter, por eso, los que sigue despues tienen que ser 'keyword arguments'
#
# # plot(): 선 그래프 생성, show(): 그래프를 화면에 보여준다
# plt.plot(years, gdp)
# plt.show()
# # ctrl + q : se puede leer la descripcion

# customize the plot
plt.plot(years, gdp, color = 'green', marker = 'o')
# color = 'green' 을 주니까 선의 색깔이 초록색으로 바뀌었다
# marker = 'o' 하면 점을 찍어준다 (create dots on the line)
# plot 에 마우스를 대고 ctrl + q 를 해주면 ##kwargs 의 값들을 볼 수 있다

plt.title('Yearly GDP')
# puse '연도별 GDP' y no salio las letras en coreano - pero en ingles funciono perfectamente
# create a title for the graph
# fontname = 'D2Coding' 혹은 맑은 고딕과 같은 값을 주면 한글이 정상적으로 나온다

# we can also label x, y - axis
plt.xlabel('Year')
plt.ylabel('GDP(billions of $)')

# In order to save the image files yeilded from the activities, we created a directory named 'image_output'
# 그래프를 화면에다 보여줄수도 있지만 저장할 수도 있다 #savefig: 그래프를 이미지 파일로 저장
plt.savefig('../image_output/year_gdp.png')
# save -> show 순서대로해야 저장하고도 보임

plt.show()

# 막대 그래프 (bar chart)

# 영화 제목
movies = ['Annie Hall', 'Ben-Hur', 'Casablanca', 'Gandhi','West Side Story']
# 아카데미 시상식에서 받은 상의 갯수
num_oscars = [5,11,3,8,10]

# 이산 데이터 (불연속적으로 떨어져 있는 discrete data)

font_name = {'fontname':'Gulim'}
plt.bar(movies, num_oscars)
plt.title('아카데미 수상작 Academy Awarded', font_name)
          # fontname = 'Gulim' 을 계속 주는 대신에 made a variable
plt.ylabel('Number of Oscars 수상 갯수',font_name)
plt.show()

# plt.bar(num_oscars, movies)
# plt.show()
# 아예 다들 그래프가 되어버렸다 (not a good graph tho)
# 바뀌는걸 기대했는데 그렇게 되지 않았다 ㅠㅠ 잉잉

# histogram
grades = [83,65,95,91,87,70,0,85,82,100,67,73,77,0]
# range 를 주고 frequency 를 세서 그래프를 그려준다 -> 막대그래프 완서어엉
# x 좌표가 연속형,,, 둠칫두둠칫

from collections import Counter # 파이썬 기본 패키지
# collections 의 Counter package
# histogram = Counter(grades) # Counter({0: 2, 83: 1, 65: 1, 95: 1, 91: 1, 87: 1, 70: 1, 85: 1, 82: 1, 100: 1, 67: 1, 73: 1, 77: 1})
# too small values for each number (1 or 2) not applicable for histogram

# so instead we used this:
# [x for x in range(10)] -> muy parecido a como se funciona del list comprehension (tal vez lo intentare hacer)
plt.title('Grades_Counter') #얘 왜 안 예뻐지니
histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)
print(histogram)

# Counter({80: 4, 90: 3, 70: 3, 60: 2, 0: 2})
# 갯수를 세어 주었다 -> 규칙을 주었다 min(grade // 10 * 10, 90)
# 하지만 규칙이 이해가 안가는걸~ *.~
# grades list 에서 grade 를 하나씩 꺼내서
# // 나눈 몫만 계산해주기 (83 // 10 = 8 * 10 = 80 -> truncated the numbers
# min(80,90) => the min value will always be 80 or lower numbers than 90
# we put the numbers in min() because 90-99 will be in one range (90점대) but 100 has only one
# so in order to include 100 in the range of 90s, we put min( x, 90)

plt.bar(histogram.keys(), histogram.values())
plt.yticks([0,1,2,3,4,5])
plt.show()

# key 와 value 를 함께 꺼낼 때: items
# 위는 key 와 values 를 따로 꺼낼 때
# 근데 히스토그램이 왤케 빈약하냐,,, ㅎㅎ;;

# histogram 을 그려주는 함수
# grades list 를 이용해서 그려주기

plt.title('Grades_edge')
plt.hist(grades, edgecolor = 'black')
plt.yticks([0,1,2,3,4,5])
plt.show()
# counter class 사용하지 않아도 알아서 갯수를 세어주고, 그리고 그걸 가지고 히스토그램까지 알아서 그려준다 ^0^!
# bin 구간의 크기

# how many times people had mentioned the word 'data science'
plt.title('Mentioned Frequency')
mentions = [500,505]
years = [2013,2014] #년도가 의미없이 쪼개져서 x-axis 에 나온다 (discrete data 인데 continuous 인 마냥) -> not appropriate
plt.bar(years, mentions,0.5) # 0.5 = width (좀 얆아졌다)
plt.xticks(years) #tick - x축에 표시할 눈금 (이걸 주니까 2013, 2014 딱 떨어지게 출력)
                  # ytick - y 축에 표시할 눈금
plt.show()






























