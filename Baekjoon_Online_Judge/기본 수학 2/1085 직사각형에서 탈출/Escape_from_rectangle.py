# BOJ 1085 Escape from Rectangle
x,y,w,h = map(int, input().split())
print(min(x,y,w-x,h-y))