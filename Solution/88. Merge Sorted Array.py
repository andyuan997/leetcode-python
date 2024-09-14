class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        """
        想法：
        判斷num1[0]跟num2[0]大小
        依序判定排列
        
        答案：
        把比較大的塞到num1 最後
        """

        for i in range(1, m + n + 1):
            if n == 0:
                break
            elif m == 0:
                nums1[-i] = nums2[n - 1]
                n -= 1
                continue

            if nums1[m - 1] < nums2[n - 1]:
                nums1[-i] = nums2[n - 1]
                n -= 1
            else:
                nums1[-i] = nums1[m - 1]
                m -= 1
        return nums1









solution = Solution()
num1 = [1, 2, 3, 0, 0, 0]
m = 3
num2 = [2, 5, 6]
n = 3
print(solution.merge(num1 , m, num2, n))
