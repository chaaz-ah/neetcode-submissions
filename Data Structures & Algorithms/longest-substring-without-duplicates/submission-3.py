class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        countMax = 0

        for right in range(len(s)):
            if s[right] not in seen:
                seen.add(s[right])
                countMax = max(len(seen), countMax)
                right+= 1
            else:
                if s[left] in seen:
                    seen.remove(s[left])
                left+=1
                countMax = max(len(seen), countMax)
        return countMax

        
                    