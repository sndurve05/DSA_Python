class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        '''
        Tracking indexes separately from the queue. 
        This means that, we pop the unwanted element after the given gap of k.
        These indexes are not realted to the deque or original list.

        The deque is being physically rotated to bring the logical target to the front, 
        while curr_index keeps track of the logical position.
        '''

        from collections import deque
        d = deque(range(1,n+1))
        curr_index = 0  #using it as a logical counter that tracks where you are in the circular elimination process.

        while len(d)>1 :
            target_index = (curr_index + k - 1) % len(d)

            while curr_index != target_index :
                d.append(d.popleft())
                curr_index = (curr_index + 1) % len(d)

            if curr_index == target_index :
                d.popleft()
                curr_index = (curr_index + 1) % len(d)
        
        return d.popleft()
            