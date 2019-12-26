# Trie Solution:
class TrieNode:
    def __init__(self):
        self.children = {}
        # self.end = False
    
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        root = TrieNode()
        bits = len(bin(max(nums))) - 2
        MASK = 1 << (bits-1)
        
        max_xor = 0
        
        for num in nums:
            mask = MASK
            val = 0
            cur = root
            cur_xor = root
            for _ in range(bits):
                bit = 1 if (mask & num) else 0 
                if bit not in cur.children:
                    cur.children[bit] = TrieNode()
                cur = cur.children[bit]
                
                toggle_bit = bit ^ 1
                if toggle_bit in cur_xor.children:
                    val += mask
                    cur_xor = cur_xor.children[toggle_bit]
                else:
                    cur_xor = cur_xor.children[bit]
                                        
                mask = mask >> 1
            max_xor = max(max_xor, val)
        
        return max_xor
        
# HashTable:
class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(31, -1, -1):
            prefix = set([num >> i for num in nums])
            ans = ans << 1
            candidate = ans + 1
            for p in prefix:
                if candidate ^ p in prefix:
                    ans = candidate
                    break
        return ans