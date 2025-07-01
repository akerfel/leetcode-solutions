class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = deque()
        for c in s:
            if c in ["(", "{", "["]:
                stack.append(c)
            else:
                if not stack:
                    return False
                if c == ")" and stack.pop() != "(":
                        return False
                if c == "}" and stack.pop() != "{":
                        return False
                if c == "]" and stack.pop() != "[":
                        return False
        return not stack


