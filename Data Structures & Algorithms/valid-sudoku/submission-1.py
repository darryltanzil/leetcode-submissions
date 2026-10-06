from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        row, col, diagnol check
        3 sets, if its seen we add it to the row
        for squares, need second check
        """
        seenRow = defaultdict(set)
        seenCol = defaultdict(set)
        seenBox = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seenBox[(i//3,j//3)]:
                    return False
                seenBox[(i//3,j//3)].add(board[i][j])
                if board[i][j] in seenRow[i]:
                    return False
                seenRow[i].add(board[i][j])
                if board[i][j] in seenCol[j]:
                    return False
                seenCol[j].add(board[i][j])

        return True

