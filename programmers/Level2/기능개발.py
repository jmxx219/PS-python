def solution(progresses, speeds):
    res = []
    stack = []
    for i in range(len(progresses)):
        tmp = (100 - progresses[i]) // speeds[i]
        day = tmp if (100 - progresses[i]) % speeds[i] == 0 else tmp + 1
        print(day, end=" ")
        if not stack or stack[0] >= day:
            stack.append(day)
        elif stack and stack[0] < day:
            res.append(len(stack))
            while stack:
                stack.pop()
            stack.append(day)
        print(stack)
    res.append(len(stack))
    return res


if __name__ == "__main__":
    progresses = [95, 90, 99, 99, 80, 99]
    speeds = [1, 1, 1, 1, 1, 1]
    print(solution(progresses, speeds))

