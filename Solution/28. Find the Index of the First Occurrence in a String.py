class Solution(object):

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if not needle:
            return 0

        len_haystack, len_needle = len(haystack), len(needle)

        for i in range(len_haystack - len_needle + 1):
            if haystack[i:i + len_needle] == needle:
                return i

        return -1



solution = Solution()
haystack = "mississippi"
needle = "issip"
print(solution.strStr(haystack, needle))
