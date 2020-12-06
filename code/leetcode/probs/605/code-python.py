class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        tot = 0
        
        for i, c in enumerate(flowerbed):
            if c == 0 and \
                (i == 0 or flowerbed[i-1] != 1) and \
                (i == (len(flowerbed)-1) or flowerbed[i+1] != 1):
                flowerbed[i] = 1
                tot += 1
            if tot == n: return True
        
        return tot >= n
 