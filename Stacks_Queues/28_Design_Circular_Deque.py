class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.k = k
        self.deque = [0]*k
        

        self.front = 0
        self.rear = -1
        self.count = 0


    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.front = (self.front -1 )%self.k
        self.deque[self.front] = value
        self.count +=1
        return True

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False

        self.rear = (self.rear + 1) % self.k
        self.deque[self.rear] = value
        self.count+=1
        return True
        

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.k
        self.count -= 1
        return True


    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False

        self.rear = (self.rear - 1) % self.k
        self.count -= 1
        return True


    def getFront(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.deque[self.front]
        

    def getRear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.deque[self.rear]


    def isEmpty(self):
        """
        :rtype: bool
        """
        if self.count == 0:
            return True
        return False


    def isFull(self):
        """
        :rtype: bool
        """
        if self.count == self.k:
            return True
        return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()