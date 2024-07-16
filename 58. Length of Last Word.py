class Solution(object):

    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        count = 0

        for i in range(len(s)):
            if s[len(s)-i-1] != " ":
                count += 1
                if s[len(s)-i-2] == " ":
                    return count
        return count



solution = Solution()
s = "Hello World"
print(solution.lengthOfLastWord(s))
