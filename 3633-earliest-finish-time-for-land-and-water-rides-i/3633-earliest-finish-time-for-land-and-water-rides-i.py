from typing import List

class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int]
    ) -> int:
        
        answer = float("inf")

        def check_order(
            ride1_start: List[int],
            ride1_duration: List[int],
            ride2_start: List[int],
            ride2_duration: List[int]
        ) -> None:
            nonlocal answer

            for i in range(len(ride1_start)):
                ride1_end_time = ride1_start[i] + ride1_duration[i]

                for j in range(len(ride2_start)):
                    ride2_actual_start = max(ride1_end_time, ride2_start[j])
                    ride2_end_time = ride2_actual_start + ride2_duration[j]

                    answer = min(answer, ride2_end_time)

        check_order(landStartTime, landDuration, waterStartTime, waterDuration)
        check_order(waterStartTime, waterDuration, landStartTime, landDuration)

        return answer