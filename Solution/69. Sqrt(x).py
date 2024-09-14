class Solution(object):

    # 我的方法
    def mySqrt_x(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0: return 0
        if x == 1: return 1
        for i in range(x+1):
            if i * i > x:
                return i-1
            print(i)
    # Binary Search
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
            print(mid)

        return right








solution = Solution()
x = 17
print(solution.mySqrt(x))
