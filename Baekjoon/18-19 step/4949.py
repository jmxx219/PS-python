import re


def isValidPS(valid: list) -> bool:
    stack = []
    table = {
        ')': '(',
        ']': '['
    }
    for i in range(len(valid)):
        if valid[i] not in table:
            stack.append(valid[i])
        elif stack and stack[-1] == table[valid[i]]:
            stack.pop()
        else:
            return False
    return not stack


while True:
    t = str(input())
    if t == '.':
        break
    str_v = re.findall('[^a-zA-Z .]', t)
    if isValidPS(str_v):
        print("yes")
    else:
        print("no")
