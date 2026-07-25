class Solution(object):
    def minimumTime(self, time, totalTrips):
        """
        :type time: List[int]
        :type totalTrips: int
        :rtype: int
        """

        def num_of_trips(n):
            total = 0
            for i in time:
                total += (n//i)
            return total

        low = 1
        high = max(time)*totalTrips
        minimum = float('inf')
        while low<=high:
            mid = low + (high-low)//2

            if num_of_trips(mid)>=totalTrips:
                minimum = min(minimum,mid)
                high = mid-1
            
            else:
                low = mid+1
        
        return minimum