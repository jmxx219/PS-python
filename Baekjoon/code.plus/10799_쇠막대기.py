def solve():
    res = 0
    stack = []
    i = 0
    while i < len(st):
        if st[i] == '(' and st[i+1] == ')':
            res += len(stack)
            i += 1
        elif st[i] == ')':
            stack.pop()
            res += 1
        else:
            stack.append(st[i])
        i += 1
    return res


st = list(input())
print(solve())