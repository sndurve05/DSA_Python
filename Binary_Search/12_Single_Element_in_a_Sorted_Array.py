def singleNonDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0 
        high = len(nums)-1
        
        while low<=high:
            mid = low + (high-low)//2
            print(mid)
            if nums[mid]!=nums[mid+1] and nums[mid]!=nums[mid-1]:
                print("in if part")
                return nums[mid]

            elif nums[mid]==nums[mid+1]:
                low = mid+1
                print("entered",mid)

            elif nums[mid]==nums[mid-1]:
                print("bottom part ",mid)
                
                high = mid-1


print(singleNonDuplicate([1,1,2,3,3,4,4,8,8]))