def sumSubarrayMins(arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        sum = 0
        stack = []
        count = 1
        for i in range (len(arr)):
            if stack and arr[i]<arr[stack[-1]]:
                count = 1

            while stack and arr[stack[-1]] > arr[i]:
                count +=1   
                stack.pop()
            
            stack.append(i)
            sum += count * arr[stack[-1]]
            
        return sum


print(sumSubarrayMins([50]))