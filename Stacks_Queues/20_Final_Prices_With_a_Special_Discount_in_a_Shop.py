class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        n = len(prices)
        ans = prices[:]
        stack =[]
        for i in range (n-1, -1, -1):
            while stack and prices[i] < prices[stack[-1]]:
                stack.pop()

            if stack:
                ans[i] = prices[i]-prices[stack[-1]]


            stack.append(i)
        return ans