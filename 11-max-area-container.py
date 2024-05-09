class Solution:
    def maxArea(self, height: list[int]) -> int:
        l_pointer, r_pointer = 0, len(height) - 1
        max_area = 0
        while l_pointer != r_pointer:
            if height[l_pointer] <= height[r_pointer]:
                max_area = max(height[l_pointer] * (r_pointer - l_pointer), max_area)
                l_pointer += 1
            else:
                max_area = max(height[r_pointer] * (r_pointer - l_pointer), max_area)
                r_pointer -= 1
        return max_area


solution = Solution()
print(solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
