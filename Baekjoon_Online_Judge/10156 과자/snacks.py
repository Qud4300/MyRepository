# BOJ 10156 과자
k, n, m = map(int, input().split())

print(max(k*n-m, 0))
