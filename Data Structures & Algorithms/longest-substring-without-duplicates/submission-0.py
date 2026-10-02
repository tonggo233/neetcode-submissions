class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        noDuplicate = set()

        for right in range(left, len(s)):
            while s[right] in noDuplicate:
                noDuplicate.remove(s[left])
                left += 1
            noDuplicate.add(s[right])
            longest = max(longest, right-left+1)
        return longest

