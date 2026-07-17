class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        charMap = {}

        if len(s1) > len(s2):
            return False

        for s in s1:
            charMap[s] = 1 + charMap.get(s,0)
        
        for left in range(len(s2) - len(s1) + 1):
            s2Map = {}

            for right in range(left, left + len(s1)):
                s2Map[s2[right]] = 1 + s2Map.get(s2[right],0)
            
            if charMap == s2Map:
                return True

        return False

        #yo this is so smart gpt helped me using my sol
                    





