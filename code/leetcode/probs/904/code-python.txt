# O(N) time solutions
# This is more general, can be applied to N-fruits
class Solution:
    def totalFruit(self, trees: List[int]) -> int:
        
        ptr = 0
        d = {}
        max_fruits = 0
        
        for loc, fruit in enumerate(trees):
            d[fruit] = d.get(fruit, 0) + 1
            while len(d) >= 3:
                d[trees[ptr]] -= 1
                if d[trees[ptr]] == 0:
                    del d[trees[ptr]]
                ptr += 1
            max_fruits = max(max_fruits, loc - ptr + 1)

        return max(max_fruits, len(trees) - ptr)

# or alternatively
class Solution:
    def totalFruit(self, trees: List[int]) -> int:
        ptr = 0
        d = {}
        max_fruits = 0
        
        for loc, fruit in enumerate(trees):
            if fruit in d:
                d[fruit] = loc
            elif fruit not in d and len(d) < 2:
                d[fruit] = loc
            else:
                max_fruits = max(max_fruits, loc - ptr)
                for x in d:
                    if x != trees[loc-1]: earlier_fruit = x
                ptr = d[earlier_fruit] + 1
                del d[earlier_fruit]
                d[fruit] = loc
        
        return max(max_fruits, len(trees) - ptr)