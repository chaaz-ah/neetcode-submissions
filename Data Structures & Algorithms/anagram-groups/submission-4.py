class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #i do not know what a defaultdict is 
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(s) - ord('a')] += 1
            res[tuple(count)].append(s) #also the tuple
        return list(res.values())
        #also explain the list(res.values())