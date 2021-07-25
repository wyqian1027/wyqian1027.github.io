class Solution:
    def findIntegers(self, n: int) -> int:
        
        '''
        less than 1-digit num '1':   '0'                => count = 1
        less than 2-digit num '10':  '0', '1'           => count = 2
        less than 3-digit num '100': '00', '01', '10'   => count = 3
        
        n-digit num = (n-1)-digit num + (n-2)-digit num (since cannot have '11' at MSB)
        
        This is Fibonaci number seq: f(n) = f(n-1) + f(n-2)
        
        '''
        
        k = len(bin(n))-2
        
        fib = [1, 2]
        for i in range(2, k+1):
            fib.append(fib[-1] + fib[-2])
        
        s = 0; bit = 0
        for i in range(k, -1, -1):
            if (1<<i) & n > 0:
                # in fact, each add is addition allowed numbers less than this bit.
                s += fib[i]
                if bit == 1: return s
                bit = 1
            else:
                bit = 0
    
        return s + 1