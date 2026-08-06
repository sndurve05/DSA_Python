class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []   #Traversing through left and storing in increasing order
        maxArea = 0 

        for i in range (len(heights)+1):
            curr = 0 if i== len(heights) else heights[i]   # if the elements are in increasing order ; our while loop wont allow to pop, hence at the end we add a imaginary height 0 so that all the stack indices go into while loop and the area gets calculated
        

            while stack and curr < heights[stack[-1]]:
                height = heights[stack.pop()]

                if stack:
                    width = i - stack[-1]-1
                else:
                    width = i 
                
                maxArea = max(maxArea, height * width)

            stack.append(i)

        return maxArea