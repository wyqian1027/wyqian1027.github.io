# 1. Using Dictionary, space cost is huge
# However, perform very well in reality

class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.store = {}
        self.curMap = {}

    def set(self, index: int, val: int) -> None:             # O(1)
        self.curMap[index] = val

    def snap(self) -> int:                                   # worst case O(N), size of array
        self.store[self.snap_id] = self.curMap.copy()
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:          # O(1)
        if index in self.store[snap_id]:
            return self.store[snap_id][index]
        else:
            return 0

# 2. Using List and Binary Search
class SnapshotArray:

    def __init__(self, length: int):
        self.records = [[[-1, 0]] for _ in range(length)]
        self.id = 0

    def set(self, index: int, val: int) -> None:                         # O(1)
        if self.records[index][-1][1] != val:
            self.records[index].append([self.id, val])

    def snap(self) -> int:                                               # O(1)
        self.id += 1
        return self.id - 1

    def get(self, index: int, snap_id: int) -> int:                      # O(logS)
        loc = bisect.bisect(self.records[index], [snap_id + 1]) - 1
        return self.records[index][loc][1]