class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        st = []
        
        for i in asteroids:
            while st and st[-1] > 0 and i < 0:
                if abs(st[-1])<abs(i):
                    st.pop()
                    continue

                elif abs(st[-1])==abs(i):
                    st.pop()
                break
            else:
                st.append(i)
      
        return st