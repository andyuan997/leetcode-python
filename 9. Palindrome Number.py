class Solution(object):

    # 基本 會用到字串轉換
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if str(x)[::-1] == str(x):
            return True
        return False

    # 反轉int放到新的變數中
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        inputNum = x
        newNum = 0

        while x > 0:
            # 取 x 的最後一位數並加到 newNum 的末尾
            newNum = newNum * 10 + x % 10
            # 去掉 x 的最後一位數
            x = x // 10

        # 比較反轉後的數字和原始數字是否相等
        return newNum == inputNum

    #最優解 反轉int放到新的變數中 並只經歷一半
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # 負數和以0結尾但不是0本身的數字不是回文數
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # 當數字長度為奇數時，可以通過 reversed_half // 10 去掉中間的數字
        return x == reversed_half or x == reversed_half // 10


solution = Solution()
print(solution.isPalindrome(x=-535))
