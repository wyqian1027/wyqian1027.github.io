# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.f = 1
        self.pre = None
        self.nxt = None
    
class DoublyLinkedList:
    def __init__(self, freq):
        '''
        Head <-> node1 <-> node2 <-> Tail
        contains nodes of the same frequency
        '''
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.size = 0
        self.freq = freq
        self.join(self.head, self.tail)
    
    def popleft(self):
        if self.size != 0:
            node = self.head.nxt
            self.head.nxt = node.nxt
            self.head.nxt.pre = self.head
            self.size -= 1
            return node
        return None
    
    def push(self, node):
        leftNode = self.tail.pre
        self.join(leftNode, node)
        self.join(node, self.tail)
        self.size += 1
        return node
    
    def join(self, node1, node2):
        node1.nxt = node2
        node2.pre = node1
    
    def remove(self, node):
        node.pre.nxt = node.nxt
        node.nxt.pre = node.pre
        node.pre = None
        node.nxt = None
        self.size -= 1

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.freqToDLL = {}
        self.keyToNode = {}
        self.minFreq = 1
      
    def addNode(self, node):
        if node.f not in self.freqToDLL:
            ddl = DoublyLinkedList(node.f)
            self.freqToDLL[node.f] = ddl
        ddl = self.freqToDLL[node.f]
        ddl.push(node)
        self.keyToNode[node.key] = node
        
    def getNodeFromKey(self, key): 
        if key in self.keyToNode:
            node = self.keyToNode[key]
            ddl = self.freqToDLL[node.f]
            ddl.remove(node)
            node.f += 1
            if ddl.size == 0 and self.minFreq == node.f - 1:
                self.minFreq = node.f
            self.addNode(node)
            return node
        else:
            return None
    
    def get(self, key: int) -> int:
        node = self.getNodeFromKey(key)
        return node.val if node else -1

    def put(self, key: int, value: int) -> None: 
        if self.cap == 0: return
        if key in self.keyToNode:   # exist, update its val
            node = self.getNodeFromKey(key)
            node.val = value
        elif self.size < self.cap:  # not exist, ok to add
            node = Node(key, value)
            self.addNode(node)
            self.size += 1
            self.minFreq = 1
        else:                       # not exist, need delete then add
            node = Node(key, value)
            minDDL = self.freqToDLL[self.minFreq]
            popNode = minDDL.popleft()
            del self.keyToNode[popNode.key]
            self.addNode(node)
            self.minFreq = 1
