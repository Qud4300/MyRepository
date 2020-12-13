# BOJ 1991 Tree Traversal
import sys
input = sys.stdin.readline

tree = dict()

for _ in range(int(input())):
    p, l, r = input().split()
    tree[p] = [l,r]


def preorder(T,v):
    if v == '.':
        return ""
    l, r = T[v]
    return v + preorder(T, l) + preorder(T, r)


def inorder(T,v):
    if v=='.':
        return ""
    l, r = T[v]
    return inorder(T,l)+v+inorder(T,r)


def postorder(T,v):
    if v == '.':
        return ""
    l, r = T[v]
    return postorder(T, l) + postorder(T, r) + v


print(preorder(tree,'A'))
print(inorder(tree,'A'))
print(postorder(tree,'A'))