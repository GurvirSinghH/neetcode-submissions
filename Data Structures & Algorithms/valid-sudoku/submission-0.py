class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        for i in range(0, n):
            hs = set()
            for j in board[i]:
                if j in hs and j != ".":
                    return False
                if j != ".":
                    hs.add(j)       
        boxes = [set() for _ in range(9)]
        for col in range(n):
            seen = set()
            for row in range(n):
                cell = board[row][col]
                cRow = row // 3
                cCol = col // 3
                box = 3*cRow+cCol
                if cell in seen and cell != ".":
                    return False
                if cell in boxes[box] and cell != ".":
                    return False
                if cell != ".":
                    seen.add(cell)
                    boxes[box].add(cell)           
        return True