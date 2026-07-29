class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack=[]
        dict = {}
        
        for n in nums2:
            while stack and n>stack[-1]:  #Everyone in the stack is waiting. When a bigger number arrives, keep giving answers until nobody on top can be answered.
            #while stack means stack isnt empty.
                smaller = stack.pop() #take the latest element and if it greater than the topmost in stack then add it to dictionary.
                dict[smaller]=n

            stack.append(n)

        while stack:
            #now stack contains only the numbers that dont have a greater next number. So assign -1 to them.
            dict[stack.pop()]=-1

        ans =[]
        for num in nums1:
            ans.append(dict[num])

        return ans