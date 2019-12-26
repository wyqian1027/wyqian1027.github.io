# Sliding window solution
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        
        count = data.count(1)
        if count <= 1: return 0
        
        n = len(data)
        cur = 0
        for i in range(count):
            cur = cur + 1 if data[i] == 1 else cur
        min_swaps = count - cur
        
        for i in range(count, n):
            if data[i] == 1: cur += 1
            if data[i - count] == 1: cur -= 1
            min_swaps = min(min_swaps, count - cur)
        
        return min_swaps