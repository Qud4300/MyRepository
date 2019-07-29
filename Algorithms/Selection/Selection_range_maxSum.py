def max_sum_1(A):
    m = len(A)
    max_sum = None
    for i in range(m):
        res = 0
        for j in range(i,m):
            res += A[j]
        if max_sum < res or max_sum == None:
            max_sum = res
    return max_sum
def prefixSum(A,k): #sum thru k'th index
    if k > len(A)-1: return None
    return sum(A[:k+1])

def max_sum_prefixSum(A):
    m = len(A)
    max_sum = None
    for i in range(m):
        for j in range(i, m):
            res = prefixSum(A,j) - prefixSum(A,i)
        if max_sum < res or max_sum == None:
            max_sum = res
    return max_sum
