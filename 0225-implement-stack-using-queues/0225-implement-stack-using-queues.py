class MyStack(object):

    def __init__(self):
        self.d = deque()
        
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.d.append(x)

    def pop(self):
        """
        :rtype: int
        """
        n = len(self.d)
        for i in range(n):
            popped = self.d.popleft()
            if i < n - 1:
                self.d.append(popped)
            else:
                return popped

    def top(self):
        """
        :rtype: int
        """
        popped = self.pop()
        self.d.append(popped)
        return popped

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.d) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()