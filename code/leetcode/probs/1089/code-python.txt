// O(N) two pass
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        count = 0
        index = 0
        while count + index < len(arr):
            if (arr[index] == 0):
                count += 1
            index += 1
        
        index = index - 1
        
        for i in range(index, -1, -1):
            if (i + count < len(arr)): arr[i + count] = arr[i]
            if (arr[i] == 0): 
                arr[i + count - 1] = 0
                count -= 1

// O(N^2)
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        index = 0
        while index < len(arr):
            if arr[index] != 0: 
                index += 1
            else:
                i = len(arr) - 1
                while (i > index):
                    arr[i] = arr[i-1]
                    i -= 1
                index += 2