# BOJ 1697 Hide 'n Seek
n, k = map(int, input().split())
visited = set()


def bfs(start, end):
    global visited
    if start == end:
        return 0
    queue = [[start]]
    visited.add(start)
    count = 0
    while len(queue):
        stage = queue.pop()
        count += 1
        next_stage = []
        while len(stage):
            cur = stage.pop()
            for target in (cur - 1, cur + 1, cur * 2):
                if 0 <= target <= 100000 and (target not in visited):
                    if target == end:
                        return count
                    else:
                        visited.add(target)
                        next_stage.append(target)
        queue.append(next_stage)
    return -count


print(bfs(n, k))
