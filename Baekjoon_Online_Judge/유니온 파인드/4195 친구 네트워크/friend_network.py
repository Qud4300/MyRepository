# BOJ 4195 Friend Network
import sys
input = sys.stdin.readline


def findParent(v):
    while v != parent[v]:
        v = parent[v]
    return v


for T in range(int(input())):
    F = int(input())
    network = []
    parent = []
    count = 0
    ID = dict()
    res = ''
    for _ in range(F):
        A, B = input().split()
        for name in A, B:
            if name not in ID:
                ID[name] = count
                network.append(1)
                parent.append(count)
                count += 1
        M, m = max(ID[A], ID[B]), min(ID[A], ID[B])
        M_par, m_par = findParent(M), findParent(m)
        if M_par != m_par:
            parent[M_par] = m_par
            network[m_par] += network[M_par]
        res += str(network[m_par])+'\n'
    print(res.rstrip())
