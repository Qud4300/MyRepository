import math
def find_divisor(n):
    div = set()
    #root = math.floor(math.sqrt(n))
    root = int(math.sqrt(n))
    for i in range(1, root+1):
        if n%i == 0 :
            div.add(i)
            div.add(n//i) # div는 set이라서, n의 제곱근은 하나만 들어간다!
    return div

a = int(input())
divisors = find_divisor(a)
divisors.discard(a)
if sum(divisors)==a : print("YES")
else: print("NO")
