class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        charSet = set(s1)
        
        left = 0
        for right in range(len(s2)):
            if s2[right] in charSet:
                while right in range(len(s1) + 1):
                    left = right
                    right += 1
                    if right in charSet:
                        break
                return True
        return False

        #this allllll i got i think its a good attempt ngl idk gonna check answer
                    





