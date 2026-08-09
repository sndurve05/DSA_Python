class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        from collections import deque

        queue = deque(range(len(tickets)))  #store indices
        total_time = 0

        while queue:
            curr_index = queue.popleft() 

            tickets[curr_index] -=1
            total_time  +=1

            if curr_index == k and tickets[curr_index]==0:
                return total_time

            if tickets[curr_index] >0 :
                queue.append(curr_index)

        return total_time