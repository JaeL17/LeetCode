class Solution:
    def convert(self, s: str, numRows: int) -> str:
        save_lst = [[] for _ in range(numRows)]
        row_count = 0
        diag_count = numRows-2
        if numRows ==1:
            return s
        #print(s, numRows)
        for char in s:
            #print(char, save_lst, row_count, diag_count)
            if row_count < numRows:
                save_lst[row_count].append(char)
                row_count +=1
            elif diag_count != 0:
                save_lst[diag_count].append(char)
                diag_count -=1
            else: # initialise counts
                #row_count = 0
                save_lst[0].append(char)
                row_count = 1
                diag_count = numRows-2

        save_lst = [''.join(i) for i in save_lst]
        return ''.join(save_lst)

        