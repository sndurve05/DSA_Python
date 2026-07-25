class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def totalHours(k):          #Calculates the hours 
            sum = 0 
            for n in piles:
                t = n//k
                if n%k !=0:        # If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
                    t+=1
                sum+=t

            if sum <= h :
                return True
            else:
                return False

        piles.sort()
        low = 1
        high = piles[-1]

        while low<=high:
            mid = low + (high-low)//2

            if totalHours(mid):
                high = mid -1
            else:
                low = mid+1
            
        return low