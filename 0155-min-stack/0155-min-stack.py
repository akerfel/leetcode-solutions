class MinStack(object):

    def __init__(self):
        self.nodes = list()

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.nodes:
            minv = val
        else:
            minv = min(val, self.nodes[-1].minv)
        self.nodes.append(Node(val, minv))

    def pop(self):
        """
        :rtype: None
        """
        self.nodes.pop()

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