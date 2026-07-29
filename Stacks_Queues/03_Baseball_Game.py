class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        ans = []
        for i in operations:              
            if ans and i =='C':
                ans.pop()

            elif ans and i == 'D':
                top = int(ans[-1])
                ans.append(top*2)

            elif ans and i == '+':              
                ans.append(int(ans[-1]) + int(ans[-2]))

            else:
                ans.append(int(i))
        return sum(ans)