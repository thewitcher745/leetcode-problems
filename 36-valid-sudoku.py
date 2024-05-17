from typing import List


class Solution:
    def check_repeats(self, check_list):
        check_list = [list_item for list_item in check_list if list_item != "."]

        if len(set(check_list)) != len(check_list):
            return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check_lists = []
        # Check rows
        check_lists = [board[i][:] for i in range(9)]
        # Add columns
        check_lists += [[board[i][j] for i in range(9)] for j in range(9)]
        # Add boxes
        for column_box_counter in range(3):
            for row_box_counter in range(3):
                check_lists += [[item for row in [[board[j][i] for i in range(column_box_counter * 3, column_box_counter * 3 + 3)] for j in
                                                  range(row_box_counter * 3, row_box_counter * 3 + 3)]
                                 for item in row]]

        if all([self.check_repeats(check_lists[i]) for i in range(27)]):
            return True
        return False


solution = Solution()
board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
print(solution.isValidSudoku(board))
