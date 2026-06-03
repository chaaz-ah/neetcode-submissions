class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final: List[List[str]] = [[]]
        final.append([])
        for i, string_1 in enumerate(strs):
            char_1 = {}

            for j, string_2 in enumerate(strs, i+1):
                char_2 = {}
                if len(string_1) == len(string_2):
                    for j in range(len(string_1)):
                        char_1[string_1[j]] = 1 + char_1.get(string_1[j], 0)
                        char_2[string_2[j]] = 1 + char_2.get(string_2[j], 0)
                
                    if char_1 == char_2:
                        final.append([]) 
                        final[i].append([string_1, string_2])

        return final

        #yea claude im stuck imma js look at the soltuion for the next submission and submit that 