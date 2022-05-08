# 숫자 카드
from sys import stdin


def solve():
    num_cards.sort()
    res = [0] * len(my_cards)

    for i in range(len(my_cards)):
        lo, hi = 0, len(num_cards) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if num_cards[mid] == my_cards[i]:
                res[i] = 1
                break
            elif num_cards[mid] < my_cards[i]:
                lo = mid + 1
            else:
                hi = mid - 1

    for x in res:
        print(x, end=" ")
    print()


N = int(stdin.readline()) # 숫자 카드 갯수
num_cards = list(map(int, stdin.readline().split()))
M = int(stdin.readline())
my_cards = list(map(int, stdin.readline().split()))
solve()
