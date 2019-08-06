# Two solutions Both O(N) time
# O(N) space
def check_identical_string(A, B):
    stack_A = []
    stack_B = []
    for ch in A:
        if A and ch == "#":
            stack_A.pop()
        elif ch != "#":
            stack_A.append(ch)
    for ch in B:
        if B and ch == "#":
            stack_B.pop()
        elif ch != "#":
            stack_B.append(ch)
    return stack_A == stack_B
    
# O(1) space
def check_identical_string(A, B):
    p1, p2 = len(A)-1, len(B)-1
    while p1 >= -1 and p2 >= -1:
        n1 = n2 = 0
        while p1 >= 0 and (A[p1] == "#" or n1 > 0):
            n1 = n1 + 1 if A[p1] == '#' else n1 - 1
            p1 -= 1
        while p2 >= 0 and (B[p2] == "#" or n2 > 0):
            n2 = n2 + 1 if B[p2] == '#' else n2 - 1
            p2 -= 1
        if p1 < 0 and p2 < 0:
            return True
        if p1 > 0 and p2 > 0 and A[p1]!= B[p2]:
            return False
        if p1 <= -1 and p2 >= 0 or p2 <= -1 and p1 >= 0:
            return False
        p1, p2 = p1 - 1, p2 - 1
    return True
            
        
        