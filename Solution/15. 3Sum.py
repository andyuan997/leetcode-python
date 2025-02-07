"""
「Medium」題目來源：blind-75-leetcode-questions

15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""
"""
思考：
暴力解O(n^3)
三個指針？ -> 外層迴圈 內層雙指標 O(n^2)

"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """output = []
        n = len(nums)
        # 暴力解
        for x in range(n - 2):
            for y in range(x + 1, n - 1):
                for z in range(y + 1, n):
                    if nums[x] + nums[y] + nums[z] == 0:
                        # 排序這個三元組以便去除重複
                        triplet = sorted([nums[x], nums[y], nums[z]])
                        if triplet not in output:
                            output.append(triplet)
        return output"""


        output = []
        nums = sorted(nums)

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # 跳過重複值
            a = nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum == -a:
                    output.append([a, nums[left], nums[right]])
                    # 移動左指標並跳過重複值
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif current_sum < -a:
                    left += 1
                else:
                    right -= 1

            i += 1

        return output




nums = [-1, 0, 1, 2, -1, -4]

[-4, -1, -1, 0, 1, 2]

solution = Solution()
print(solution.threeSum(nums))
