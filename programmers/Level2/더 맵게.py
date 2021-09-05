import heapq


def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)

    while len(scoville) > 1:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        if first >= K:
            return cnt
        heapq.heappush(scoville, first + second * 2)
        cnt += 1

    return cnt if scoville[0] >= K else -1


if __name__ == "__main__":
    # scoville = [1, 2, 3, 9, 10, 12]
    scoville = [1, 1, 1, 1]
    k = 5
    print(solution(scoville, k))