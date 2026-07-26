#TLE:
'''def maximumCandies(candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        original = candies.copy()
        if sum(candies)<k:
            return 0

        def piles(x,candies): # x is candies per child 
          
            i = 0 
            children = 0
            while i<len(candies) :
                print(candies)
                if candies[i]>=x:
                    candies[i]=candies[i]-x
                    children +=1
                else:
                    i+=1

            if children >= k:
                print("returning true",x,children)
                return True
            print("returning false",x)
            return False
           
        low = 1 
        high = max(candies)
        ans = 0
        while low<=high:
            mid = low + (high-low)//2
            print(low,high,mid,original)
            if piles(mid,original.copy()):
                ans = max(mid,ans)
                low = mid+1

            else:
                high = mid-1

        return ans


print(maximumCandies([1,2,3,4,10], 5))'''


class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        
        if sum(candies)<k:
            return 0

        low = 1 
        high = max(candies)   #piles are allowed to go unsed
        ans = 0

        while low<=high:
            mid = low + (high-low)//2

            children_fed = sum(candy // mid for candy in candies)
            
            if children_fed >= k:
                ans = mid      # mid is a valid answer, try to find a larger one
                low = mid + 1
            else:
                high = mid - 1
                
        return ans