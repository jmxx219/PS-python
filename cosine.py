# import
from numpy import dot
from numpy.linalg import norm
import numpy as np


# 코사인 유사도 함수
def cos_sim(A, B):
       return np.dot(A, B) / (np.linalg.norm(A) * np.linalg.norm(B))


def cos_sim2(A, B):
       return dot(A, B)/(norm(A)*norm(B))


# data
# item1=np.array([4, 2, 3, _])
# item2=np.array([3, 5, 1, 2])
# item3=np.array([_, 4, 2, 3])
# item4=np.array([1, 2, 5, 1])


# item1
print('item1과 item2 유사도: ', cos_sim(np.array([4, 2, 3]), np.array([3, 5, 1])))
print('item1과 item3 유사도: ', cos_sim(np.array([2, 3]), np.array([4, 2])))
print('item1과 item4 유사도: ', cos_sim(np.array([4, 2, 3]), np.array([1, 2, 5])))
print('item2과 item3 유사도: ', cos_sim(np.array([5, 1, 2]), np.array([4, 2, 3])))
print('item2과 item4 유사도: ', cos_sim(np.array([3, 5, 1, 2]), np.array([1, 2, 5, 1])))
print('item3과 item4 유사도: ', cos_sim(np.array([4, 2, 3]), np.array([2, 5, 1])))
print()
