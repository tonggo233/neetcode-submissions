class Solution:
    def isValid(self, s: str) -> bool:
        pair = {"]":"[","}":"{",")":"("}

        st = []
        for i in s:
            if i not in pair :
                st.append(i)
            else:
                if not st or pair[i] != st[-1]:
                   return False
                st.pop()
            
        return len(st) == 0
        