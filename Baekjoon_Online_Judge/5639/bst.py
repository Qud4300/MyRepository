# BOJ 5639 BST
import sys
sys.setrecursionlimit(10**9)


def postorder(start: int, end: int):
    global res, tree

    root = tree[start]
    r = start+1
    for i in range(start+1, end):
        if tree[r] < root:
            r += 1
        else: break
    if start+1 < r:
        postorder(start+1, r)
    if r < end:
        postorder(r, end)
    res += str(root)+'\n'
    return


res = ""
tree = []
for _ in range(10000):
    try:
        a = int(sys.stdin.readline().rstrip())
        if a is not None:
            tree.append(int(a))
    except ValueError:
        break
postorder(0, len(tree))
print(res.rstrip())
