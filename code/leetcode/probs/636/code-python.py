class Solution:
    def exclusiveTime(self, N: int, logs: List[str]) -> List[int]:
        ans = [0]*N
        prev_time = 0
        stack = []  # functional stack 
        
        for log in logs:
            func_id, func_type, timestamp = log.split(":")
            func_id = int(func_id)
            timestamp = int(timestamp)
            
            if func_type == "start":
                
                # update time spent if already running a process
                if stack:
                    ans[stack[-1]] += timestamp - prev_time
                    
                # starting new process
                stack.append(func_id)
                prev_time = timestamp
                
            else:
                
                # terminating current process
                ans[stack.pop()] += timestamp - prev_time + 1
                prev_time = timestamp + 1
        
        return ans