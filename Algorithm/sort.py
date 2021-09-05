from typing import List


def selectionSort(N):
    for i in range(len(N) - 1):
        minLoc = i
        for j in range(i + 1, len(N)):
            if N[minLoc] > N[j]: minLoc = j
        if minLoc != i:
            N[minLoc], N[i] = N[i], N[minLoc]


def insertionSort(N):
    for i in range(1, len(N)):
        temp = N[i]
        j = i - 1
        while j >= 0 and temp < N[j]:
            N[j + 1] = N[j]
            j = j - 1
        N[j + 1] = temp


def bubbleSort(N):
    for i in range(len(N)):
        flag = False
        for j in range(len(N) - 1, i, -1):
            if N[j - 1] > N[j]:
                flag = True
                N[j - 1], N[j] = N[j], N[j - 1]
        if not flag: break


N = [8, 7, 6, 5, 4, 3, 2, 1]
selectionSort(N)
print(N)
N = [8, 7, 6, 5, 4, 3, 2, 1]
insertionSort(N)
print(N)
N = [8, 7, 6, 5, 4, 3, 2, 1]
bubbleSort(N)
print(N)
