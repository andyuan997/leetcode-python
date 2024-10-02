class Solution:

    # 排序簡單解法
    def isAnagram(s: str, t: str) -> bool:
      return sorted(s) == sorted(t)

    # 使用 hash map 方法
    def isAnagram(self, s: str, t: str) -> bool:
        # 如果兩字串長度不一致，直接回傳 False
        if len(s) != len(t):
            return False
        
        # 創建一個字典來記錄字母次數
        count = {}
        
        # 計算 s 中每個字母的次數
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        # 減少 t 中每個字母的次數
        for char in t:
            if char in count:
                count[char] -= 1
            else:
                return False
        
        # 最後檢查每個字母的次數是否都為 0
        for value in count.values():
            if value != 0:
                return False
        
        return True
        
    from collections import Counter
    # 優化
    def isAnagram(s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
