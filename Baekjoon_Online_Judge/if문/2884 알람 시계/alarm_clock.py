h,m = map(int, input().split())
if m<45:
    h,m=h-1,m+15
    if h<0 : h+=24
else: m-=45
print(h,m)