def solution(s):
    stack = []
    for x in s:
        if not stack:
            stack.append(x)
        elif stack[-1] == x:
            stack.pop()
        else:
            stack.append(x)

    return 1 if not stack else 0


st = "baabaa"
print(solution(st))