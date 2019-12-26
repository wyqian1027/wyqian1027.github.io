class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        if a == 0: return b
        if b == 0: return a
        
        mask = 0xFFFFFFFF
        MAX = 0x7FFFFFFF
        # print("mask = ", mask)
        # print("MAX = ", MAX)
        print(a, b)
        
        while b != 0:
            
            carry = a & b
            a = a^b
            b = carry << 1
            # print("unmasked: ", a, "\t", b)
            a = a & mask
            b = b & mask
            # print("masked:   ", a, "\t", b)
            # print()
            
        return a if a <= MAX else ~(a ^ mask)

# Below are the output for -10 and 5
# mask =  4294967295
# MAX =  2147483647

# -10 5

# unmasked:  -13 	 8
# masked:    4294967283 	 8

# unmasked:  4294967291 	 0
# masked:    4294967291 	 0