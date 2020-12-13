# BOJ 2263 Tree Traversal
from collections import deque

n = int(input())
inorder = [*map(int, input().split())]
postorder = [*map(int, input().split())]


def preorder(n, mid, post):
    res = []
    queue = deque([[0, n-1, 0, n-1]])
    loc = [0 for _ in range(n+1)]
    for i in range(n):
        loc[mid[i]] = i
    while queue:
        # l r for inorder, s e for postorder index
        l, r, s, e = queue.popleft()
        root = post[e]
        root_loc = loc[root]
        res.append(root)
        l_size = root_loc-l
        if 0 <= root_loc < r:
            queue.appendleft([root_loc+1, r, s+l_size, e-1])
        if 0 <= l < root_loc:
            queue.appendleft([l, root_loc-1, s, s+l_size-1])
    return res


print(*preorder(n, inorder, postorder), sep=' ')
