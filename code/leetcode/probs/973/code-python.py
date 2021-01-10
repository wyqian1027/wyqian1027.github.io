from heapq import nsmallest, heappush, heappop

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        # heapq solutions using default method 
        # O(NlogK)
        # return nsmallest(K, points, lambda x: x[0]*x[0] + x[1]*x[1])
        # alternatively:
        # h = []
        # for p in points:
        #     heappush(h, [-(p[0]*p[0] + p[1]*p[1]), p])
        #     if len(h) > K:
        #         heappop(h)
        # return [e[1] for e in h]
        self.sort(points, 0, len(points)-1, K)
        return points[:K]
        
    def sort(self, A, l, r, k):
        if l < r:
            p = self.partition(A, l, r)
            if p == k:
                return
            elif p < k:
                self.sort(A, p+1, r, k)
            else:
                self.sort(A, l, p-1, k)
    
    def partition(self, A, l, r):
        pivot = A[r]
        i = l
        for j in range(l, r):
            if self.compare(A[j], pivot) < 0:
                A[i], A[j] = A[j], A[i]
                i += 1
        A[i], A[r] = A[r], A[i]
        return i
    
    def compare(self, p1, p2):
        return p1[0]*p1[0] + p1[1]*p1[1] - p2[0]*p2[0] - p2[1]*p2[1]