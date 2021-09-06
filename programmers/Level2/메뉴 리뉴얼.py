from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []

    for N in course:
        candidate = []
        for order in orders:
            candidate.extend(list(combinations(sorted(order), N)))

        # 카운터를 사용하여 중복되는 횟수를 셈
        counter = Counter(candidate)
        print(counter)
        if len(counter) > 0 and max(counter.values()) >= 2:
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]

    return sorted(answer)


if __name__ == "__main__":
    orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
    course = [2,3,4]
    print(solution(orders, course))