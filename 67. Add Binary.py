class Solution(object):

    # 我寫的
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        g = 0

        if len(a) - len(b) > 0:
            b = "0"*(len(a) - len(b)) + b
        else:
            a = "0" * (len(b) - len(a)) + a

        result = []
        for i in range(len(a)-1, -1, -1):
            if int(a[i]) + int(b[i]) + g < 2:
                result.append(str(int(a[i]) + int(b[i]) + g))
                g = 0
            else:
                result.append(str((int(a[i]) + int(b[i]) + g) % 2))
                g = 1
        if g == 1:
            result.append(str(1))

        return ''.join(result[::-1])


    # ChatGPT
    def addBinary(self, a, b):
        carry = 0

        if len(a) > len(b):
            b = "0" * (len(a) - len(b)) + b
        else:
            a = "0" * (len(b) - len(a)) + a

        result = []
        for i in range(len(a) - 1, -1, -1):
            total = int(a[i]) + int(b[i]) + carry
            carry = total // 2  # 計算進位
            result.append(str(total % 2))  # 計算當前位

        if carry == 1:
            result.append(str(1))

        return ''.join(result[::-1])




solution = Solution()
a = "1"
b = "11"
print(solution.addBinary(a,b))
