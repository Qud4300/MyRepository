# BOJ 11723 Set
import sys
input = sys.stdin.readline

S = 0b0

def add(x):
    global S
    S |= 1<<(x-1)

def remove(x):
    global S
    S&=~(1<<(x-1))

def check(x):
    global S
    return (S>>(x-1))&1

def toogle(x):
    global S
    S ^= 1<<(x-1)

def all():
    global S
    S = 1048575

def empty():
    global S
    S = 0

m = int(input())
res = ""
for _ in range(m):
    a = input().split()
    com = a[0]
    if com=="add":
        add(int(a[1]))
    elif com=="remove":
        remove(int(a[1]))
    elif com=="check":
        print(check(int(a[1])))
    elif com=="toggle":
        toogle(int(a[1]))
    elif com=="all":
        all()
    elif com=="empty":
        empty()
    else:
        continue
