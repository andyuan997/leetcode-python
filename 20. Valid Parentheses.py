class Solution(object):

    # 理解錯誤
    def isValid_x(self, s):
        """
        :type s: str
        :rtype: bool
        ()[]{}
        """
        while True:
            if s.find("(") != -1 and s.find("(") == s.find(")")-1 :
                s = s[:s.find("(")] + s[s.find(")")+1:]

            elif s.find("[") != -1 and s.find("[") == s.find("]")-1 :
                s = s[:s.find("[")] + s[s.find("]")+1:]

            elif s.find("{") != -1 and s.find("{") == s.find("}")-1 :
                s = s[:s.find("{")] + s[s.find("}")+1:]

            elif s != "":
                return False

            elif s == "":
                return True

    # 嘗試用stack做()的
    def isValid_x(self, s):
        """
        :type s: str
        :rtype: bool
        ()[]{}
        """
        stack = []

        for char in s:
            if char == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
            #return True
            print(stack)
        if stack:
            return False
        else:
            return True

    # 再加入map 變成()[]{}的
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        ()[]{}
        """
        stack = []
        map = {")" : "(", "]" : "[", "}" : "{"}

        for char in s:
            if char in map:
                if stack and stack[-1] == map[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
            print(stack)
        if stack:
            return False
        else:
            return True

solution = Solution()

print(solution.isValid("()[]["))
