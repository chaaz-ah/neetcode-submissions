class Solution:
    def isPalindrome(self, s: str) -> bool:
        #subs after are all looked up 
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]