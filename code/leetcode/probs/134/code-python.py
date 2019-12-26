class Solution:
    
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    
        start = 0
        cur_tank = 0
        total_tank = 0
        
        for i in range(len(gas)):
            change = gas[i] - cost[i]
            cur_tank += change
            total_tank += change
            
            if cur_tank < 0:
                start = i + 1
                cur_tank = 0
        
        return start if total_tank >= 0 else -1