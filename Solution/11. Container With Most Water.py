"""
「Medium」題目來源：blind-75-leetcode-questions

11. Container With Most Water
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""
"""
想到的解法 
1. 暴力解 O(n^2)
2. 雙指針 O(n)
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # 計算容器面積
            area = min(height[left], height[right]) * (right - left)
            if area > max_area:
                max_area = area

            # 移動指標，要移動小的，因為只有移動小的那邊才有可能增加容積
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area







height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
output = 49

solution = Solution()
print(solution.maxArea(height))