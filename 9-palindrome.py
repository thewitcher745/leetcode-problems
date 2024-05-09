class Solution:
    def isPalindrome(self, x) -> bool:
        string_x = str(x)
        if len(string_x) == 1:
            return True
        elif len(string_x) == 2:
            if string_x[0] == string_x[1]:
                return True
            else:
                return False
        else:
            if string_x[0] == string_x[-1]:
                return self.isPalindrome(str(x)[1:-1])
            return False


solution = Solution()
print(solution.isPalindrome(1200021))
