class Solution:
    def simplifyPath(self, path: str) -> str:
        splits = path.split('/')
        stack = deque()
        for s in splits:
            if s == ".." and stack:
                stack.pop()
            elif s and s != "." and s != "..":
                stack.append(s)
        
        return "/" + "/".join(stack)