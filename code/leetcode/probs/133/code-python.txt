# Definition for a Node.

class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

# BFS
class Solution(object):
    def cloneGraph(self, node):

        org = collections.deque([node])
        d = {}
        d[node] = Node(node.val, [])
        
        while org:
            cur = org.popleft()
            
            for nei in cur.neighbors:
                if nei not in d: 
                    d[nei] = Node(nei.val, [])
                    neiCopy = d[nei]
                    d[cur].neighbors.append(neiCopy)
                    org.append(nei)
                else:
                    d[cur].neighbors.append(d[nei])
                                
        return d[node]

# DFS
class Solution:

    def cloneGraph(self, node):

        d = {node: Node(node.val, [])}
        self.dfs(node, d)
        return d[node]
    
    def dfs(self, node, d):
        
        for nei in node.neighbors:
            if nei not in d:
                d[nei] = Node(nei.val, [])
                d[node].neighbors.append(d[nei])
                self.dfs(nei, d)
            else:
                d[node].neighbors.append(d[nei])