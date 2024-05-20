from typing import List


class Solution:
    def subsets(self, nums):
        if not nums:
            return [[]]
        x = self.subsets(nums[1:])
        return x + [[nums[0]] + y for y in x]

    def subsetXORSum(self, nums: List[int]) -> int:
        sum_of_xors = 0
        for subset in self.subsets(nums):
            xor_result = 0
            for num in subset:
                xor_result = xor_result ^ num
            sum_of_xors += xor_result

        return sum_of_xors


solution = Solution()
print(solution.subsetXORSum([5, 1, 6]))
