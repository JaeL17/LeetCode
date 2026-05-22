class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        # O (nlogn)
        nums.sort()
        answer = []

        n = len(nums)

        # O(n^2)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[right] + nums[left]
                if total == 0:
                    answer.append([nums[i], nums[right], nums[left]])

                    while left < right and nums[left] == nums[left + 1]:
                        left +=1

                    while left < right and nums[right] == nums[right -1]:
                        right -=1

                    left +=1
                    right -=1
                elif total < 0:
                    left +=1
                else:
                    right -=1

        return answer