import collections

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Create dictionaries where the default value is an empty set
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set) # Key will be a tuple: (r // 3, c // 3)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                if val == '.':
                    continue
                
                # The coordinate of the 3x3 box this cell belongs to
                box_coord = (r // 3, c // 3)

                # Check if we have already seen this number in the current row, col, or box
                if val in rows[r] or val in cols[c] or val in boxes[box_coord]:
                    return False
                
                # Add the number to our tracking sets
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_coord].add(val)
                
        return True