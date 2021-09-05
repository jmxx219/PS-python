import collections

dq = collections.deque()
dq.append(1)
dq.append(2)
dq.append(3)
dq.appendleft(4)
print(dq)
print(dq.pop())
print(dq.popleft())
