class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [[] for _ in range(3)]

        for n in nums:
            buckets[n].append(n)

        nums.clear()
        nums.extend([n for sublist in buckets for n in sublist])
