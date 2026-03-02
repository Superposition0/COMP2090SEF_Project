import json
import typer
from rich import print
from abc import ABC, abstractmethod
#anime class
'''
Name: Anime Name
StartDate: Start airing date of the anime, should be input following DD/MM/YYYY
UpdateWeekDay: When anime update per week, should be input as full name e.g. "Monday" or 1
UpdateTime: The time anime update, should be input as HH:MM format, JST/HKT support, show on HKT by default
EpisodeNumber: Total number of episode of anime, should be input in integer
Special: Special arrangement, e.g. pause airing for a week
ViewPlatform: Viewing Platform, e.g. Netflix, Youtube
'''
class anime(ABC):
    def __init__(self, name: str, StartDate: str):
        self.name = name
        self.startDate = StartDate

    def name_get(self):
        return self.name

    def name_set(self, name):
        self.name = name
        return "Name updated successfully"

    def StartDate_get(self):
        return self.startDate

    def StartDate_set(self, date):
        self.startDate = date
        return "Start date updated successfully"

    @abstractmethod
    def time_get(self):
        ...

    @abstractmethod
    def time_set(self, time):
        ...

    @abstractmethod
    def ViewMethod_get(self):
        ...

    @abstractmethod
    def ViewMethod_set(self, method):
        ...

class MovieVer(anime):
    def __init__(self, name, StartDate, Time, Cinema):
        super().__init__(name, StartDate)
        self.Time = Time
        self.Cinema = Cinema

    def time_get(self):
        return self.Time

    def time_set(self, time):
        self.Time = time

    def ViewMethod_get(self):
        return self.Cinema

    def ViewMethod_set(self, method):
        self.Cinema = method

class WeeklyAnime(anime):
    def __init__(self, name, StartDate, UpdateWeekDay, UpdateTime, EpisodeNumber, Special, ViewPlatform):
        super().__init__(name, StartDate)
        self.UpdateWeekDay = UpdateWeekDay
        self.UpdateTime = UpdateTime
        self.EpisodeNumber = EpisodeNumber
        self.Special = Special
        self.ViewPlatform = ViewPlatform


def main():
    print("Hello, world!")

if __name__ == "__main__":
    typer.run(main)
