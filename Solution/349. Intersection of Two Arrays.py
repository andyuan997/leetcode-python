
class Solution:

    # 我寫的
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2 = set(nums2)
        output = set()

        for i in nums1:

            if i in nums2:
                output.add(i)

        return output

    # 更好的方法
    def intersection(self, nums1, nums2):
        # 將兩個數組轉換為集合，去除重複元素
        set1 = set(nums1)
        set2 = set(nums2)
        
        # 使用集合的交集方法
        result = set1.intersection(set2)
        
        # 返回結果轉為列表
        return list(result)

    # hash table
    def intersection(self, nums1, nums2):
        # 使用 Hash Table 來儲存 nums1 的所有元素
        hash_table = set(nums1)
        
        # 檢查 nums2 中的元素是否存在於 Hash Table 中
        result = set()
        for num in nums2:
            if num in hash_table:
                result.add(num)
                
        # 返回結果轉為列表
        return list(result)

