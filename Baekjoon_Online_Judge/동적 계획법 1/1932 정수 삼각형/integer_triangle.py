import sys
input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    nums.append(list(map(int, input().split())))
for i in range(n-1,0,-1):
    for j in range(i):
        nums[i-1][j] += max(nums[i][j], nums[i][j+1])
print(nums[0][0])
