class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        flat_matrix = []
        for row in matrix:
            flat_matrix.extend(row)
        
        left = 0
        right = rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            if flat_matrix[mid] == target:
                return True
            if flat_matrix[mid] < target:
                left = mid +1
            else:
                right = mid - 1


        return False

        