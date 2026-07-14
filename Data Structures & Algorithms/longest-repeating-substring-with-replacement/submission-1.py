class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = set(s)

        for c in charSet:
            left = 0
            count = 0
            for right in range(len(s)):
                if s[r] == c:
                    count += 1
                
                while (r - l + 1) - count > k:
                    l += 1
                    if s[l] == c:
                        count -= 1
                    l += 1
                
                res = max(res, r-l +1)
        return res

        #i dont fully get this yet but ill relook

                




        


