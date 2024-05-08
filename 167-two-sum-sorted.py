class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left_counter, right_counter = 0, len(numbers) - 1

        while numbers[left_counter] + numbers[right_counter] != target:
            if numbers[left_counter] + numbers[right_counter] > target:
                right_counter -= 1
            else:
                left_counter += 1

        return [left_counter + 1, right_counter + 1]
