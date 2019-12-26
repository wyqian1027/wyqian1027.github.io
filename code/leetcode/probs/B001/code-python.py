# O(N^2)

def findMaxNumChunks(A, l=0):
    n = len(A)
    m = len(A) - l*2   # slice length
    if m == 0:
        return 0
    for i in range(0, m//2):
        if A[l:l+i+1] == A[n-l-i-1:n-l]:
            return findMaxNumChunks(A, l+i+1) + 2
    return 1