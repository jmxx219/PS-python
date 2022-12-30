
def isEndHomeIndex(n, deliveries, pickups):
    for i in range(n-1, -1, -1):
        if deliveries[i] > 0 or pickups[i] > 0:
            return i
    return -1


def solution2(cap, n, deliveries, pickups): # 재활용 택배 상, 집 개수, 배달할 상자, 수거할 상자
    answer = 0
    i = n-1

    while i >= 0:
        delTmp = cap
        pickTmp = 0
        i = isEndHomeIndex(n, deliveries, pickups)

        for j in range(i, -1, -1):
            if delTmp == 0 and pickTmp == cap:
                break

            if delTmp > 0:
                delTmp -= deliveries[j]
                if delTmp >= 0:
                    deliveries[j] = 0
                else:
                    deliveries[j] = delTmp * -1
                    delTmp = 0

            if pickTmp < cap:
                pickTmp += pickups[j]
                if pickTmp >= cap:
                    pickups[j] = pickTmp - cap
                    pickTmp = cap
                else:
                    pickups[j] = 0

        print(deliveries)
        print(pickups)
        answer += (i + 1) * 2

    return answer


def solution(cap, n, deliveries, pickups): # 재활용 택배 상, 집 개수, 배달할 상자, 수거할 상자
    answer = 0

    delTmp = cap
    pickTmp = 0

    i = isEndHomeIndex(n, deliveries, pickups)
    j = n - 1
    while j >= 0:
        if delTmp == 0 and pickTmp == cap:
            delTmp = cap
            pickTmp = 0
            answer += (i + 1) * 2
            i = isEndHomeIndex(n, deliveries, pickups)
            j = i

        if delTmp > 0:
            delTmp -= deliveries[j]
            if delTmp >= 0:
                deliveries[j] = 0
            else:
                deliveries[j] = delTmp * -1
                delTmp = 0

        if pickTmp < cap:
            pickTmp += pickups[j]
            if pickTmp >= cap:
                pickups[j] = pickTmp - cap
                pickTmp = cap
            else:
                pickups[j] = 0
        j -= 1

    if i != -1:
        answer += (i + 1) * 2

    return answer



# print(solution(1, 1, [0], [0]))

print(solution(2, 3, [1, 0, 1], [0, 1, 0]))

# print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
#
# print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))
