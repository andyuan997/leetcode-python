class Solution(object):

    # 跟第9題類似
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 題目給出上下限 因此放入
        MAX_INT = 2 ** 31 - 1  # 2,147,483,647
        MIN_INT = -2 ** 31  # -2,147,483,648

        result = 0
        y = abs(x)
        while y > 0:
            if result > MAX_INT / 10 or result < MIN_INT / 10:
                return 0
            result = result * 10 + (y % 10)
            y //= 10
        return result if x > 0 else -result


solution = Solution()
print(solution.reverse(1534236469))
