from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = Counter(s)

        for char in s:
            if hash_map[char] == 1:
                return s.index(char)
        
        return -1
