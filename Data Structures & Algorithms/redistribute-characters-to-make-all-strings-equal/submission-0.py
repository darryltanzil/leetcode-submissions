from collections import defaultdict
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        freq = defaultdict(int)
        for word in words:
            for c in word:
                freq[c] += 1
    
        for key, value in freq.items():
            if value % len(words) != 0:
                return False
        
        return True