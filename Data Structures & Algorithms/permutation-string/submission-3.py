class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counts = [0] * 26
        s2_counts = [0] * 26

        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            s1_counts[ord(s1[i])-97] += 1
            s2_counts[ord(s2[i])-97] += 1

        if s1_counts == s2_counts:
            return True
        
        for right in range(len(s1), len(s2)): #bro i was so confused for long time as to why its this range
            s2_counts[ord(s2[right])-97] += 1
            s2_counts[ord(s2[right - len(s1)])-97] -= 1
            if s1_counts == s2_counts:
                return True
        return False

        #im getting really confused as to the index and ranges where start stop which indices to use and stuff where to essentially start and stop the windows