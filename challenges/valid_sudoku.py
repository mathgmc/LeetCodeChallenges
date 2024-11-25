# https://leetcode.com/problems/valid-sudoku/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:     
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        control = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue

                subBox = f"{i // 3}{j // 3}"
                if board[i][j] in control.get(f"line{i}", []) or board[i][j] in control.get(f"column{j}", []) or board[i][j] in control.get(subBox, []):
                    return False

                control[f"line{i}"] = control.get(f"line{i}", []) + [board[i][j]] 
                control[f"column{j}"] = control.get(f"column{j}", []) + [board[i][j]] 
                control[subBox] = control.get(subBox, []) + [board[i][j]] 
                
        return True