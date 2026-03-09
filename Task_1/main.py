#Import Area
import io
import os
import sys
import json
import typer
import datetime
from rich import print, box
from rich.text import Text
from rich.table import Table
from rich.layout import Layout
from typing import Annotated
from abc import ABC, abstractmethod
from archive import archive
#JSON file loader
try:
    json_skeleton = {"name": "",
        "startDate": "",
        "Time": "",
        "Cinema": "",
        "UpdateWeekDay": "",
        "UpdateTime": "",
        "EpisodeNumber": "",
        "ViewStatus": "",
        "Special": "",
        "ViewPlatform": "",
        "Ratings": "",
        "Notes": ""}
    if os.path.exists("anime_tracker.json"):
        with open("anime_tracker.json", "r+", encoding="utf-8-sig") as tracker_file: #TODO Proper read/write rights
            AnimeTrack = json.load(tracker_file)
    else:
        with open("anime_tracker.json", "w+", encoding="utf-8-sig") as tracker_file:
            json.dump(json_skeleton,tracker_file)
except IOError:
    sys.exit("Cannot open relative files!")
except ValueError:
    sys.exit("Decode error")

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

#WeeklyAnime sub-class
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

#After action received, redirect user to related module
def router():
        action = typer.prompt("Enter Your Action (Add/Update/List/Quit) ")
        action = action.strip()
        action = action.lower()
        if action == "add":
            ...
        elif action == "update":
            ...
        elif action == "list":
            archive()
        elif action == "quit":
            typer.Exit()
        else:
            print("Unsupported action, Please enter again.")
            return router()


def main():
    #Date getter and formatter
    currentDate = datetime.datetime.now()
    DisplayDate = currentDate.strftime("%d/%m/%Y, %A")
    WeekNum = currentDate.strftime("%w")
    welcomeMessage = Text(r''''
                                                                 ___
 \    / _  |  _  _  ._ _   _    _|_  _     /\  ._  o ._ _   _     | ._ _.  _ |   _  ._ |
  \/\/ (/_ | (_ (_) | | | (/_    |_ (_)   /--\ | | | | | | (/_    | | (_| (_ |< (/_ |  o
' ''')
    welcomeMessage.stylize("bold magenta")
    print(welcomeMessage)

    #Week view base template
    print(f"[green bold]Today is {DisplayDate}")
    table = Table(title="This Week Anime", box=box.ASCII2, safe_box=False, show_header=False, expand=True)

    tableSun = Table(box=box.SIMPLE, safe_box=False, expand=True, style="on steel_blue" if WeekNum=="0" else "")
    tableSun.add_column("Sunday", justify="center")

    tableMon = Table(box=box.SIMPLE, safe_box=False, expand=True, style="on steel_blue" if WeekNum=="1" else "")
    tableMon.add_column("Monday", justify="center")

    tableTue = Table(box=box.SIMPLE, safe_box=False, expand=True, style="on steel_blue" if WeekNum=="2" else "")
    tableTue.add_column("Tuesday", justify="center")

    tableWed = Table(box=box.SIMPLE, safe_box=False, expand=True, style="on steel_blue" if WeekNum=="3" else "")
    tableWed.add_column("Wednesday", justify="center")

    tableThu = Table(box=box.SIMPLE, safe_box=False, expand=True, style="on steel_blue" if WeekNum=="4" else "")
    tableThu.add_column("Thursday", justify="center")

    tableFri = Table(box=box.SIMPLE, safe_box=False, expand=True, style="on steel_blue" if WeekNum=="5" else "")
    tableFri.add_column("Friday", justify="center")

    tableSat = Table(box=box.SIMPLE, safe_box=False, expand=True, style="on steel_blue" if WeekNum=="6" else "")
    tableSat.add_column("Saturday", justify="center")

    for i in range(7):
        table.add_column()
    table.add_row(tableSun,tableMon,tableTue,tableWed,tableThu,tableFri,tableSat)

    if table.columns:
        print(table)
    else:
        print("[yellow i]Render Error, Please Restart")

    router()
    # print(os.path.exists("anime_tracker.json")) #TODO dev use:Delete



if __name__ == "__main__":
    typer.run(main)

