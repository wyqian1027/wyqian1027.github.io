class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        
        d = collections.defaultdict(list) # map labels to values
        for i in range(len(values)):
            d[labels[i]].append(values[i])
        
        res = []
        for k, v in d.items():
            res += sorted(v, reverse=True)[:use_limit]
        
        res.sort(reverse=True)
        
        return sum(res[:min(len(res), num_wanted)])