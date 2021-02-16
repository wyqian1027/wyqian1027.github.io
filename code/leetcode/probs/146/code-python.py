# O(1) implementation with Doubly Linked Node with two fields
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        
class DLL:
    def __init__(self):
        self.head = Node(1, 1)
        self.tail = Node(1, 1)
        self.joinNodes(self.head, self.tail)
        self.size = 0
       
    def append(self, node):
        self.joinNodes(self.tail.left, node)
        self.joinNodes(node, self.tail)
        self.size += 1
    
    def popLeft(self):
        return self.popNode(self.head.right)
    
    def popNode(self, node):
        self.joinNodes(node.left, node.right)
        self.size -= 1
        return node

    def joinNodes(self, leftNode, rightNode):
        leftNode.right = rightNode
        rightNode.left = leftNode


class LRUCache:
    '''
    Most frequent nodes are indexed to the right in the DDL
    '''
    def __init__(self, capacity: int):
        self.keyToNode = {}
        self.dll = DLL()
        self.cap = capacity
        
    def get(self, key: int) -> int:
        if key in self.keyToNode:
            node = self.keyToNode[key]
            self.dll.popNode(node)
            self.dll.append(node)
            return node.val
        else:
            return -1
        
 
    def put(self, key: int, value: int) -> None:
        # 3 cases to consider
        if key in self.keyToNode:
            node = self.keyToNode[key]
            node.val = value
            self.dll.popNode(node)
            self.dll.append(node)
            return 
        if self.dll.size == self.cap:
            node = self.dll.popLeft()
            del self.keyToNode[node.key]
        node = Node(key, value)
        self.keyToNode[key] = node
        self.dll.append(node)  


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