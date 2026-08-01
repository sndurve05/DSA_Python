class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        from collections import deque

        d = deque()

        for i in tokens:
           
            if i == '+':
                a = d.pop()
                b = d.pop()
                d.append(int(a)+int(b))

            if i == '-':
                a = d.pop()
                b = d.pop()
            
                d.append(int(b)-int(a))

            if i == '*':
        
                a = d.pop()
                b = d.pop()
        
                d.append(int(a)*int(b))
           
            if i == '/':
                a = d.pop()
                b = d.pop()
                c = b // a
                if c < 0 and b % a != 0:
                    c += 1 
                d.append(c)

            if i.lstrip('-').isdigit():
                d.append(int(i))

        return d.pop()