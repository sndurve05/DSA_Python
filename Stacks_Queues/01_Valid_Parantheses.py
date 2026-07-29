class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        a =[]
        for i in s:
            if i=='(' or i=='{' or i=='[':
                a.append(i)
            else:
                if not a:
                    return False
                top = a.pop()
                if i==')' and top != '(':
                    return False
                elif i=='}' and top != '{':
                    return False
                elif i==']' and top != '[':
                    return False
                
        return len(a)==0 