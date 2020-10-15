# BOJ 2292 Beehive

n = int(input())
k = 0
while 1:
    if 3*k**2+3*k+1<n:
        k+=1
    else:
        break
print(k+1)