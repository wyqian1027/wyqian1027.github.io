class Solution:
    def maxRepOpt1(self, text: str) -> int:
        
        chunk_label = []
        chunk_count = []
        num_chunks = {}
        
        label, count = text[0], 1
        for ch in text[1:] + " ":
            if ch == label:
                count += 1
            else:
                chunk_label.append(label)
                chunk_count.append(count)
                num_chunks[label] = num_chunks.get(label, 0) + 1
                label = ch
                count = 1
        
        max_length = max(chunk_count)
        i = 0
        while i + 2 < len(chunk_label):
            ch = chunk_label[i]
            ans = 0
            if ch == chunk_label[i+2] and chunk_count[i+1] == 1:
                ans = chunk_count[i] + chunk_count[i+2] + (num_chunks[ch] > 2)
            elif ch == chunk_label[i+2] and chunk_count[i+1] > 1 and num_chunks[ch] > 1:
                ans = max(chunk_count[i+2], chunk_count[i]) + 1
            max_length = max(max_length, ans)
            i += 1
                
        return max_length