
G = graph()
visited = [False]*n
pre = []*n
post = []*n
parent = []*n

def recursive_DFS(v): #starts with rec_DFS(startNode)
    visited[v] = True
    pre[v] = currrentTime()
    for each edge v->w:
        if visited[w] == True: continue
        parent[w] = v
        rec_DFS(w)
    post[v] = currentTime()
    return

def iterative_DFS(G):
    Stack.push( (None,s) )
    while Stack is not empty:
        p, v = Stack.pop()
        parent[v] = p
        visited[v] = True
        print(v, end = ' ')
        for every edges (v,w):
            if w is unmarked:
                Stack.push( (v,w) )
