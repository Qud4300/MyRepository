# BOJ 11758 CCW
import sys
input = sys.stdin.readline

a = [*map(int,input().split())]
b = [*map(int,input().split())]
c = [*map(int,input().split())]

# 외적을 이용한 삼각형의 면적 부호를 사용해 삼각형의 구성 방향을 판단한다.
ccw = (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
if ccw > 0:
    print(1)
elif ccw == 0:
    print(0)
else:
    print(-1)