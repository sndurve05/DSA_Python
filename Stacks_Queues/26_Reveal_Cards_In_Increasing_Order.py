class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort()

        result = [0]*len(deck)
        index_queue = deque(range(len(deck)))

        d = 0 # deck_index
        skip = False

        while index_queue:
            curr_index = index_queue.popleft()

            if not skip :
                result[curr_index] = deck[d]
                d+=1
            
            else:
                index_queue.append(curr_index)

            skip = not skip 

        return result


            
        