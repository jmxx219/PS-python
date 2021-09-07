from collections import deque

n = int(input())
dq = deque()
for i in range(1, n+1):
    dq.append(i)

while len(dq) != 1:
    dq.popleft()
    dq.append(dq.popleft())

print(dq.pop())


# n = int(input())
# s = 1
# while s<n:
#     s *= 2
# print(s if s == n else 2*n-s)