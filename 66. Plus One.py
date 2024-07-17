class Solution(object):

    # 我的解法
    def plusOne_x(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        x = len(digits)
        digits[-1] += 1
        for bit in range(len(digits)):
            if digits[-bit-1] == 10:
                digits[-bit - 1] = 0
                if digits[0] != 0:
                    digits[-bit - 2] += 1
                else:
                    return [1] + [0] * x

        return digits

    # ChatGPT
    def plusOne(digits):
        n = len(digits)

        # 從最後一個數字開始處理
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        # 如果所有的數字都是9，那麼最終會在開頭新增一個1
        return [1] + [0] * n




solution = Solution()
digits = [9,9,9]
print(solution.plusOne(digits))
