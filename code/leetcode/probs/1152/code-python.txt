class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        user = collections.defaultdict(list)
        for t, u, w in sorted(zip(timestamp, username, website)):
            user[u].append(w)
        
        counter = collections.Counter()
        for websites in user.values():
            counter += collections.Counter(set(itertools.combinations(websites, 3)))
        
        return min(counter, key=lambda x: (-counter[x], x))