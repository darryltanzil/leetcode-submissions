class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        Hello World -> 5#Hello6#World
                              i 
                              j
        """
        res = []
        for s in strs:
            res.append(str(len(s)) + "#" + s)
        return "".join(res)
                
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i

            # grab the length
            length = []
            while s[j] != "#":
                length.append(s[j])
                j += 1
            length = int("".join(length))
            i = j + 1 
            j = i + length
            res.append(s[i:j])
            i = j
        return res
            

