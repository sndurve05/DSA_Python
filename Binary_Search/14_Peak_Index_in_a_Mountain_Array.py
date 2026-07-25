class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        low = 1
        high = len(arr)-2

        if arr[0]>arr[1]:
            return 0
        elif arr[-1]>arr[-2]:
            return len(arr)-1

        while low<=high:
            mid = low+(high-low)//2
           
            if arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid

            elif arr[mid-1]<arr[mid]:
                low = mid+1

            elif arr[mid] > arr[mid+1]:
                high = mid-1

                    