import random, time

def quick_sort(A, first, last):
	comp , swap = 0, 0
	if first >= last : return 0,0
	comp += 1
	left , right = first+1, last
	p = A[first]
	while left <= right :
		comp += 1
		while left <= last and A[left] < p :
			left += 1
			comp += 1
		comp += 1
		while right > first and A[right] >= p:
			right -= 1
			comp += 1
		comp += 1
		if left <= right :
			A[left], A[right] = A[right], A[left]
			left += 1
			right -= 1
			swap += 3
	A[first], A[right] = A[right], A[first]
	swap += 3
	c1, s1 = quick_sort(A,first,right-1)
	c2, s2 = quick_sort(A,right+1, last)
	return comp+c1+c2, swap+s1+s2

def merge_sort(A, first, last):
	comp, swap = 0, 0
	if first >= last: return 0,0
	m = (first + last)//2
	c1, s1 = merge_sort(A, first, m)
	c2, s2 = merge_sort(A, m+1, last)
	B = []
	i = first #i 는 앞 분할의 시작지점
	j = m +1 #j는 뒤 분할의 시작지점
	while i <= m and j<= last:
		if A[i] <= A[j]:
			B.append(A[i])
			i+=1
		else:
			B.append(A[j])
			j+=1
		comp += 2
	#append 작업은 둘 중 하나만 실행된다.
	for k in range(i, m+1): B.append(A[k])
	for k in range(j, last+1) : B.append(A[k])
	#B의 정렬된 원소들을 A로 옮긴다.
	for k in range(first,last+1): 
		A[k] = B[k-first]
		swap += 1
	return comp+c1+c2, swap+s1+s2

def check_sorted(A):
	sorted = True
	for i in range(n-1):
		if A[i] > A[i+1]: return False
	return True
while True:
        n = int(input())
        if n == -1 : break
        random.seed()
        A, B = [], []

        # A, B에 n개의 같은 랜덤 값을 만들어 저장한다
        for i in range(n):
                r = random.randint(-1000,1000)
                A.append(r)
                B.append(r)
        t0 = time.clock()
        cmp_quick, move_quick = quick_sort(A, 0, n-1)
        t1 = time.clock()
        cmp_merge, move_merge = merge_sort(B, 0, n-1)
        t2 = time.clock()

        # 진짜 정렬되었는지 check한다 - check_sorted를 호출
        assert(check_sorted(A))
        assert(check_sorted(B))
        print("Quick sort: n =", n)
        print("time = {} seconds".format(t1-t0))
        print("comparisons = {}, moves = {}".format(cmp_quick, move_quick))
        print("Merge sort: n =", n)
        print("time = {} seconds".format(t2-t1))
        print("comparisons = {}, moves = {}".format(cmp_merge, move_merge))
