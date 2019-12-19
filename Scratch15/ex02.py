# NamedTuple을 상속받는 클래스 선언
import math
from typing import NamedTuple
import numpy as np
import matplotlib.pyplot as plt
from collections import namedtuple, Counter, defaultdict


# Candidate = namedtuple('Candidate', ('level','lang','tweets','phd','result'))
class Candidate(NamedTuple):
    """NamedTuple을 상속받는 클래서 선언"""
    level: str
    lang: str
    tweets: bool
    phd: bool
    result: bool = None #set default value as None
    # Using the inheritance method (#C), we can set the default values in variables
    # the Python method(#A) has no such option

c1 = Candidate('','',True,True)
# When using Python method, we cannot skip a single column, but inheritance method can

def uncertainty(p):
    """0 <= p <= 1
        확률이 p = 0이면, 사건이 '항상' 발생하지 않는다 -> 불확실성 0
        확률이 p = 1이면, 사건이 '항상' 발생한다 -> 불확실성 0
        확률이 0 < p < 1 이면 사건이 발생할 수도 않을 수도 있다 -> 불확실성이 있다 """
    return -p * math.log(p, 2) #2를 밑수로 하는 로그 함수
    # log2X = y => X = 2^y


def entropy(class_probabilities):
    """ 주어질 확률들의 리스트에 대해서 엔트로피를 계산
        E = sum(i)[uncertainty(p_i)] = -p_1 * log(p_1) - p_2 * log(p_2) ... """
        # f(p) = 사건 1개에 대한 확률 = plog2P
        # 날씨가 맑을 확률 + 비올 확률 = 1
        # 모든 정보의 불확실성을 다 합친 것 -> entropy
        # 예를 들어, there are three levels ( junior, mid and senior). Each level's uncertaity is calculated by f(p)
        # But the uncertainty of all three leves using Entropy (Thus, the Entropy for levels)
        # what about the uncertainty of language (Java, R, Python)?
        # the uncertainty of each category is using f(p), however, the uncertainty of all three categories is using ENTROPY
    ent = 0
    for p in class_probabilities:
        if p != 0:
            ent += uncertainty(p)
            # 확률은 0이 나올 수 있지만, 로그함수의 계산이기때문에 0이 오지 못한다 -> 에러
            # 이렇게해도 상관 없음: 더하지 않는다 = 더하기 0
    return ent



def binary_entropy(p):
    """ 사건이 일어날 확률 p, 사건이 일어나지 않을 확률 (1 - p)
        Entropy = -p * log(p) - (1-p) * log(1-p) """
    return uncertainty(p) + uncertainty(1 - p)
    # 두 가지 경우 밖에 존재하지 않을 때


def class_probabilities(labels):
    # 부분/전체
    total_counts = len(labels)
    counts = Counter(labels)
    print(counts)
    probabilities = []
    # for count in counts: 이렇게하면 key 값만 뽑아줌
    for count in counts.values(): #우린 count가 필요
        p = count/total_counts #각 레이블의 확률
        probabilities.append(p) # we do not know what would come
        # can also be written in list comprehension:
        # lines from probabilities = []  to  probabilities.append(p) will be reduced to
        # probabilities = [count/total_count for count in counts.values()]
    return probabilities

# Using list comprehension
# def class_probabilities(labels):
#     # 부분/전체
#     total_counts = len(labels)
#     counts = Counter(labels)
#         probabilities = [count/total_count for count in counts.values()]
#     return probabilities

def partition_by(dataset, attr_name):
    """ NameTuple들의 리스트로 이루어진 dataset를
        NameTuple의 특정 attribute로 partitioning """

    partitions = defaultdict(list) # key값이 없으면 생성해주고, key값이 있으면 자기의 카테고리로 보내주는 함수
    for sample in dataset: #dataset = candidates 가 들어온다
        # each row (here, sample) of df will be retrieved
        # sample.attr_name # attr_name 함수는 이 자체가 이름이여야해서 쓸 수 없다?
        key = getattr(sample, attr_name)
        # dict의 키로 사용함
        partitions[key].append(sample) # != partitions[key] = sample/ 값을 그냥 덮어써버리는
    return partitions

def partition_entropy_by(dataset, by_partition, by_entropy):
   """attr_name으로 분리된 각 파티션에서 label_name의 entropy를 각각 계산하고
      파티션 내에서의 엔트로피 * 파티션의 비율들의 합을 리턴 """
#파티션을 나눔
   partitions = partition_by(dataset, by_partition)
        # 클래스(레이블)별 확률을 계산하기 위해서 레이블들의 리스트를 생성
   labels = []
   for partition in partitions.values(): #파티션 개수만큼 반복 # 전체 집합에서 부분집합을 꺼냄
       values = [] #각 파티션에 속한 샘플들을 찾아서
       for sample in partition: #파티션의 원소 개수만큼 반복 # 부분집합에서 원소를 꺼냄
            values.append(getattr(sample,by_entropy))
                                    # result 만 뽑는다 (true/false) 그리고 그것을 label의 append
       labels.append(values) # 그 결과가 파티션별로, 파티션의 length만큼 나온다
   print(labels)
   # 각 파티션이 차지하는 비율을 계산하고, 각 파티션에서의 엔트로피에 그 비율을 곱해주기 위해서
   total_count = sum(len(label) for label in labels)  # 밑으로 내려가는 것 까지 생각하기 위해서 # 위에서 구한 label을 가지고 계산
   # lables = 3개의 리스트가 있고, 각 리스트당 5개 혹은 4개의 원소가 있다
   # 리스트의 길이를 세어주고, 더함, 전체 15명~ 하고 말해줌
   # 서브파티션을 만들고, 그 리스트를 5 - 2,3명 이런식으로 만들어 줄 수도 있다
   ent = 0
   for label in labels:
       # 파티션이 가지고 있는 클래스들의 확률 리스트 # [2/5, 3/5] 와 같은 값을 리턴
       cls_prob = class_probabilities(label) # 확률이 나왔으니 계산할 수 있다
       part_ent = entropy(cls_prob) # 파티션 엔트로피
            # 파티션 엔트로피 * 파티션 비율
       ent += part_ent * len(label) / total_count # 전체에서 파티션이 차지하는 비율
   return ent

# 목표: target으로 도착
    # 면접 결과를 두고 계산을 할 수 있고, partition을
    # Entropy =  P(junior > true or false) + (senior > true or false) + (mid > true or false)
    # 합격했느냐 실패했느냐에대한 엔트로피(불확실성)을 계산하고 싶은 것
    # 백지상태에서 15명(total population)의 합격/불합격여부밖에 나오지 않지만, partition 을 하면?
    # 각 변수별로의 엔트로피를 구하고, 그 엔트로피들의 총 합을 구한다
    # 이게 final






if __name__ == '__main__':
    # candidates 객체? array? 생성
    candidates = [Candidate('Senior', 'Java', False, False, False),
                  Candidate('Senior', 'Java', False, True, False),
                  Candidate('Mid','Python', False, False, True),
                  Candidate('Junior','Python', False, False, True),
                  Candidate('Junior','R',True, False, True),
                  Candidate('Junior', 'R', True, True, False),
                  Candidate('Mid', 'R', True, True, True),
                  Candidate('Senior', 'Python', False, False, False),
                  Candidate('Senior', 'R', True, False, True),
                  Candidate('Junior','Python', True, False, True),
                  Candidate('Senior', 'Python', True, True, True),
                  Candidate('Mid', 'Python', False, True, True),
                  Candidate('Mid', 'Java', True, False, True),
                  Candidate('Junior', 'Python', False, True, False)]
    # 첫 질문이 중요하다: 그려지는 트리의 모양이 달라진다
    # 갈라지고 갈라지고 갈라지고 하면서 결정하는 것
    # 짦게 맞출수록 좋다 (최종적으로 나오는 leaf의 갯수가 가장 적게 나오는 것이 목표)
    # 최종 leaf가 적다고 해서 늘 좋은 세트/모델은 아니다 -> 정답지로 만드는 모델이기 때문에, 새로운 예시가 들어가면 오답률이 높다 (overfitting?)

    # drawing a tree with the least leaf possible # 어떻게 질문을 던져야 가능?
    # Entropy = uncertainty?
    # https://medium.com/coinmonks/what-is-entropy-and-why-information-gain-is-matter-4e85d46d2f01
    # https://towardsdatascience.com/entropy-how-decision-trees-make-decisions-2946b9c18c8

    # uncertainty 함수 그래프

    # uncertainty 함수 그래프
    x_pts = np.linspace(0.0001, 1, 100) # 0~1 까지의 숫자를 100가지의 구간으로 잘르겠다
                                        # 0이 아니라 0.0001을 준 이유: math.log 의 그래프는 0에 닿지 않으니까
    y_pts = [uncertainty(x) for x in x_pts]
    plt.plot(x_pts, y_pts)
    plt.title('-p * log(p)')
    plt.xlim(0.0) # 시작점 0.0을 준다; 의미: 0 <= X, 그리고 이 값보다 작은 부분은 그리지 않겠다
    plt.ylim(0.0) # 시작점 0.0을 준다; 의미: 0 <= y 그리고 이 값보다 작은 부분은 그리지 않겠다
    plt.show()
    # mid = 4/4; P = 1 or senior = 0/4; p = 0
    # 확률이 0 혹은 1 이면 불확정성이 없는 것
    # 0 과 1 사이의 불확정성(entropy)를 보여주는 그래프

    # binary_entropy 함수 그래프
    x_pts = np.linspace(0.0001, 0.999, 100) # Entropy = -p * log(p) - (1-p) * log(1-p) 이기 때문에, 1 이 들어오면 0이되어버리기 때문에 성립이 되지 않는다.
                                            # 그러므로 최댓값을 1보다는 적은 값을 주어야한다
    y_pts = [binary_entropy(p) for p in x_pts]
    plt.plot(x_pts, y_pts)
    plt.title('binary entropy')
    plt.axvline(0.5, color = '0.75')
    plt.xlim(0)
    plt.ylim(0)
    plt.show()

   # entropy 함수 테스트
    rain_prob = [1] #1 = 백프로 비가 온다, 0 = 백프로 비가 오지 않는다
                    # 확률이 1개 밖에 없다
    ent = entropy(rain_prob)
    print('entropy =', ent) # entropy = 0.0 확실한 경우니까 -> 노 불확실성

    rain_prob = [0.5, 0.5] #확률은 합쳐서 1이 되어야한다 (올 확률 0.5, 오지 않을 확률 0.5)
    ent = entropy(rain_prob)
    print('entropy =', ent) # entropy = 1.0 -> max 불확실성 (비가 올 수도 있고, 오지 않을 수도 있다)

    rain_prob = [0.9, 0.1] #비가 올 확률 90% 일 때
    ent = entropy(rain_prob)
    print('entropy =', ent) # ent = 0.468

    # decision tree에서 entropy가 가장 낮은 변수를 첫번째 질문으로 채택

    #class probabilites 함수 테스트
    level = ['junior', 'senior', 'mid', 'junior']
    # what we want to find out: P(junior) = 2/4, P(mid) = 1/4, P(senior) = 1/4
    cls_prob = class_probabilities(level)
    print('cls_prob =',cls_prob)
    # class probabilities 를 만든 이유: 카테고리 리스트를 함수에 넣어서 각 원소의 확률들을 알아내서 entropy를 계산할 수 있게 하기 위해서

    # Entropy 계산
    # level 이라고 하는 attribute의 entropy를 계산하려면 원소들을 나누어주어야한다
    # 전체집합을 원소별로 grouping/모으는 것: partitioning
    # Level attribute can be partitioned into : junior, mid, senior
    # Language attribute can be partitioned into: Python, R, Java
    # But the pies of two partitioning can be different
    # the partition of level is evenly distributed, but the partition of language weighs the most on Python
    # target: entrance/passing rate
    # 새로운함수 partition_by 생성

    # partition_by 함수 테스트
    partition_by_level = partition_by(candidates, 'level')
    print('partition_by_level',partition_by_level)
    # 결과값을 보면, level 들이 senior, mid, junior로 나뉘어져서 각각 다른 리스트에 들어가있다
    # 그 후에는 각 레벨들에 해당하는 파티션을 만들어서 엔트로피를 계산 -> 결과값에 따라 또 파티션닝 & 엔트로피 ,,, 들어가고 들어가고 들어가고
    partition_by_tweet = partition_by(candidates, 'tweets')
    print('partition_by_tweets', partition_by_tweet)
    # the df_candidates partitioned by the usability(?) of Twitter

    #partition_entropy_by 함수 테스트
    # 전체 지원자들을 level로 파티션을 나눠서 result의 엔트로피를 계산
    ent_level =  partition_entropy_by(candidates, 'level', by_entropy= 'result')
    print('entropy partitioned by level:', ent_level)
    # [[False, False, False, True, True], [True, True, True, True], [True, True, False, True, False]]
    # entropy_partitioned_by_level: 0.6935361388961919
    ent_lang = partition_entropy_by(candidates, 'lang', 'result') # 어떠한 partition에 관해서 True의 확률로 합격이 될 것이다 # sum of all the entropies (비율별로)
    print('entropy partitioned by lang = ', ent_lang) # 0.8601317128547441
    ent_tweets = partition_entropy_by(candidates,'tweets','result')
    print('entropy partitioned by tweets =', ent_tweets) # 0.7884504573082896
    ent_phd = partition_entropy_by(candidates,'phd', 'result')
    print('entropy partitioned by phd =', ent_phd) # 0.8921589282623617
    # 불확실성이 높을 수록 가지가 많아진다 = 가능성이 많아지는 것
    # 가장 높은 entropy를 가진 아이로 시작하면 (i.e. ent_phd) - true/false 로 해서 계속해서 질문을 해나가는 것
    # 불확실성이 가장 낮은 아이를 먼저 시작하는 것이 좋다 (i.e. level 로 하면 mid는 시작하자마자 끝난다)
    # 그러면 leaf가 가장 적은 모델이 된다