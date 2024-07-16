class Solution(object):

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        for i in range(len(nums)):
            if nums[0] > target:
                return 0
            if nums[len(nums)-1] < target:
                return len(nums)
            if nums[i] == target:
                return i
            if nums[i] < target and nums[i+1] > target:
                return i + 1

solution = Solution()
nums = [1,3,5,6]
target = 7
print(solution.searchInsert(nums, target))
