# BOJ 17298 Next Greater Element(오큰수)
n = int(input())
arr = [*map(int, input().split())]
res = [-1 for _ in range(n)]
stack = [0]
i = 1
while stack and i<n:
    while stack and arr[stack[-1]] < arr[i]:
        res[stack[-1]] = arr[i]
        stack.pop()
    stack.append(i)
    i += 1

print(*res)
