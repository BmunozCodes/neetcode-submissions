class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            if self.has_duplicates(board[r]):
                return False
        for c in range(9):
            column = [board[r][c] for r in range(9)]
            if self.has_duplicates(column):
                return False
        for box_row in range(3):
            for box_col in range(3):
                box = []
                for r in range(box_row*3, box_row * 3 +3):
                    for c in range(box_col*3, box_col *3+3):
                        box.append(board[r][c])
                if self.has_duplicates(box):
                    return False
        return True
    def has_duplicates(self, values):
        seen = set()
        for v in values:
            if v==".":
                continue
            if v in seen:
                return True
            seen.add(v)
        return False
        