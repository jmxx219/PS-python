# 가장 긴 증가하는 부분 수열 2 - 이분 탐색
# 참고: https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-12015-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4-2-%EA%B3%A8%EB%93%9C2-%EC%9D%B4%EB%B6%84-%ED%83%90%EC%83%89

from sys import stdin


def findPlace(e, LIS):
    start = 0
    end = len(LIS) - 1

    while start <= end:
        mid = (start + end) // 2

        if LIS[mid] == e:   return mid
        elif LIS[mid] < e:  start = mid + 1
        else:   end = mid - 1

    return start


def solve():
    LIS = [nums[0]]

    for item in nums:
        if LIS[-1] < item:  LIS.append(item)
        else:
            idx = findPlace(item, LIS)
            LIS[idx] = item

    return len(LIS)


N = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
print(solve())