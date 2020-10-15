# BOJ 2164 Card 2
from collections import deque
q = deque([i for i in range(1, int(input())+1)])
while len(q) > 1:
    q.popleft()
    q.append(q.popleft())
print(q[0])
