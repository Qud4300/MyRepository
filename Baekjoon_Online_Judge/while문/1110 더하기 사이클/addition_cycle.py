a = int(input())
cycle = 0
b = a
while b != a or cycle==0:
    b = (b//10 + b%10)%10 + 10*(b%10)
    cycle+=1
print(cycle)
