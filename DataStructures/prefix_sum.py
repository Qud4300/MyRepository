import time, random

def prefixSum1(X, n):
	A = [0]*n
	for i in range(n):
		for j in range(0, i+1):
			A[i] += X[j]
	return A

n = int(input())# n 입력받음
X = []
for i in range(n):
	X.append(random.randint(0,5)) # 리스트 X를 randint를 호출하여 n개의 랜덤한 숫자로 채움
A = prefixSum1(X,n)
print(X)
print(A)
