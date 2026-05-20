# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:

#         def find_first():
#             left = 0
#             right = len(nums) - 1
#             answer = -1

#             while left <= right:
#                 mid = (left + right) // 2

#                 if nums[mid] == target:
#                     answer = mid
#                     right = mid - 1
#                 elif nums[mid] < target:
#                     left = mid + 1
#                 else:
#                     right = mid - 1

#             return answer

#         def find_last():
#             left = 0
#             right = len(nums) - 1
#             answer = -1

#             while left <= right:
#                 mid = (left + right) // 2

#                 if nums[mid] == target:
#                     answer = mid
#                     left = mid + 1
#                 elif nums[mid] < target:
#                     left = mid + 1
#                 else:
#                     right = mid - 1

#             return answer

#         return [find_first(), find_last()]

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
     
        answer = [-1, -1]
        left = 0
        right = len(nums) -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                temp_left = mid
                temp_right = mid
                while nums[temp_left] == target:
                    answer[0] = temp_left
                    if temp_left > 0: 
                        temp_left -= 1
                    else:
                        break
                    
                while nums[temp_right] == target:
                    answer[1] = temp_right
                    if temp_right < len(nums) - 1: 
                        temp_right +=1
                    else:
                        break
                    
                return answer
            if nums[mid] < target:
                left = mid + 1
            if nums[mid] > target:
                right = mid - 1


        return answer