#BOJ 2579 Climbing Stairs
import sys
input = sys.stdin.readline

n = int(input())
stairs = [0]
for _ in range(n):
    stairs.append(int(input().strip()))
m = [0 for _ in range(n+1)]
for i in range(1,min(3, n+1)):
    m[i] = m[i-1]+stairs[i]
for i in range(3, n+1):
    m[i] = max(stairs[i]+stairs[i-1]+m[i-3], stairs[i]+m[i-2])
print(m[-1])
