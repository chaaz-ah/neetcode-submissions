class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}

        for c in s:
            count[c] = 1 + count.get(c,0)

        maxChar = max(count, key=count.get)

        for c in range(len(s)):
            if s[c] is not maxChar:
                s[c] = maxChar
                #bruh this sum buns brute force




        


