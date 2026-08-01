class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import deque

        d = deque()
        for i in s:
            
            if (d and (i.islower() and d[-1].isupper() and i == d[-1].lower())) or (d and (i.isupper() and d[-1].islower() and i == d[-1].upper())):
                d.pop()
                
            else:
                d.append(i)
               

        if len(d)==0:
            return ""
        s = "".join(d)
        return s
