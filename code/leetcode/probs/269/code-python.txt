class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        graph = collections.defaultdict(set)
        indegree = {}
        
        for word in words:
            for ch in word:
                indegree[ch] = 0
        
        for w1, w2 in zip(words, words[1:]):
            maxL = min(len(w1), len(w2))
            for i in range(maxL):
                if w1[i] == w2[i]: 
                    continue
                else:
                    if w1[i] in graph[w2[i]]: return ""
                    if w2[i] not in graph[w1[i]]: 
                        graph[w1[i]].add(w2[i])
                        indegree[w2[i]] += 1
                    break
        
        start = collections.deque([x for x in indegree if indegree[x] == 0])
        order = []
        
        while start:
            ch = start.popleft()
            order.append(ch)
            for nei in graph[ch]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    start.append(nei)
        return "".join(order) if len(order) == len(indegree) else ""