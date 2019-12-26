
def findSingleElement(A):
    lo, hi = 0, len(A) - 1
    while lo < hi:
        mid = lo + (hi - lo)//2
        if A[mid] == A[mid^1]:
            lo = mid + 1
        else:
            hi = mid
    return A[lo]
    
# PS: By the way it is same as 540. Single Element in a Sorted Array
