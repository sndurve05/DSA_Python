class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
   
        def ship(capacity):
        
            reqd_day = 1
            current_weight = 0

            for weight in weights:

                if current_weight + weight > capacity:
                    reqd_day += 1
                    current_weight = 0

                current_weight += weight

            return reqd_day <= days
                
        
        low=max(weights)
        high = sum(weights)
        
        while low<=high:
            mid = low+(high-low)//2
 
            if ship(mid):
                high=mid-1
            else:
                low=mid+1

        return low