from sys import stdin


def solve():
    discovered = []
    for _ in range(S + 1):
        discovered.append([False] * (S + 1))

    queue = [[1, 0, 0]] # 이모티콘, clip, 시간
    discovered[1][0] = True

    while queue:
        emo, clip, currTime = queue.pop(0)

        if emo == S:
            return currTime

        # 1. 클립 복사
        if emo != clip and not discovered[emo][emo]:
            queue.append([emo, emo, currTime + 1])
            discovered[emo][emo] = True

        # 2. 클립 화면에 붙여넣기
        nextEmo = clip + emo
        if nextEmo <= S and not discovered[nextEmo][clip]:
            queue.append([nextEmo, clip, currTime + 1])
            discovered[nextEmo][clip] = True

        # 3. 삭제
        nextEmo = emo - 1
        if nextEmo > 0 and not discovered[nextEmo][clip]:
            queue.append([nextEmo, clip, currTime + 1])
            discovered[nextEmo][clip] = True


S = int(stdin.readline())
print(solve())