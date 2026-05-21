class Solution:

    def encode(self, strs: List[str]) -> str:
        final = ""
        for i in strs:
            final += i + " "
        return final

    def decode(self, s: str) -> List[str]:
        final_lt = []
        word = ""

        for i in range(len(s)):
            if s[i] == " ":
                final_lt.append(word)
                word = ""
            else:
                word += s[i]

        return final_lt

        # chatgpt solved the whole decode lol