import heapq as hq

def cost(T):
    H = []
    for i in range(len(T)):
        hq.heappush(H, (T[i],str(T[i])))
    while len(H) > 1 :
        a = hq.heappop(H)
        b = hq.heappop(H)
        hq.heappush(H, (a[0]+b[0], '( '+a[1]+' , '+b[1]+' ) '))
    root = hq.heappop(H)
    count = 0
    res = 0
    for a in root[1].split() :
        if a == '(': count+=1
        elif a == ')' : count-=1
        elif a == ',' : continue
        else : res += count*int(a)
    return res
        
A = list(map(int, input().split()))
print(cost(A))
