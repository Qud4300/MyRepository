# BOJ 10250 ACM Hotel
import sys
input = sys.stdin.readline

k = int(input())
res = ""
for _ in range(k):
    h,w,n = map(int, input().split())
    res += str((n%h if n%h!=0 else h)*100+(n-1)//h+1)+'\n'
print(res)
