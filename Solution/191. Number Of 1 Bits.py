"""
「Easy」題目來源：blind-75-leetcode-questions

191. Number Of 1 Bits.

Given a positive integer n, write a function that returns the number of
set bits in its binary representation (also known as the Hamming weight).
"""
"""
2025/2/17
時間複雜度約為 O(log n)，因為 n 轉成二進位後的長度是 log n，計算 1 的數量也是 log n 的長度。
"""
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')


solution = Solution()


print(solution.hammingWeight(10))
