class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # windows size - Maxoccur <= k 

        left = 0
        occur = {}
        maxOccur = 0
        result = 0

        for right in range(len(s)):
            occur[s[right]] = occur.get(s[right],0)+1
            maxOccur = max(maxOccur, occur.get(s[right]))
            
            while right - left + 1 - maxOccur > k:
                occur[s[left]] -= 1
                left += 1
            
            
            
            result = max(result, right-left+1)

        return result


        