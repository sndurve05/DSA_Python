class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        i = 0 
        st = []
        
        while i<len(num):
                while k>0 and st and num[i] < st[-1]:
                    st.pop()
                    k -= 1
                st.append (num[i])
                i += 1
        while k > 0:
            st.pop()
            k -= 1
        ans = "".join(st).lstrip('0')
       

        if ans =="" :
            return "0"

        return ans    

    