class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        maxf = 0
        left = 0
        need = {}
        for c in s1:
            need[c] = 1 + need.get(c, 0)

        window = {}
        m = len(s1)
        for right in range(len(s2)):
            window[s2[right]] = window.get(s2[right], 0) + 1

            if right >= m:
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    del window[s2[left]]
                left+=1
            if window == need:
                return True
        return False
