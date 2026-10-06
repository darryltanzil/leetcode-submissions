class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s): 
            j = i
            # determine length
            length = 0
            while s[j] != "#":
                length = (length*10) + int(s[j])
                j += 1
            i = j+1
            j = i + length
            res.append(s[i:j])
            i = j
        return res