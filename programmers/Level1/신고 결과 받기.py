from collections import defaultdict


def solution(id_list, report, k):
    reports = set(report)
    answer = [0] * len(id_list)

    user_dict = defaultdict(list)
    cnt_dict = defaultdict(int)

    for r in reports:
        user, reported = map(str, r.split(" "))
        user_dict[reported].append(user)
        cnt_dict[reported] += 1

    for user in cnt_dict:
        if cnt_dict[user] >= k:
            for repo in user_dict[user]:
                answer[id_list.index(repo)] += 1

    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id_list, report, k))

id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3
print(solution(id_list, report, k))
