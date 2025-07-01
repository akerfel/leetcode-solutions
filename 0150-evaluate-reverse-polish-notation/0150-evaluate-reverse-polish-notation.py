class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        s = []
        for t in tokens:
            if t == "+":
                right = s.pop()
                left = s.pop()
                s.append(left + right)
            elif t == "*":
                right = s.pop()
                left = s.pop()
                s.append(left * right)
            elif t == "-":
                right = s.pop()
                left = s.pop()
                s.append(left - right)
            elif t == "/":
                right = s.pop()
                left = s.pop()
                s.append(int(float(left) / right))
            else:
                s.append(int(t))
        return s.pop()
