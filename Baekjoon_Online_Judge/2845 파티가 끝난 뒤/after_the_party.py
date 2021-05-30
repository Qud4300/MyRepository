# BOJ 2845 After the Party

L, P = map(int, input().split())
est = L*P
res = ""
for i in [*map(int, input().split())]:
    res += str(i - est) + ' '
print(res.rstrip())
