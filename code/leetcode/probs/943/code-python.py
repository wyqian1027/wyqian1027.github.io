# The equivalent of finding a shortest path across all nodes at least once, the Traveling Salesman Problem (TSP)
class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        
        # the Cost func: more overlap less the cost
        def calc(a, b):
            for i in range(1, len(a)):
                if b.startswith(a[i:]):
                    return len(b) - len(a) + i
            return len(b)
        
        n = len(words)
        graph = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                graph[i][j] = calc(words[i], words[j])
                graph[j][i] = calc(words[j], words[i])
        
        dp = [[0]*n for _ in range(1 << n)]
        path = [[0]*n for _ in range(1 << n)]
        last = -1
        best_min = float('inf')
        max_mask = (1 << n) - 1
        
        # TSP DP O(2^n * n^2)
        for i in range(1, 1<<n):
            for j in range(n):
                dp[i][j] = float('inf')
            for j in range(n):
                # go back to a prev bitmask
                if (i & (1 << j)) > 0:
                    prev = i - (1 << j)
                    if prev == 0:
                        dp[i][j] = len(words[j])
                    else:
                        for k in range(0, n):
                            if dp[prev][k] < float('inf') and dp[prev][k] + graph[k][j] < dp[i][j]:
                                dp[i][j] = dp[prev][k] + graph[k][j]
                                path[i][j] = k
                                
                if i == max_mask and dp[i][j] < best_min:
                    best_min = dp[i][j]
                    last = j
        
        cur = max_mask
        stack = []
        while cur > 0:
            stack.append(last)
            tmp = cur
            cur -= (1 << last) # subtract last to get prev path
            last = path[tmp][last]        
        
        output = []
        i = stack.pop()
        output.append(words[i])
        while stack:
            j = stack.pop()
            start_pos = len(words[j]) - graph[i][j]
            output.append(words[j][start_pos:])
            i = j
        
        return "".join(output)