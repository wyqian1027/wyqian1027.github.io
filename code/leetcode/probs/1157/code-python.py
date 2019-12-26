# O(NlogN) Query: Binary Search with Pruning

from bisect import bisect_left as bl
from bisect import bisect_right as br
from collections import defaultdict

class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.d = defaultdict(list)
        for i, val in enumerate(arr):
            self.d[val].append(i)
        self.elements = sorted(self.d.keys(), key=lambda x: len(self.d[x]), reverse=True)

    def query(self, left: int, right: int, threshold: int) -> int:
        
        for x in self.elements:
            if br(self.d[x], right) - bl(self.d[x], left) >= threshold:
                return x
            elif len(self.d[x]) < threshold:
                break
        return -1
        
# O(10N) Binary Search with Random number.
from bisect import bisect_left as bl
from collections import defaultdict
import random

class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.d = defaultdict(list)
        for i, val in enumerate(arr):
            self.d[val].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        
        for _ in range(10):
            x = self.arr[random.randint(left, right)]
            start = bl(self.d[x], left)
            if start + threshold - 1 < len(self.d[x]) and self.d[x][start+threshold-1] <= right:
                return x
        return -1