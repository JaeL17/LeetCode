class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # 1. sort array in ascending order.
        # 2. subtract arr[i+1] - arr[i]
        arr.sort() # O(nlogn) python sort
        n = len(arr) # O(1) length of list
        diff_lst = []
        answer = []
        for i in range(n-1): # O(n-1) -> O(n) time complexity for iterating the loop
            # 0 ~ n-1
            diff = arr[i+1] - arr[i]
            diff_lst.append((diff,[arr[i], arr[i+1]])) # O(n-1) -> O(n) space complexity for saving intermediate values
        min_diff = min(diff_lst) # time complexity for finding min of List[int, List[int, int]]
        # print(min_diff)
        for j in range(len(diff_lst)): # O(n-1) -> O(n) time complexity for iterating the loop
            if diff_lst[j][0] == min_diff[0]:
                answer.append(diff_lst[j][1])
        return answer



        