# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def is_common_subsequence(X, Y, S):
	return is_subsequence(X, S) and is_subsequence(Y, S)

def is_subsequence(X, S):
	n = len(X)
	m = len(S)
	i = 0
	j = 0
	assert(m <= n)
	while j < m and i < n:
		if S[j] == X[i]:
			j = j + 1
		i = i + 1
	return j == m

def find_LCS(X, Y):
	L = []
	S = ""
	for i in range(len(X)+1):# 길이 : L 2차원 리스트 초기화
		L.append([])
		for j in range(len(Y)+1):
			L[i].append(0)
			
	for i in range(len(X)): #L의 각 값 대입
		for j in range(len(Y)):
			if X[i] == Y[j]:
				L[i+1][j+1]=L[i][j]+1
			elif L[i][j+1] >= L[i+1][j]:
				L[i+1][j+1] = L[i][j+1]
			else : L[i+1][j+1] = L[i+1][j]
	
	i=len(X)
	j=len(Y)
	while i>0 and j>0:
		if X[i-1] == Y[j-1]:
			S = X[i-1] + S
			i-=1
			j-=1
		elif L[i][j-1] >= L[i-1][j]:
			j-=1
		else :
			i-=1
	return L[-1][-1], S

# don't touch the code below!
X = input().strip()
Y = input().strip()
k, S = find_LCS(X, Y) # take the length k and LCS S
print(k)
print(is_common_subsequence(X, Y, S))
