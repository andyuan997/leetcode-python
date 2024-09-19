class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 計數數組，用於計算每個數字出現的次數
        count = [0] * 101

        # 統計每個數字出現的次數
        for num in nums:
            count[num] += 1

        # 累積計數，用於計算有多少個數小於當前數
        for i in range(1, 101):
            count[i] += count[i - 1]

        # 對每個數字返回有多少數小於它
        result = []
        for num in nums:
            if num == 0:
                result.append(0)
            else:
                result.append(count[num - 1])

        return result
