class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import Counter

        count_s = Counter(s)
        count_t = Counter(t)

        for ch in t:
            if count_s[ch]!=count_t[ch]:
                return ch

