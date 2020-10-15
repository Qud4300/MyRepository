# BOJ 10989 Sort 3 -Counting Sort
import sys
input = sys.stdin.readline

n = int(input())
dic = dict()
for _ in range(n):
    x = int(input())
    if x in dic:
        dic[x] += 1
    else :
        dic[x] = 1
for key,count in sorted(dic.items()):
    for _ in range(count):
        print(key)