class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = deque()
        for c in s:
            if c == "(":
                stack.append(1)
            elif c == "{":
                stack.append(2)
            elif c == "[":
                stack.append(3)
            else:
                if not stack:
                    return False
                elif c == ")" and stack.pop() != 1:
                        return False
                elif c == "}" and stack.pop() != 2:
                        return False
                elif c == "]" and stack.pop() != 3:
                        return False
        return not stack