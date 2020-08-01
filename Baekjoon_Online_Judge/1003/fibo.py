import sys
input = sys.stdin.readline
arr = [0]*41
for i in range(41):
    arr[i] = [0,0]
arr[0] = [1,0]
arr[1] = [0,1]
for i in range(2,41):
    arr[i][0] = arr[i-1][0] + arr[i-2][0]
    arr[i][1] = arr[i-1][1] + arr[i-2][1]
    
n = int(input())
for i in range(n):
    a = int(input())
    print(arr[a][0],arr[a][1])