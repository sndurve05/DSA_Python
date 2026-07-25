class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        def sumforDivision(k):
            sum = 0
            for i in nums:
                t = i//k
                if i<0 or i%k != 0:
                    t = t+1
                sum += t
            if sum <= threshold:
                return True
            else:
                return False
                
        nums.sort()
        low = 1
        high = nums[-1]
        while low<=high:
            mid = low + (high-low)//2

            if sumforDivision(mid):
                high = mid-1

            else:
                low = mid+1

        return low
