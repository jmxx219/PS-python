def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()

    a = []
    b = []

    for i in range(len(str1) - 1):
        if 'A' <= str1[i] <= 'Z' and 'A' <= str1[i + 1] <= 'Z':
            a.append(str1[i] + str1[i + 1])

    for i in range(len(str2) - 1):
        if 'A' <= str2[i] <= 'Z' and 'A' <= str2[i + 1] <= 'Z':
            b.append(str2[i] + str2[i + 1])

    # 다중합집합
    tmp = a.copy()
    union = a.copy()
    for c in b:
        if c not in tmp:
            union.append(c)
        else:
            tmp.remove(c)

    # 다중교집합
    intersection = []
    for c in b:
        if c in a:
            a.remove(c)
            intersection.append(c)

    if not union:
        return 65536
    return int(len(intersection) / len(union) * 65536)


st1	= "E=M*C^2"
st2 = "e=m*c^2"
# print(solution(st1, st2))