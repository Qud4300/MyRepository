import sys

input = sys.stdin.readline

n = int(input())
link = [[] for _ in range(n + 1)]
t = int(input())
for _ in range(t):
    i, j = map(int, input().split())
    link[i].append(j)
    link[j].append(i)
virus = [1]
visited = [0 for _ in range(n + 1)]
visited[1] = 1
for i in virus:  # BFS
    for c in link[i]:
        if visited[c] == 0:
            visited[c] = 1
            virus.append(c)
    for c in link[i]:
        try:
            link[i].remove(c)
            link[c].remove(i)
        except:
            continue
print(len(virus) - 1)
