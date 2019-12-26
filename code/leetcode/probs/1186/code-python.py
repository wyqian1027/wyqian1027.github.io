class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        
        n = len(arr)
        max_arr_0 = [arr[0]]*n  # 0 delete, accum sum ending here
        max_arr_1 = [arr[0]]*n  # at most 1 delete ending here
        
        for i in range(1, n):
            num = arr[i]
            max_arr_0[i] = max(max_arr_0[i-1] + num, num)
            max_arr_1[i] = max(max_arr_1[i-1] + num, num)
            if i >= 2:
                max_arr_1[i] = max(max_arr_1[i], max_arr_0[i-2] + num)
            
        return max(max_arr_1)