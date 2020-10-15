# BOJ 10816 숫자카드 2
import sys

input = sys.stdin.readline
n = int(input())
cards = sorted([*map(int, input().split())])
m = int(input())
keys = [*map(int, input().split())]

dic = {}
for card in cards:
    try: dic[card] += 1
    except KeyError: dic[card] = 1

res = ""
for key in keys:
    try: res += str(dic[key]) + " "
    except KeyError: res += "0 "
print(res.strip())
