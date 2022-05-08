from sys import stdin


st1 = list(stdin.readline().rstrip())
M = int(stdin.readline())
st2 = []

for i in range(M):
    command = list(stdin.readline().split())

    if command[0] == 'L':
        if st1:
            st2.append(st1.pop())

    elif command[0] == 'D':
        if st2:
            st1.append(st2.pop())

    elif command[0] == 'B':
        if st1:
            st1.pop()

    else:
        st1.append(command[1])

st1.extend(reversed(st2))
print(''.join(st1))