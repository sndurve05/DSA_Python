def backspaceCompare( s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = []
        p = []
        for i in s:
            if d and i == "#":
                d.pop()
            else:
                if i != "#":
                    d.append(i)
       
        for a in t:
            if p and a == "#":
                p.pop()
            else:
                if a != '#':
                    p.append(a)
      
        return p==d


print(backspaceCompare("y#fo##f","y#f#o##f"))