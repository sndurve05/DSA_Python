class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False

        st = [] #stores a tuple with max acceptable number and the minimum till now 
        first_num = nums[0]
        for i in range(1, len(nums)):
            
            while st and nums[i] >= st[-1][0]:
                st.pop()
            if st and nums[i] > st[-1][1]:
                return True
       
            st.append((nums[i],first_num))
            first_num = min (first_num, nums[i])

        return False