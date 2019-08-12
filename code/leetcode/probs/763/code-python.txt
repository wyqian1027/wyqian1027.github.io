class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        
        last_pos = {}
        for i, ch in enumerate(S):
            last_pos[ch] = i
        
        chunks = []
        left = right = 0
        for i, ch in enumerate(S):
            right = max(right, last_pos[ch])
            if i == right:
                chunks.append(right - left + 1)
                left = i + 1
        return chunks