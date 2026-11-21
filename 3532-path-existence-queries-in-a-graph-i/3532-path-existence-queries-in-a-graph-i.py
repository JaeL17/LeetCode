class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        answer: List[bool] = []

        components = [0] * n
        component_id = 0
        for i in range(1, n):
            if nums[i] - nums[i-1] > maxDiff:
                component_id +=1
            components[i] = component_id
        
        for u, v in queries:
            answer.append(components[u] ==components[v])
        return answer




        # component = [0] * n
        # comp_id = 0

        # for i in range(1, n):
        #     if nums[i] - nums[i - 1] > maxDiff:
        #         comp_id += 1
        #     component[i] = comp_id

        # answer = []
        # for u, v in queries:
        #     answer.append(component[u] == component[v])

        # return answer