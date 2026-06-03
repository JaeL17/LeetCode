class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:

        min_land_finish = float("inf")

        for start, duration in zip(landStartTime, landDuration):
            min_land_finish = min(min_land_finish, start + duration)
        
        min_water_finish = float("inf")

        for start, duration in zip(waterStartTime, waterDuration):
            min_water_finish = min(min_water_finish, start + duration)

        answer = float("inf")

        # land ride -> water ride
        for start, duration in zip(waterStartTime, waterDuration):
            second_start = max(min_land_finish, start)
            answer = min(answer, second_start + duration)

        # water ride -> land ride
        for start, duration in zip(landStartTime, landDuration):
            second_start = max(min_water_finish, start)
            answer = min(answer, second_start + duration)

        return answer