import collections


class User:
    def __init__(self, id, check_in_station_name, check_in_time):
        self.id = id
        self.check_in_station_name = check_in_station_name
        self.check_in_time = check_in_time


class Station:
    def __init__(self, total_time=0, count=0):
        self.total_time = total_time
        self.count = count


class UndergroundSystem:
    def __init__(self):
        self.users = {}
        self.stations = collections.defaultdict(
            lambda: collections.defaultdict(Station))

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.users[id] = User(id, stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        user = self.users.pop(id)
        end_station = self.stations[user.check_in_station_name][stationName]
        end_station.count += 1
        end_station.total_time += t - user.check_in_time

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        end_station = self.stations[startStation][endStation]

        return end_station.total_time / end_station.count
