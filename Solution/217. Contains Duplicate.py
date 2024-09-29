class Solution:

    # 我寫的
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_table = {}
        for index, num in enumerate(nums):
            target = num
            if target in hash_table:
                return True
            hash_table[num] = index
        return False

    # 改進
    def containsDuplicate(nums):
        hash_table = {}  # 建立一個空字典
    
        for num in nums:
            if num in hash_table:  # 如果元素已經存在於 hash_table 中
                return True        # 表示有重複，返回 True
            hash_table[num] = 1    # 否則將元素加入 hash_table，值設為 1
    
        return False               # 若無重複元素，返回 False

    # 用Set

    def containsDuplicate(nums):
        # 建立一個空的 Set
        seen = set()
        
        # 遍歷每個元素
        for num in nums:
            # 如果該元素已經在 Set 中，表示有重複元素
            if num in seen:
                return true
            # 否則將元素加入 Set 中
            seen.add(num)
        
        # 沒有重複元素，返回 false
        return False
