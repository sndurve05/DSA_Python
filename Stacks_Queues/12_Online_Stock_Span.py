class StockSpanner(object):
    # WE get price one by one,, entire stock list is not available

    def __init__(self):
        self.st = [] #stores tuple (price, span) (span is the day count we need)

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        span = 1
        while self.st and self.st[-1][0] <= price : 
            # self.st [-1] is the last tuple 
            # self.st [-1][0] is the first element of that tuple
            span += self.st.pop()[1]

        self.st.append((price,span))
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)