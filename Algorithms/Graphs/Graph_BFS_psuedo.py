import deque

def BFS(G):
    n = len(G)
    visited = [False]*n
    parent = [-1]*n
    dist = [0]*n

    Q = Queue()
    for every sourceNodes s in G:
        Q.enque(s)
        while Q is not empty:
            v = Q.deque()
            visited[v] = True
            for every edges v->w:
                if visited[w] == False:
                    Q.enque(w)
                    parent[w] = v
                    dist[w] = dist[v]+1
