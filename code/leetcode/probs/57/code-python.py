class Solution:
    
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
            
        res = []
        j = 0
        
        while j < len(intervals):          
            if intervals[j][0] > newInterval[1]:
                break
            if intervals[j][0] <= newInterval[0] <= intervals[j][1] or \
            newInterval[0] <= intervals[j][0] <= newInterval[1]:
                l = min(newInterval[0], intervals[j][0])
                r = max(newInterval[1], intervals[j][1])
                newInterval = [l, r]
            else:
                res.append(intervals[j])
            j += 1
        
        res.append(newInterval)
        res.extend(intervals[j:])
        return res