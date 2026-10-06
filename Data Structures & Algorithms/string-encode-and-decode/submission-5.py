class Solution:
    """
    Format is the length, then comma, and then the elements, then comma

    ex. ["Hello","World"] -> "Hello#5World#5"
    Hello5
    ^    ^

    """
    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            count = 0
            for c in s:
                res.append(c)
                count += 1
            res.append("#")
            res.append(str(count))
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        "iterate backwards, check count and then grab that amt"
        curr = len(s)-1
        res = []
        length = ""
        while curr >= 0:
            # determine the number
            if s[curr] != "#":
                length += s[curr]
                curr -= 1
                continue
            count = curr - int(length[::-1])
            res.append(s[count:curr]) # from the curr to the count of the word
            curr = count-1
            length = ""
        return res[::-1]


