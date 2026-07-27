class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        from collections import Counter
        
        count_stones = Counter(stones)
        sum =0
        for i in jewels:
            sum += count_stones[i]

        return sum