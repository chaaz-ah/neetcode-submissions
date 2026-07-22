class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        countT = {}
        window = {}

        res = [-1, 0]
        resLen = float("infinity")

        for i in t:
            countT[i] = 1 + countT.get(i, 0)

        need = len(countT)
        have = 0

        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1 

            
            
            while have == need:
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    res = [l, r]
            
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1 

                l += 1
        
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""
        #watched vid and drew it out


            


        