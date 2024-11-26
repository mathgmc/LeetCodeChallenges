# https://leetcode.com/problems/valid-sudoku/?envType=study-plan-v2&envId=top-interview-150
from typing import List
from collections import defaultdict


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
    

class Solution1:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or board[r][c] in cols[c] 
                or board[r][c] in squares[(r // 3,c // 3)]):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True