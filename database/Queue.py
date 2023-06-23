import collections

q = collections.deque()

q.append(1)
q.append(2)
q.append(3)

print(q)

q.popleft()
q.pop()

print(q)
