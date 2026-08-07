class RecentCounter(object):
    from collections import deque
    def __init__(self):
        self.queue = deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.queue.append(t)

        min_time = t - 3000
        while self.queue and self.queue[0]<min_time:
            self.queue.popleft()
        

        return len(self.queue)
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)