class Solution:

    def encode(self, strs: List[str]) -> str:
        final = ""
        for i in strs:
            final += i
        return final

    def decode(self, s: str) -> List[str]:
        space_count = 0
        for i in range(len(s)):
            if s[i] == " ":
                space_count += 1
        final_lt = [0] * space_count
        for i in range(len(s)):
            for j in range(space_count):
                while letter != " ":
                    final_lt[j] += s[i]

        return final_lt

        #as far as i got before turning to chatgpt