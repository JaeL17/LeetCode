class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = 0
        left = 0
        curr_sum =0
        count = {}

        # time complexity O(n), space complexity O(k)
        for right in range(len(nums)):

            # update curr_sum
            curr_sum += nums[right]
            
            # update counter
            if nums[right] in count:
                count[nums[right]] +=1
            else:
                count[nums[right]] = 1

            # move left index if the subarray size is greater than k    
            if right - left + 1 > k:
                curr_sum -= nums[left] # update current sum
                count[nums[left]] -=1 # update counter
                if count[nums[left]] == 0: # if there is no nums[left] element in counter, remove it
                    del count[nums[left]]
                left +=1
            
            # if subarray size == k and the elements are dinstinct
            if right - left + 1 == k and len(count) == k:
                max_sum = max(max_sum, curr_sum)


        return max_sum