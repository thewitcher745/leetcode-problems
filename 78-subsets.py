from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        x = self.subsets(nums[1:])
        return x + [[nums[0]] + y for y in x]


solution = Solution()
print(solution.subsets([1, 2, 3]))
