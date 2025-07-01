class MinStack(object):

    def __init__(self):
        self.stack = list()
        self.minstack = list()

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if len(self.minstack) == 0:
            minv = val
        else:
            minv = min(val, self.minstack[-1])
        self.stack.append(val)
        self.minstack.append(minv)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minstack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()