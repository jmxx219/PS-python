from collections import defaultdict


def solution(today, terms, privacies):
    answer = []

    today = list(map(int, today.split('.')))
    termDict = defaultdict()
    for i in range(len(terms)):
        type, term = terms[i].split()
        termDict[type] = int(term)

    # print(today)
    # print(termDict)

    for i in range(len(privacies)):
        pri, type = privacies[i].split()
        priDay = list(map(int, pri.split('.')))

        priDay[1] += termDict[type]

        if priDay[1] > 12:
            priDay[0] = priDay[0] + priDay[1] // 12
            priDay[1] %= 12

        priDay[2] -= 1
        if priDay[2] == 0:
            priDay[2] = 28
            priDay[1] -= 1

        if priDay[1] == 0:
            priDay[1] = 12
            priDay[0] -= 1

        # 현재 날짜와 비교
        print(priDay)
        for j in range(3):
            if priDay[j] < today[j]:
                answer.append(i + 1)
                break

    return answer


print(solution("2022.05.19", ["B 6"],
               ["2021.07.01 B"]))

# print(solution("2022.05.19", ["A 6", "B 12", "C 3"],
#                ["2021.05.02 A", "2021.01.01 B", "2022.02.19 C", "2022.02.20 C"]))
# print(solution("2020.01.01", ["Z 3", "D 5"],
#                ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))