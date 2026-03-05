import io
import os
import json
import typer
from rich import print
from abc import ABC, abstractmethod

with open("anime_tracker.json" "w+") as tracker_file:
    tracker = json.load(tracker_file)
#anime class
'''
Name: Anime Name
StartDate: Start airing date of the anime, should be input following DD/MM/YYYY

'''
class anime(ABC):
    def __init__(self, name, StartDate):
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
    def time_set(self, time)->str:
        ...

    @abstractmethod
    def ViewMethod_get(self):
        ...

    @abstractmethod
    def ViewMethod_set(self, method)->str:
        ...

#MovieVer sub-class
'''
Time: Decided watch time; should be input as HH:MM
Cinema: Decided watch cinema
'''
class MovieVer(anime):
    def __init__(self, name, StartDate, Time, Cinema):
        super().__init__(name, StartDate)
        self.Time = Time
        self.Cinema = Cinema

    def time_get(self):
        return self.Time

    def time_set(self, time):
        self.Time = time
        return "Time updated successfully"

    def ViewMethod_get(self):
        return self.Cinema

    def ViewMethod_set(self, method):
        self.Cinema = method
        return "Cinema updated successfully"

#WeeklyAnime
'''
UpdateWeekDay: The week day that the anime updated; can be input as full form e.g."Monday" or short form e.g. "1"
UpdateTime: The time that the anime updated; should be input as HH:MM
EpisodeNumber: Total EpisodeNumber of the anime
Special: Special airing arrangement
ViewPlatform: Platform to watch the anime
'''
class WeeklyAnime(anime):
    def __init__(self, name, StartDate, UpdateWeekDay, UpdateTime, EpisodeNumber, Special, ViewPlatform):
        super().__init__(name, StartDate)
        self.UpdateWeekDay = UpdateWeekDay
        self.UpdateTime = UpdateTime
        self.EpisodeNumber = EpisodeNumber
        self.Special = Special
        self.ViewPlatform = ViewPlatform

    def UpdateWeekDay_get(self):
        return self.UpdateWeekDay
    def UpdateWeekDay_set(self, weekday):
        self.UpdateWeekDay = weekday
    def time_get(self):
        return self.UpdateTime
    def time_set(self, time):
        self.UpdateTime = time
        return "UpdateTime updated successfully"
    def EpisodeNumber_get(self):
        return self.EpisodeNumber
    def EpisodeNumber_set(self, episodenumber):
        self.EpisodeNumber = episodenumber
    def Special_get(self):
        return self.Special
    def Special_set(self, special):
        self.Special = special
    def ViewMethod_get(self):
        return self.ViewPlatform
    def ViewMethod_set(self, method):
        self.ViewPlatform = method
        return "ViewPlatform updated successfully"



def main():
    print("Hello, world!")

if __name__ == "__main__":
    typer.run(main)
