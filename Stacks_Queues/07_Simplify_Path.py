class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        components = path.split("/")
        st = []

        for comp in components:
            if comp == "" or comp == ".":
                continue
            
            if comp == "..":
                if st:
                    st.pop()
            else:
                st.append(comp)
        
        return "/" + "/".join(st)
