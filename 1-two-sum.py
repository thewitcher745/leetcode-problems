# More systematic and clean
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        indexed_nums = sorted(list(enumerate(nums)), key=lambda x: x[1])
        indices = [x[0] for x in indexed_nums]
        counter_1, counter_2 = 0, len(nums) - 1

        while counter_2 >= counter_1:
            if indexed_nums[counter_1][1] + indexed_nums[counter_2][1] > target:
                counter_2 -= 1
            elif indexed_nums[counter_1][1] + indexed_nums[counter_2][1] < target:
                counter_1 += 1
            else:
                return [indices[counter_1], indices[counter_2]]


# Completely iterative and brute force
class Solution2:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for num1_ind in range(len(nums)):
            for num2_ind in range(len(nums)):
                if num1_ind != num2_ind:
                    if nums[num1_ind] + nums[num2_ind] == target:
                        return [num1_ind, num2_ind]


# Iterative, but uses caching
class Solution3:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for idx, value in enumerate(nums):
            needed_sum = target - value;

            if needed_sum in seen:
                return [idx, seen[needed_sum]]

            seen[value] = idx