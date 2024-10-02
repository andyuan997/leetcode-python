class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()  # 用來儲存已出現過的數字，避免無限循環
        while n != 1 and n not in seen:
            seen.add(n)  # 將當前數字加入集合
            n = sum(int(digit) ** 2 for digit in str(n))  # 計算每個位數的平方和
        return n == 1  # 如果 n 最終變成 1，則返回 True，否則返回 False
