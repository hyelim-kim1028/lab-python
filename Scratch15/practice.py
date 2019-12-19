import math
from typing import NamedTuple
import numpy as np
import matplotlib.pyplot as plt
from collections import namedtuple, Counter, defaultdict

class Candidate(NamedTuple):
    level: str
    lang: str
    tweets: bool
    phd: bool
    result: bool = None

def uncertainty(p):
    """
    0 <= p <= 1
    확률이 p = 0 이면, 사건이 항상 발생하지 않는다 -> 불확실성 0
    확률이 p = 1이면, 사건이 항상 발생한다 -> 불확실성 0
    확률이 0 < p < 1 이면 사건이 발생할 수도 않을 수도 있다
    """
    return -p * math.log(p, 2) #2를 밑수로 하는 로그 함수

def entropy(class_probabilities):
    """
    주어질 확률들의 리스트에 대해서 엔트로피를 계산
    E = sum(i)[uncertainty(p_i) = -p_1 * log(p_1) - p_2 * log(p_2) ...
    """
    ent = 0
    for p in class_probabilities:
        if p != 0:
            ent += uncertainty(p)
    return ent

def binary_entropy(p):
    """
    사건이 일어날 확률 p, 사건이 일어나지 않을 확률 (1-p)
    Entropy = -p * log(p) - (1-p) * log(1-p)
    """
    return uncertainty(p) + uncertainty(1 - p)


def class_probabilities(labels):
    total_counts = len(labels)
    counts = Counter(labels)
    print(counts)
    probabilities = []
    for count in counts.values():
        p = count/total_counts
        probabilities.append(p)
    return probabilities

def partition_by(dataset, attr_name):
    """ NameTuple들의 리스트로 이루어진 dataset를 NameTuple의 특정 attribute로 partitioning """
    partitions = defaultdict(list)
    for sample in dataset:
        key = getattr(sample, attr_name)
        partitions[key].append(sample)
    return partitions

def partition_entropy_by(dataset, by_partition, by_entropy):
    partitions = partition_by(dataset, by_partition)
    labels = []
    for partition in partitions.values():
        values = []
        for sample in partition:
            values.append(getattr(sample, by_entropy))
        labels.append(values)
    print(labels)
    total_count = sum(len(label) for label in labels)
    ent = 0
    for label in labels:
        cls_prob = class_probabilities(label)
        part_ent = entropy(cls_prob)
        ent += part_ent * len(label)/total_count
    return ent





if __name__ == '__main__':
                         # level,    lang   , tweet, phd,  result
    candidates = [Candidate('Senior', 'Java', False, False, False),
                  Candidate('Senior', 'Java', False, True, False),
                  Candidate('Mid', 'Python', False, False, True),
                  Candidate('Junior', 'Python', False, False, True),
                  Candidate('Junior', 'R', True, False, True),
                  Candidate('Junior','R', True, True, False),
                  Candidate('Mid','R', True, True, True),
                  Candidate('Senior','Python', False, False, False),
                  Candidate('Senior', 'R', True, False, True),
                  Candidate('Junior', 'Python', True, False, True),
                  Candidate('Senior', 'Python', True, True, True),
                  Candidate('Mid', 'Python', False, True, True),
                  Candidate('Mid', 'Java', True, False, True),
                  Candidate('Junior', 'Python', False, True, False)]

    # uncertainty 함수 그래프
    x_pts = np.linspace(0.0001, 1, 100)
    y_pts = [uncertainty(x) for x in x_pts]
    plt.plot(x_pts, y_pts)
    plt.title('-p * log(p)')
    plt.xlim(0.0)
    plt.ylim(0.0)
    plt.show()