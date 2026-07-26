class Solution(object):
    def minSpeedOnTime(self, dist, hour):
        """
        :type dist: List[int]
        :type hour: float
        :rtype: int
        """
        if hour <= len(dist) - 1:
            return -1

        def hoursRequired(speed):
            totalHours=0
            for i in range(len(dist)-1):

                t = float(dist[i]//speed)          # we cant do float(dist[i]//speed) because it first evaluates int divided int and then just makes it float. So for e.g. if it is 2 float converts it to 2.0
                
                if dist[i]<speed or dist[i] % speed != 0:
                    t+=1
                totalHours+=t
            
            totalHours += float(dist[-1])/speed
           
            return totalHours<=hour

        low = 1
        high = 10**7
        min_speed = -1

        while low<=high:
            mid = int(low + (high-low)//2)

            if hoursRequired(mid):
                min_speed = mid
                high = mid-1

            else:
                low = mid+1

        return min_speed