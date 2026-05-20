from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting_colour = image[sr][sc]
        moves = [(-1,0), (1,0), (0, -1), (0, 1)] # up down left right
        if starting_colour == color:
            return image

        queue = deque([(sr, sc)])
        image[sr][sc] = color

        while len(queue) > 0:
            curr_row, curr_col = queue.popleft()
            
            # check whether the colour of matches with the starting colour.
            for move in moves:
                new_row, new_col = curr_row + move[0], curr_col + move[1]
                
                # check whether new values are within correct index range
                if 0<= new_row < len(image) and 0<= new_col < len(image[0]):
                    if image[new_row][new_col] == starting_colour:
                        image[new_row][new_col] = color

                        queue.append((new_row, new_col))
                    # visited[new_row][new_col] = True
        return image
                    
                    
        
