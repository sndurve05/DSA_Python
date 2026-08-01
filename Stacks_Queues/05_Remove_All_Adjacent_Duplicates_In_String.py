class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import deque

        d = deque()

        for i in s:
            if d and i == d[-1]:
                d.pop()
            
            else:
                d.append(i)

        s = "".join(d)
        return s