class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0 
        high = len(nums)-1
        minimum = float('inf')

        if nums[low]<nums[high]:
            return nums[low]

        while low<=high:
            mid = low + (high-low)//2

            if nums[low]==nums[mid]==nums[high]:
                minimum= min(minimum,nums[mid])
                low +=1
                high-=1
            
            elif nums[low]<=nums[mid]:
                minimum =min(minimum,nums[low])
                low = mid +1

            elif nums[mid]<=nums[high]:
                minimum = min(minimum,nums[mid])
                high=mid-1

        return minimum

                   