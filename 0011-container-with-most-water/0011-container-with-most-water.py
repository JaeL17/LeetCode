class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        n = len(height)
        # area = diff(i, j) index * min(height[i], height[j])

        left = 0
        right = n - 1
        while left < right:
            max_water = max_water = max((right - left) * min(height[right], height[left]), max_water) 

            if height[left] < height[right]:
                left +=1
            else:
                right -=1
        return max_water


        # O (n^2)
        # for i in range(len(height) - 1):
        #     for j in range(i + 1, len(height)):
        #         max_water = max((j - i) * min(height[i], height[j]), max_water)


        # return max_water