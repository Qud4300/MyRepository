# BOJ 2108 Statistics
import sys
from collections import Counter
import decimal
context = decimal.getcontext()
context.rounding = decimal.ROUND_HALF_UP
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
counter = Counter(arr)
arr.sort()
avg = int(round(decimal.Decimal(str(sum(arr)/n)), 0))
median = arr[n//2] if n%2 else (arr[n//2-1]+arr[n//2])/2
c = Counter(counter.values())
mode = counter.most_common()[0][0] if c[max(c.keys())]==1 else sorted([key for key,value in counter.most_common()  if value == max(counter.values())])[1]
rang = arr[-1]-arr[0]
print(avg,median,mode,rang,sep = '\n')