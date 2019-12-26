class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        
        d = {}  # map prison state to day #

# Better use List Comprehension        
#        def change_state(cells):
#            new_cells = [0]*len(cells)
#            for i in range(1, len(cells)-1):
#                if cells[i-1] == cells[i+1]:
#                    new_cells[i] = 1
#            return new_cells

        while N > 0:
            key = tuple(cells)
            if key in d:
                N = N % (d[key] - N)
                if N == 0: return cells
            else:
                d[tuple(cells)] = N
            cells = [0] + [1 if cells[i-1] == cells[i+1] else 0 for i in range(1, len(cells)-1)] + [0]
            N -= 1
        
        return cells