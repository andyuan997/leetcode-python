class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = {}  # 使用 Hash Map 記錄字符最後出現的位置
        left = 0  # 左指針初始化
        max_length = 0  # 最大無重複子字串長度

        # 使用右指針遍歷字串
        for right, char in enumerate(s):
            # 如果字符已經出現在 Hash Map 中，並且其索引大於等於左指針，移動左指針
            if char in hash_map and hash_map[char] >= left:
                left = hash_map[char] + 1

            # 更新當前字符在 Hash Map 中的位置
            hash_map[char] = right

            # 計算當前無重複子字串的長度，並更新最大長度
            max_length = max(max_length, right - left + 1)

        return max_length
