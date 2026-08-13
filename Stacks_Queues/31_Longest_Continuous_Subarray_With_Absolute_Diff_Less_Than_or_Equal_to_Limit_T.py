class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        from collections import deque
        max_d = deque()
        min_d = deque()
        left = 0
        length = 0
        for right in range(len(nums)):
            
            while max_d and nums[max_d[-1]] < nums[right]:
                max_d.pop() # monotonic stack: decreasing order

            max_d.append(right)

            while min_d and nums[min_d[-1]] > nums[right]:
                min_d.pop() #monotonic stack: increasing order

            min_d.append(right)

            while nums[max_d[0]] - nums[min_d[0]] > limit:

                if max_d[0] == left:
                    max_d.popleft()

                if min_d[0] == left:
                    min_d.popleft()

                left += 1

            length = max(length, right - left + 1)

        return length