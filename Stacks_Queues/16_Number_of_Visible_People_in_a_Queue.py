class Solution(object):
    def canSeePersonsCount(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        n = len(heights)
        st = []     
        ans = [0] * n
        for i in range (n-1, -1 , -1):
            
            while st and heights [i] > heights[st[-1]]:
                ans[i] +=1
                st.pop()

            if st:
                ans[i]+=1

            st.append(i)

        return ans
        