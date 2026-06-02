class Solution:
    def isPalindrome(self, s: str) -> bool:
        #s = "".join(s.split())#.lower() this is what i tried first before realiszing all not alpha char and seardhred up some syntax tho
        s = "".join(char for char in s if char.isalpha())
        s = s.lower()
        reversed = s[::-1]
        if s == reversed:
            return True
            print("bruh")
        return False