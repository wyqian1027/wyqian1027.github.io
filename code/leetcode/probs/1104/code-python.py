class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        
        path = [label]
        
        while label > 1:
            label = (label - 1) // 2 if  label % 2 == 1 else label // 2
            path.append(label)
        
        path = path[::-1]   # Correct Path if No Zigzag
        
        start = 2 if len(path) % 2 == 0 else 1 
            
        for i in range(start, len(path), 2):
            path[i] = 2**i + (2**(i+1)-1 - path[i])
        
        return path