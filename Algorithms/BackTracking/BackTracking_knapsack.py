def knapsack(i, T):
	global mp
	if i >= n or T <= 0 :
		return
	
	pv = sum(P[j]*X[j] for j in range(i)) # j : 0 ~ i-1
	sv = sum(S[j]*X[j] for j in range(i))
	B1 = frac_knapsack(n-(i+1),S[i+1:], P[i+1:], T-S[i])
	B2 = frac_knapsack(n-(i+1),S[i+1:], P[i+1:], T)
	
	if S[i] <= T and pv + B1 + P[i] > mp:
		if pv + P[i] > mp:
			mp = pv + P[i]
		X[i] = 1
		knapsack(i+1, T-S[i])
	if pv + B2 > mp :
		X[i] = 0
		knapsack(i+1, T)
	return
def frac_knapsack(n, S, P, T):
	if T <= 0 : return 0
	s=0
	p=0
	for i in range(n):
		if s + S[i] <= T:
			p += P[i]
			s += S[i]
		else:
			p += (T-s) * (P[i]/S[i])
			s = T
			break
	return p
		
k = int(input())
n = int(input())
S = [int(x) for x in input().split()]
P = [int(x) for x in input().split()]
X = [0] * n
mp = 0

SP = list(zip(S,P)) # 튜플로 패킹하여 리스트로
SP.sort(key = lambda x: x[1]/x[0], reverse = True)
S, P = list(zip(*SP)) # tuple 로 언패킹, 리스트로 바꿔주든 말든~
knapsack(0, k)
print(mp)
