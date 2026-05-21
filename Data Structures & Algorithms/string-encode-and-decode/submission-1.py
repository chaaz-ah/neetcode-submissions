class Solution:

    def encode(self, strs: List[str]) -> str:
        final = ""
        for i in strs:
            final += i + " "
        return final

    def decode(self, s: str) -> List[str]:
        space_count = 0
        for i in range(len(s)):
            if s[i] == " ":
                space_count += 1
        final_lt = [""] * space_count
        for i in range(len(s)):
            for j in range(space_count):
                while s[i] != " ":
                    final_lt[j] += s[i]
                    i+=1

        return final_lt

        #chatgpt but still doesnt work