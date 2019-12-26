class Solution:
    def canPartitionKSubsets(self, A, k):
        
        if (k > len(A)): return False
        if (sum(A) % k != 0): return False
        target = sum(A) // k
        visited = [False]*len(A)
        A.sort(reverse=True)  # reverse the array, always picking the largest first

        # backtracking
        def dfs(A, sum_set, start, visited, target, num_subsets):
        
            if (num_subsets == 0):   # only exit condition
                return True
                
            if (sum_set == target) and dfs(A, 0, 0, visited, target, num_subsets - 1):
                return True
                
            for i in range(start, len(A)):
                if (visited[i] == False) and (sum_set + A[i] <= target):
                    visited[i] = True
                    if dfs(A, sum_set + A[i], i+1, visited, target, num_subsets):
                        return True
                    visited[i] = False
            return False
        
        return dfs(A, 0, 0, visited, target, k)