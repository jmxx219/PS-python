def makeStrLength(split_data):
    i = 0
    j = 1
    res = ""

    while j < len(split_data):
        if split_data[i] == split_data[j]:
            j += 1
        else:
            res += split_data[i] if j - i == 1 else str(j - i) + split_data[i]
            i = j
            j += 1

    res += split_data[i] if j - i == 1 else str(j - i) + split_data[i]
    print(res)
    return len(res)


def solution(s):
    minLength = len(s)
    for n in range(1, len(s) + 1):
        # split_data = list(map(''.join, zip(*[iter(s)] * n)))
        # tmp = len(s) % n
        # if tmp != 0:
        #     split_data.append(s[-tmp::])
        split_data = [s[i:i + n] for i in range(0, len(s), n)]
        print(split_data)
        minLength = min(minLength, makeStrLength(split_data))

    return minLength





if __name__ == "__main__":
    s = "ababcdcdababcdcd"
    print(solution(s))



