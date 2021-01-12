# BOJ 1806 Subtotal

n, s = map(int, input().split())
arr = [*map(int, input().split())]

count = n+1
l, r = 0, 1
total = arr[l] + arr[r]
while l < n:
    if (total < s and r < n-1) or l > r:
        r += 1
        total += arr[r]
    else:
        if total >= s:
            count = min(count, r-l+1)
            if count == 1:
                break
        total -= arr[l]
        l += 1

print(count if count != n+1 else 0)
