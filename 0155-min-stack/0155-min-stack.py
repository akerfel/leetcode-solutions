class MinStack(object):

    def __init__(self):
        self.nodes = list()
        self.tailIndex = -1

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.tailIndex == -1:
            minv = val
        else:
            minv = min(val, self.nodes[self.tailIndex].minv)
        self.nodes.append(Node(val, minv))
        self.tailIndex += 1

    def pop(self):
        """
        :rtype: None
        """
        self.nodes.pop()
        self.tailIndex -= 1

    def top(self):
        """
        :rtype: int
        """
        return self.nodes[-1].value

    def getMin(self):
        """
        :rtype: int
        """
        return self.nodes[-1].minv
        
class Node(object):

    def __init__(self, value, minv):
        self.value = value
        self.minv = minv

    def __str__(self):
        return "value: {}, minv: {}".format(self.value, self.minv)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()