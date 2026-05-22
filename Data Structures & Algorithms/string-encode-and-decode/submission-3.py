class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes = []
        res = ""
        for s in strs:
            sizes.append(len(s))
        for sz in sizes:
            res += str(sz)
            res += ','
        res += '#'
        for s in strs:
            res += s
        return res


    def decode(self, s: str) -> List[str]:
        #5,5#HelloWorld
        if not s:
            return []
        sizes = []
        dec = []
        i = 0
        while s[i] != '#':
            cur = ""
            while s[i] != ',':
                cur += s[i]
                i += 1
            sizes.append(int(cur))
        i += 1
        for sz in sizes:
            dec.append(s[i:i+sz])
            i += sz
        return dec
