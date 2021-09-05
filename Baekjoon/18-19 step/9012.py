def isValidPS(valid: list) -> bool:
    stack = []
    for i in range(len(valid)):
        if valid[i] == '(':
            stack.append(valid[i])
        elif stack:
            stack.pop()
        else:
            return False
    return not stack


t = int(input())

for i in range(t):
    if isValidPS(list(input())):
        print("YES")
    else:
        print("NO")
