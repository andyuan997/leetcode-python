"""
「Easy」題目來源：blind-75-leetcode-questions

268. Missing Number

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

"""
"""
題目是要從打亂的數列中找出缺失的排列數字
想法：
感覺就是用一種排序法，在排的時候順邊找出缺少的數字
但因為一定是從0開始，所以可以直接計數查找
結果就是暴力法 O(n^2)

優化解法：
數學公式解O(n)：直接利用公式就可以找到了（？傻眼

### 不知道為啥題目被分到Binary下，要用Binary Search要先排序，因此最終O(n log n)	會比較慢
"""


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        # 暴力法
        for i in range(len(nums)):
            try:
                nums.index(i)
            except:
                return i
        return len(nums)
        """
        n = len(nums)
        return (n * (n + 1)) // 2 - sum(nums)




nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]

solution = Solution()
print(solution.missingNumber(nums))

