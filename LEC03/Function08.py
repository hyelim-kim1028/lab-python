# November 08, 2019
# 선택 정렬 알고리즘

import numpy as np

def find_min(numbers: list):
    '''
    주어진 리스트에서 최솟값과 최솟값의 인덱스를 찾아서 리턴
    :param numbers: 숫자들의 리스트
    :return: (최솟값의 인덱스, 최솟값) 의 쌍 (tuple)
    '''
    min_id, min_value = 0, numbers[0]
    for i, v in enumerate(numbers):
        if v < min_value:
            min_id, min_value = i,v
    return min_id, min_value

def find_max(numbers: list) -> tuple:
    max_id, max_value = 0, numbers[0]
    for i, v in enumerate(numbers): #enumerate는 i,v 를 순서대로 꺼내준다
        if v > max_value:
            max_id, max_value = i,v
    return max_id, max_value


# 선택 정렬 함수 만들기 (sel_sort)

# def sel_sort(numbers: list) -> list:
#     """
#     주어진 리스트의 원소들이 정렬된 새로운 리스트를 생성해서 리턴
#     주어진 리스트(파라미터에 전달된 리스트)의 순서는 바뀌지 않습니다
#
#     :param numbers:
#     :return:
#     """
#     result = [] #빈 리스트 생성
#     while numbers: # numbers의 원소가 있는 동안에 (python 에서는 0 = FALSE, 다른 숫자 = True, 빈 리스트도 false)
#         # numbers 에서 하나씩 원소를 꺼내는데, 비워 질때 까지 한다 라고 만든 것
#         _, min_value = find_min(numbers) # 이렇게 써주는 이유는, 앞에서 만든 함수에 변수가 2개라서
#         result.append(min_value) # 결과 리스트에 추가
#         numbers.remove(min_value) # 원본에서 최솟값 삭제 -> 원소가 없어 질 때 까지 반복
#     return result
#
# # 최솟값을 넣어주고, 지우고, 계속 반 복함으로써 sorted 된 리스트를 만드는 것
#
# def sel_sort2(numbers: list) -> None:
#     """
#     주어진 리스트를 정렬하는 함수
#     새로운 리스트를 생성하지 않고, 원본 리스트의 순서를 바꿈
#
#     :param numbers:
#     :return:
#     """
#     length = len(numbers)
#     for i in range(0, length - 1): # 마지막 하나있는 것은 비교의 대상이 없기 때문에 하나 전까지만 간다
#         # i 는 최솟값을 옮길 위치
#         for j in range(i + 1, length):
#             # j: 2번째로 작은 숫자가 들어갈 위치 (i 다음부터 마지막 숫자까지)
#             #   : 최솟값을 찾기 위해서 비교할 원소들의 인덱스
#             if numbers[i] > numbers[j]:
#                 numbers[i], numbers[j] = numbers[j], numbers[i] # swapped indices
#                 # 오른쪽은 바뀌기 전의 값들, 왼쪽이 바뀌는 값들
#                 print(numbers)
#
# # Example:
# print("=====================")
# numbers = [np.random.randint(0,100) for _ in range(10)]
# print(numbers)
# sel_sort2(numbers)
# print("===========")
# print(numbers)


# 파라미터 넣어보기
# sel_sort 함수에서 reverse 라는 boolean 타입의 파라미터를 F -> 오름차순, T -> 내림차순
# 그리고 reverse 의 기본값은 False 로 해주기

# sel_sort에 reverse라는 아이 넣어보기
def sel_sort(numbers: list, reverse:bool = False) -> list:
    """
    :param numbers:
    :param reverse: False인 경우는 오름차순, True 인 경우는 내림차순
    기본값은  False(즉, 오름차순 정렬)
    :return:
    """
    numbers_copy = numbers.copy() #원본 numbers list 를 사라지지 않게 하기 위해서
    result = [] #빈 리스트 생성
    while numbers_copy: # numbers의 원소가 있는 동안에 (python 에서는 0 = FALSE, 다른 숫자 = True, 빈 리스트도 false)
        # numbers 에서 하나씩 원소를 꺼내는데, 비워 질때 까지 한다 라고 만든 것
        if reverse == True: #내림차순 정렬 (find_max 함수를 위에 만들어준다)
            _, found = find_max(numbers_copy) #최댓값을 찾는다
        else: # False: 오름차순 정렬
            _, found = find_min(numbers_copy) #최솟값 찾음
        # T와 F에 공통된 코드이므로, 공통으로 만들어 준다
        result.append(found) # 결과 리스트에 추가
        numbers_copy.remove(found) # 원본에서 최솟/댓값 삭제
    return result

numbers = [np.random.randint(0,100) for _ in range(10)]
sorted_numbers = sel_sort(numbers) #오름차순 정렬
print(' ascending = ', sorted_numbers)
sorted_numbers = sel_sort(numbers, reverse = True) #내림차순 number
print('descending = ', sorted_numbers)

# sel_sort2 에도 똑같이
def sel_sort2(numbers: list, reverse:bool = False) -> None:
    """
    주어진 리스트를 정렬하는 함수
    새로운 리스트를 생성하지 않고, 원본 리스트의 순서를 바꿈

    :param numbers:
    :return:
    """
    length = len(numbers)
    for i in range(0, length -1):
        for j in range(i + 1, length):
            if reverse:
                if numbers[i] < numbers[j]:
                    # 리스트 맨 앞에 있는 값보다 더 큰 값을 찾았다면
                    # 서로 위치를 바꿔줌 (큰 값을 앞으로 이동)
                    numbers[i], numbers[j] = numbers[j], numbers[i]
            else:
                if numbers[i] > numbers[j]:
                    # 리스트 맨 앞에 있는 값보다 더 큰 값을 찾았다면
                    # 서로 위치를 바꿔줌 (작은 값을 앞으로 이동)
                    numbers[i], numbers[j] = numbers[j], numbers[i]

            print(numbers) #이렇게 되면 if/else 모두 출력

print('================================')
numbers2 = [np.random.randint(0,100) for _ in range(3)]
sorted_numbers2 = sel_sort2(numbers2) #오름차순 정렬
print(numbers2)
print('====================')
sorted_numbers21 = sel_sort2(numbers2, reverse = True) #내림차순 number
print(numbers2)

# 내가 생각한 방식 -> returned None
#     length = len(numbers)
#     if reverse == True:
#         for i in range(0, length - 1):
#             for j in range(i + 1, length):
#                 if numbers[i] > numbers[j]:
#                     numbers[i], numbers[j] = numbers[j], numbers[i]
#     else:
#         for i in range(0, length - 1):
#             for j in range(i + 1, length):
#                 if numbers[i] < numbers[j]:
#                     numbers[i], numbers[j] = numbers[j], numbers[i]
#     print(numbers)




