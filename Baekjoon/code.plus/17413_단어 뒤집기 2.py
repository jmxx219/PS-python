S = list(input())

queue = []
stack = []
i = 0

while i < len(S):
    if S[i] == '<' or S[i] == ' ':
        while len(stack):
            queue.append(stack.pop())
    if S[i] == '<':
        while S[i] != '>':
            queue.append(S[i])
            i += 1
        queue.append(S[i])
    elif S[i] == ' ':
        queue.append(S[i])
    else:
        stack.append(S[i])
    i += 1

while len(stack):
    queue.append(stack.pop())

print(''.join(queue))
