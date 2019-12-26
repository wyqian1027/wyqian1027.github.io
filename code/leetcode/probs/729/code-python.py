# class MyCalendar:

#     def __init__(self):
#         self.bookings = []

#     def book(self, start: int, end: int) -> bool:
#         for s, e in self.bookings:
#             if start < e and end > s:
#                 return False
#         self.bookings.append([start, end])
#         return True

class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        
class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = Node(start, end)
            return True
        def visit(start, end, node):
            if start < node.end and end > node.start:
                return False
            if start >= node.end:
                if node.right: 
                    return visit(start, end, node.right)
                else:
                    node.right = Node(start, end)
                    return True
            elif end <= node.start:
                if node.left:
                    return visit(start, end, node.left)
                else:
                    node.left = Node(start, end)
                    return True
        return visit(start, end, self.root)