class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        
        n_bytes = 0
        mask1 = 1 << 7
        mask2 = 1 << 6
        for num in data:
            mask = mask1
            if n_bytes == 0:
                while mask & num > 0:
                    n_bytes += 1
                    mask = mask >> 1

                if n_bytes == 0:
                    continue
                if n_bytes == 1 or n_bytes > 4:
                    return False
            else:
                
                if not ((mask1 & num) > 0 and (mask2 & num) == 0):
                    return False
            n_bytes -= 1
            
        return n_bytes == 0