# BOJ 7562 Moving Knight
import sys
input = sys.stdin.readline

for T in range(int(input())):
    L = int(input())
    start = [*map(int, input().split())]
    end = [*map(int, input().split())]
    if start == end:
        print(0)
        continue
    visited = [[False]*L for _ in range(L)]
    # bfs
    stage = [start]
    visited[start[0]][start[1]] = True
    count = 1
    flag = False
    while stage:
        next_stage = []
        for a,b in stage:
            for c,d in [(a+2,b+1),(a+2,b-1),(a-2,b+1),(a-2,b-1),(a+1,b+2),(a+1,b-2),(a-1,b+2),(a-1,b-2)]:
                if 0<=c<L and 0<=d<L and not visited[c][d]:
                    if c == end[0] and d == end[1]:
                        print(count)
                        flag = True
                    else:
                        next_stage.append([c,d])
                        visited[c][d] = True
                if flag:
                    break
            if flag:
                break
        if flag:
            break
        count += 1
        stage = next_stage

