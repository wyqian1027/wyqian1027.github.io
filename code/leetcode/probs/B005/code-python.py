# Selection Sort O(N^2)
def minSwaps(A):
    count = 0
    for i in range(len(A)-1):
        idx = i
        for j in range(i+1, len(A)):
            if A[j] < A[idx]:
                idx = j
        if A[idx] != A[i]:
            A[idx], A[i] = A[i], A[idx]
            count += 1
    return count

# With Hash and HeapQ O(NLgN)
from heapq import *
import collections

def minSwaps(A):
    h = list(A)
    heapify(h)
    d = collections.defaultdict(list)
    for i, el in enumerate(A):
        d[el].append(i)
        
    count = 0
    for i in range(len(A)-1):
        d[A[i]].pop()
        minE = heappop(h)        
        if A[i] != minE:
            idx = d[minE].pop()
            A[idx], A[i] = A[i], A[idx]
            d[A[idx]].append(idx)
            count += 1
        print(A)
    return count