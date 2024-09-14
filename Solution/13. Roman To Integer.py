class Solution(object):
    
    # 映射+判斷前後字串大小
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int

        I = 1
        V = 5 判定前後有無I
        X = 10 判定前後有無I
        L = 50 判定前後有無X
        C = 100 判定前後有無X
        D = 500 判定前後有無C
        M = 1000 判定前後有無C
        """
        number = 0
        dic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        last_value = 0

        for char in s[::-1]:
            current_value = dic[char]
            if current_value < last_value:
                number -= current_value
            elif current_value >= last_value:
                number += current_value
            last_value = current_value

        return number
