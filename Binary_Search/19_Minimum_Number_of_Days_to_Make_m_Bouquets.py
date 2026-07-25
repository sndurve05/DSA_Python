class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        if len(bloomDay)<(m*k):
            return -1

        def bouquet(day):
            num_of_bouquets = 0
            count = 0
            for i in bloomDay:

                if i<=day:
                    count +=1 # adding flower in a bouquet
                else:
                    count=0  #break and reset count to 0 as we only consider adajcent flowers in the bouquet
                
                if count == k: #if bouquet limit satisfied then increase num of bouquet and reset count to 0
                    num_of_bouquets +=1
                    count=0

            return num_of_bouquets
        
        low =1
        high = max(bloomDay)
        minimum = max(bloomDay)

        while low<=high:
            mid = low+(high-low)//2

            if bouquet(mid)>=m:
                minimum = min(minimum,mid)
                high = mid-1
            else:
               
                low= mid+1
            
        return minimum