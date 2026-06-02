class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        time_list: List[int] = []

        def find_time(ride1_start: List[int], duration1: List[int], ride2_start: List[int], duration2: List[int]) -> None:

            for i, start_time1 in enumerate(ride1_start):
                ride1_duration = duration1[i]
                ride1_end_time = start_time1 + ride1_duration

                for j, start_time2 in enumerate(ride2_start):
                    if start_time2 <= ride1_end_time:
                        ride2_end_time = ride1_end_time + duration2[j]
                    else:
                        ride2_end_time = start_time2 + duration2[j]
                    time_list.append(ride2_end_time)

        # land -> water
        find_time(landStartTime, landDuration, waterStartTime, waterDuration)

        # land -> water
        find_time(waterStartTime, waterDuration, landStartTime, landDuration)

        return min(time_list)
