class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        result = ""
        need = {}
        window = {}
        have = 0
        shortest = len(s) +1

        for i in t:
            need[i] = need.get(i,0) + 1
        required = len(need) 

        for right in range(len(s)):
            window[s[right]] = window.get(s[right],0) +1 

            if s[right] in need and window[s[right]] == need[s[right]]:
                have += 1
            
            while have == required:
                if shortest > right - left +1:
                    shortest = right-left+1
                    result = s[left: right+1]

                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                        have -=1
                left += 1

        return result

            
        

        