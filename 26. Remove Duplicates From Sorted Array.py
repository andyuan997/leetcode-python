class Solution(object):


    # 使用stack 效率太低
    def removeDuplicates_x(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = []
        counter = 0

        for num in nums:
            if num in stack:
                #stack.pop()
                counter += 1
            else:
                stack.append(num)

            print(counter)
            print(stack)
        for i in range(len(stack)):
            nums[i] = stack[i]

        return len(nums) - counter


    # 我自己寫的方法
    def removeDuplicates_x(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = nums[0]
        counter = 0

        for num in nums:
            if num >= n:
                nums[counter] = num
                n = num + 1
                counter += 1
        print(nums)

        return counter

    # 更優解
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            if nums[count] != nums[i]:
                count += 1
                nums[count] = nums[i]
        #print(nums)

        return count + 1







solution = Solution()
nums = [1,1,2]
print(solution.removeDuplicates(nums))
