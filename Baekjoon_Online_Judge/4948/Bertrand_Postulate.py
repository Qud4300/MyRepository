# BOJ 4948 Bertrand Postulate
import sys
input = sys.stdin.readline
arr = [True for i in range(2*123456+1)]
arr[0],arr[1] = False,False
for i in range(2,int((2*123456)**0.5)+1):
    if arr[i] == True:
        for j in range(i*2, 2*123456+1, i):
            arr[j] = False
res = ""
while True:
    n = int(input())
    if n == 0: break
    res += str(sum(arr[n+1:2*n+1])) + '\n'
print(res)