class Solution:

    def wordPattern(self, pattern: str, s: str) -> bool:
        hash_map = {}
        s = s.split(" ")
        counter = 0

        if len(pattern) != len(s):
            return False

        for char in pattern:
            if hash_map.get(char):
                if hash_map[char] != s[counter]:
                    return False
            else:
                if s[counter] in hash_map.values():
                    return False
                hash_map[char] = s[counter]
            counter += 1
        return True


    

    
    # 優化
    def wordPattern(self, pattern: str, s: str) -> bool:
        # 將 s 分割為單詞列表
        words = s.split(" ")
        
        # 如果 pattern 和 words 的長度不同，直接返回 False
        if len(pattern) != len(words):
            return False

        # 創建兩個映射字典：pattern -> word 和 word -> pattern
        pattern_to_word = {}
        word_to_pattern = {}

        # 遍歷 pattern 和 words 中的每一個元素
        for char, word in zip(pattern, words):
            # 檢查 pattern 中的字母是否已經有對應的單詞
            if char in pattern_to_word:
                # 如果對應的單詞不同，返回 False
                if pattern_to_word[char] != word:
                    return False
            else:
                # 檢查該單詞是否已經對應到其他字母
                if word in word_to_pattern:
                    return False
                # 建立新的映射
                pattern_to_word[char] = word
                word_to_pattern[word] = char

        # 如果所有條件都符合，返回 True
        return True
