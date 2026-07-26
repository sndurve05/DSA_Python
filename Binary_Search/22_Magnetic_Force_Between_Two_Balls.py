class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        position.sort()
        def validGap(x):
            prev_ball_position = position[0]
            balls_placed= 1

            for i in range(1,len(position)):
                # Iterate on each 'position' and place a ball there if we can place it.
                curr_position = position[i]
                
                if curr_position - prev_ball_position>=x:
                    balls_placed +=1
                    prev_ball_position = curr_position

                if balls_placed ==m :
                    return True
            return False


            
        low = 1
        high = position[-1]-position[0]
        ans = -1
        while low<=high:
            mid = low + (high-low)//2

            if validGap(mid):
                ans = mid
                low = mid+1

            else:
                high = mid-1

        
        return ans