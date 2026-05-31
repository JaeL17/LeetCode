from collections import defaultdict

class UndergroundSystem:

    def __init__(self):
        self.train_time_track: dict[str, List[int]] = defaultdict(list)
        self.customer_time_track: dict[int, Tuple[str, int]] = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customer_time_track[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        station_in, in_time = self.customer_time_track[id][0], self.customer_time_track[id][1]
        journey = f"{station_in}_to_{stationName}"
        self.train_time_track[journey].append(t - in_time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        journey = f"{startStation}_to_{endStation}"
        return sum(self.train_time_track[journey])/len(self.train_time_track[journey])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)