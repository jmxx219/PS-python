def isProper(p):    # 올바른 괄호 문자열인지
    stack = []
    for x in p:
        if x == "(":
            stack.append(x)
        else:
            if not stack:
                return False
            stack.pop()

        return True


def split(p):   # 균형잡힌 문자열로 분리
    openP = 0
    closeP = 0

    for i in range(len(p)):
        if p[i] == '(':
            openP += 1
        else:
            closeP += 1
        if openP == closeP:
            return p[:i + 1], p[i + 1:]


def solution(p):
    if p == '':
        return p

    u, v = split(p)

    if isProper(u):
        return u + solution(v)
    else:
        tmp = '(' + solution(v) + ')'
        for p in u[1:len(u) - 1]:
            if p == '(':
                tmp += ')'
            else:
                tmp += '('
        return tmp


st = "()))((()"
print(solution(st))