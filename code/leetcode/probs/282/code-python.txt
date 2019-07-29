class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        
        def dfs(idx, path, op, cur, val):
            '''
            location of operators is added after the idx
            '''
            if idx >= len(num):   
                s = val + cur if op == "+" else val - cur 
                if s == target:
                    res.append(path)
                return
            
            for i in range(idx, len(num)):
                k = int(num[idx:i+1])
                if op == "-":
                    dfs(i+1, path+"+"+num[idx:i+1], "+", k, val-cur) 
                    dfs(i+1, path+"-"+num[idx:i+1], "-", k, val-cur) 
                    dfs(i+1, path+"*"+num[idx:i+1], "-", cur*k, val)
                elif op == "+":
                    dfs(i+1, path+"+"+num[idx:i+1], "+", k, val+cur) 
                    dfs(i+1, path+"-"+num[idx:i+1], "-", k, val+cur) 
                    dfs(i+1, path+"*"+num[idx:i+1], "+", cur*k, val)
                else:
                    dfs(i+1, num[idx:i+1], "+", k, 0)                   
                if k == 0: break
                    
        res = []
        dfs(0, "", None, 0, 0)
        return res