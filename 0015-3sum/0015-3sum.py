class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        answer = []
        nums.sort()
        hash_ = {}
        for i in range(len(nums)):
            left_idx = i+1
            right_idx = len(nums)-1
            
            while left_idx < right_idx: # and :
                sum_ = nums[i]+ nums[left_idx] + nums[right_idx]

                if sum_ == 0:
                    if str(nums[i]) + str(nums[left_idx]) + str(nums[right_idx]) not in hash_.keys():                
                        answer.append([nums[i], nums[left_idx], nums[right_idx]])
                        hash_[str(nums[i]) + str(nums[left_idx]) + str(nums[right_idx])] = ""
                    left_idx = left_idx +1
                    right_idx = right_idx - 1
                elif sum_ < 0:
                    left_idx = left_idx+1
                else:
                    right_idx = right_idx - 1
                # if nums[left_idx] == nums[right_idx]:
                #     break


            # for j in range(i+1, len(nums)):
            #     for k in range(j+1, len(nums)):
            #         if nums[i] + nums[j] + nums[k] == 0 and i != j and k != j and k != i:
            #             if str(nums[i]) + str(nums[j]) + str(nums[k]) not in hash_.keys():                
            #                 answer.append([nums[i], nums[j], nums[k]])
            #                 hash_[str(nums[i]) + str(nums[j]) + str(nums[k])] = ""

        # answer = list(set(answer))
        return answer


        