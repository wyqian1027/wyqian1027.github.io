# Two pass
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        def delete_invalid_close_symbol(s, open_symbol, close_symbol):
            sb = []
            left = right = 0
            for ch in s:
                if ch == open_symbol: 
                    left += 1
                elif ch == close_symbol and left > right: 
                    right += 1 
                elif ch == close_symbol and left == right:
                    continue
                sb.append(ch)
            return "".join(sb)
        
        s = delete_invalid_close_symbol(s, "(", ")")
        s = delete_invalid_close_symbol(s[::-1], ")", "(")
        
        return s[::-1]

# Alternative, from Solution:
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        indexes_to_remove = set()
        stack = []
        for i, c in enumerate(s):
            if c not in "()":
                continue
            if c == "(":
                stack.append(i)
            elif not stack:
                indexes_to_remove.add(i)
            else:
                stack.pop()
        indexes_to_remove = indexes_to_remove.union(set(stack))
        string_builder = []
        for i, c in enumerate(s):
            if i not in indexes_to_remove:
                string_builder.append(c)
        return "".join(string_builder)