class Solution:
    
    def findTheDifference(self, s: str, t: str) -> str:
        hash_map = {}
        for char in s:
            if char in hash_map:
                hash_map[char] += 1
            else:
                hash_map[char] = 1
        
        for char in t:
            if char not in hash_map or hash_map.get(char) == 0:
                return char
            else:
                hash_map[char] -= 1

    # 改進
    def findTheDifference(self, s: str, t: str) -> str:
        # 初始化哈希表來計算 s 中每個字符的出現次數
        hash_map = {}
        for char in s:
            hash_map[char] = hash_map.get(char, 0) + 1  # 如果字符存在則增加計數，否則初始化為 1

        # 遍歷 t 中的字符來查找多出來的那個字符
        for char in t:
            if char not in hash_map or hash_map[char] == 0:  # 如果字符不在 hash_map 中或次數為 0
                return char
            hash_map[char] -= 1  # 減少計數
