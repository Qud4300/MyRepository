# BOJ 1193 N'th fractional number.
x = int(input())
n = 1
while n*(n+1)//2 < x:
    n += 1
diff = n*(n+1)//2-x
if n%2:
    a,b = 1+diff,n-diff
else:
    a, b = n - diff, 1 + diff
print(a,'/',b,sep='')