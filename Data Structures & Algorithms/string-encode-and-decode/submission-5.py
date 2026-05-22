class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        enc = ""
        for s in strs:
            enc += str(len(s))
            enc += '#'
            enc += s
        return enc


    def decode(self, s: str) -> List[str]:
        #5,5#HelloWorld
        if not s:
            return []
        dec = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length 
            dec.append(s[i:j])
            i = j
        return dec

            
            
