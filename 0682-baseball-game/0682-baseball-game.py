class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = deque()
        for op in operations:
            if op == "+":
                stack.append(int(stack[-1]) + int(stack[-2]))
            elif op == "D":
                stack.append(int(stack[-1]) * 2)
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
        
        return sum(stack)