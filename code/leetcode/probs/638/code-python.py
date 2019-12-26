class Solution:
    
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
    
        d = {}
        
        def calculate(needs):

            if tuple(needs) in d:
                return d[tuple(needs)]
                        
            ans = sum(needs[i]*price[i] for i in range(len(needs)))
            
            for deal in special:
                tmp = [needs[i] - deal[i] for i in range(len(needs))] 
                if min(tmp) >= 0:
                    ans = min(ans, calculate(needs) + deal[-1])

            d[tuple(needs)] = ans
            return ans
        
        return calculate(needs)
                
                
            
    
        
        