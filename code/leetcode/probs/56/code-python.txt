class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if not intervals or len(intervals) == 0: return []
        intervals.sort()
        res = []
        
        res.append(intervals[0])
        
        for i in range(1, len(intervals)):
            left, right = intervals[i]
            if left <= res[-1][1] and right > res[-1][1]:
                res[-1][1] = right
            elif left > res[-1][1]:
                res.append([left, right])
        
        return res