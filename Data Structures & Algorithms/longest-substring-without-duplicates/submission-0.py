class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 1
        maxCount = 1
        count = 1

        while right < len(s):
            if s[right] != s[left]:
                count += 1
                maxCount = max(maxCount, count)
            else: 
                count = 1
                left = right
            right += 1
        
        return maxCount

        #this all i got
