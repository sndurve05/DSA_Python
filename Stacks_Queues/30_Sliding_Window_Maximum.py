class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import deque
        d = deque()
        result = []

        for i,curr in enumerate(nums):
            
            while d and nums[d[-1]] <= curr:
                d.pop()
            d.append(i)

            if d[0] == i - k:
                d.popleft()

            if i >=k -1:
                result.append(nums[d[0]])

        return result
                