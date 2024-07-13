class Solution(object):

    # 暴力方法 runtime error
    def maximumGain_x(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        score = 0
        if x > y:
            high = "ab"
            low = "ba"
            n = x
            m = y
        else:
            high = "ba"
            low = "ab"
            n = y
            m = x
        while True:
            while True:
                score += s.count(high) * n
                s = s.replace(high, "")
                if s.count(high) == 0:
                    break
            score += s.count(low) * m
            s = s.replace(low, "")
            if s.count(high) or s.count(low) == 0:
                return score
            
    # 使用stack方法
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """

        def calculate_max_score(s, first_pair, first_score, second_pair, second_score):
            stack = []
            score = 0
            for char in s:
                if stack and stack[-1] + char == first_pair:
                    stack.pop()
                    score += first_score
                else:
                    stack.append(char)

            new_stack = []
            for char in stack:
                if new_stack and new_stack[-1] + char == second_pair:
                    new_stack.pop()
                    score += second_score
                else:
                    new_stack.append(char)
            return score

        if x > y:
            return calculate_max_score(s, "ab", x, "ba", y)
        else:
            return calculate_max_score(s, "ba", y, "ab", x)


solution = Solution()

print(solution.maximumGain("cdbcbbaaabab", x = 4, y = 5))
