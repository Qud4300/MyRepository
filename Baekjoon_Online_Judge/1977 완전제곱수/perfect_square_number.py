# BOJ 1977 Perfect Square number

m = int(input())
n = int(input())

mm = int(m**0.5) if int(m**0.5)**2 == m else int(m**0.5) + 1
nn = int(n**0.5) + 1
arr = [i**2 for i in range(mm, nn)]
if len(arr):
    print(sum(arr))
    print(arr[0])
else:
    print(-1)
