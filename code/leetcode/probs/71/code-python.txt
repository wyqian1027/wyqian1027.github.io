class Solution:
    def simplifyPath(self, path: str) -> str:
        
        path = path.split("/")
        
        stack = []
        
        for el in path:
            if not el: continue;
            if el == ".." and stack:
                stack.pop()
            if el != "." and el != "..":
                stack.append(el)
        
        return "/" + "/".join(stack)