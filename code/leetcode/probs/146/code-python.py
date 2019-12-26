# O(1) implementation with Doubly Linked Node with two fields
class Node:
    
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.left = None
        self.right = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.cap = capacity
        self.cache = {}   # map from key to node
        
        # only change in between head and tail to avoid corner cases
        self.head.right = self.tail
        self.tail.left = self.head
    
    def add(self, node):
        
        # always add after head like a Priority Queue
        tmp = self.head.right
        node.left = self.head
        node.right = tmp
        self.head.right = node
        tmp.left = node 
        
    def remove(self, node):
        before = node.left
        after = node.right
        before.right = after
        after.left = before
    
    def moveToHead(self, node):
        self.remove(node)
        self.add(node)

    def popLast(self):
        last = self.tail.left
        last.right.left = last.left
        last.left.right = last.right
        return last
        
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.moveToHead(node)
            return node.val
        return -1
                        
    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            self.moveToHead(node)
            node.val = value
        else:
            newNode = Node(key, value)
            self.cache[key] = newNode
            self.add(newNode)
            self.size += 1
            if self.size > self.cap:
                last = self.popLast()
                del self.cache[last.key]
                self.size -= 1


# Using OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = collections.OrderedDict()
        self.size = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        val = self.cache.pop(key)
        self.cache[key] = val
        return val
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        else:
            if self.size > 0:
                self.size -= 1
            else:
                self.cache.popitem(last=False)
        self.cache[key] = value