class Solution:
    def frequencySort(self, s: str) -> str:
        count = {}
        freq = [[] for i in range(len(s)+1)]
        for i in s:
            count[i] = count.get(i, 0) + 1
        for c, amt in count.items():
            freq[amt].append(c)
        
        res = ""
        for val in range(len(freq)-1, 0, -1):
            for ch in freq[val]:
                res += ch * val

        return res
