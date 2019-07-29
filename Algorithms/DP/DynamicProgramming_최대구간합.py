n = int(input())
A = list(map(int, input().split()))
print(len(A))
print(A)
S = [0] * (n+1)
for i in range(1,len(A)+1):
	S[i] = max(A[i-1], S[i-1]+A[i-1])
print(max(S))
