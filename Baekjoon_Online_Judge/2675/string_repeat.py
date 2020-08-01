c = int(input())
for i in range(c):
    R, S = input().split()
    for x in S:
        print(x*int(R), end='')
    print()
