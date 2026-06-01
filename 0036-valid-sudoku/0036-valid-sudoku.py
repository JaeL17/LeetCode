class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def remove_empty_cell(lst: List[str]) -> List[str]:
            return [item for item in lst if item.isdigit()]
        
        # check row & col rule
        for i in range(9):
            row = board[i]
            row = remove_empty_cell(row) # [j for j in row if j != "."]
            col = [board[j][i] for j in range(9) if board[j][i] != "."]

            if len(row) != len(set(row)) or len(col) != len(set(col)):
                return False

            if i % 3 == 0:
                sub_box1 = board[i][: 3] + board[i + 1][: 3] + board[i + 2][: 3]
                sub_box1 = remove_empty_cell(sub_box1)  #sub_box1 = [j for j in sub_box1 if j != "."]

                sub_box2 = board[i][3: 6] + board[i + 1][3: 6] + board[i + 2][3: 6]
                sub_box2 = remove_empty_cell(sub_box2)  # sub_box2 = [j for j in sub_box2 if j != "."]

                sub_box3 = board[i][6: ] + board[i + 1][6: ] + board[i + 2][6: ]
                sub_box3 = remove_empty_cell(sub_box3) 
                # sub_box3 = [j for j in sub_box3 if j != "."]

                if len(sub_box1) != len(set(sub_box1)) or len(sub_box2) != len(set(sub_box2)) or len(sub_box3) != len(set(sub_box3)):
                    return False

        return True
        