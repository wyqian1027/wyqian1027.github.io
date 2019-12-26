class Solution:
    def parseBoolExpr(self, s: str) -> bool:
        
        stack = []
        
        for i, ch in enumerate(s):
            if ch in "tf(!&|":
                stack.append(ch)
            elif ch == ")":
                group = []
                while stack and stack[-1] != "(":
                    group.append(stack.pop())
                stack.pop()
                op = stack.pop()
                stack.append(self.calc(op, group))
        return stack.pop() == "t"

    def calc(self, op, group):
        if op == "!":
            return "t" if group[0] == "f" else "f"
        elif op == "&":
            return "t" if all(x == "t" for x in group) else "f"
        elif op == "|":
            return "t" if any(x == "t" for x in group) else "f"
        return "f"