class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # Creating a set to store the characters in the current window
        window = set()

        # Initializing the maximum length of the substring to 0
        max_len = 0

        # Initializing the left and right pointers for the sliding window
        left, right = 0, 0

        while right < len(s):
            # If the current character is not in the window, add it to the window
            if s[right] not in window:
                window.add(s[right])
                right += 1
                max_len = max(max_len, len(window))
            # If the current character is in the window, remove characters from the left side until the duplicate character is removed
            else:
                window.remove(s[left])
                left += 1

        return max_len


solution = Solution()
print(solution.lengthOfLongestSubstring("abcodaffodaaqoewrogvboxcvo ;ajeobnrofgiubnoaV:oo"))
