class Solution:
    def accountsMerge(self, accounts):

        n = len(accounts)
        
        parent = list(range(n))
        
        # simple union-find data structure
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            parent[px] = py
        
        # first set up the "graph"
        email_to_id = defaultdict(list)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                email_to_id[email].append(i)
                
        # union-find 
        for ids in email_to_id.values():
            for id in ids[1:]:
                union(ids[0], id)
        
        merged_accounts = defaultdict(set)
        for i, account in enumerate(accounts):
            merged_accounts[find(i)].update(account[1:])
        
        return [[accounts[i][0]] + sorted(emails) for i, emails in merged_accounts.items()]