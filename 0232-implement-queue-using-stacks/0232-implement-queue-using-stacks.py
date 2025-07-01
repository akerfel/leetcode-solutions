class MyQueue(object):
    def __init__(self):
        self.s1 = list()
        self.s2 = list()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.s1.append(x)
        
    def pop(self):
        """
        :rtype: int
        """
        for i in range(len(self.s1) - 1):
            self.s2.append(self.s1.pop())
        head = self.s1.pop()
        for i in range(len(self.s2)):
            self.s1.append(self.s2.pop())
        return head
        
    def peek(self):
        """
        :rtype: int
        """
        head = None
        n = len(self.s1)
        for i in range(n):
            popped = self.s1.pop()
            self.s2.append(popped)
            if i == n - 1:
                head = popped
        for i in range(len(self.s2)):
            self.s1.append(self.s2.pop())
        return head

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.s1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()