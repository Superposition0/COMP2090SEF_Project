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

<<<<<<< Updated upstream
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
=======
#Database connection
dir_path = Path(os.path.dirname(__file__))
root = dir_path / "animate_tracker.db"
conn = sqlite3.connect(root)
cur = conn.cursor()
res = cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='anime'")
e = res.fetchone() is None
if not(e):
    cur.execute("""UPDATE anime SET ViewStatus = "" WHERE ViewStatus IS NULL""")
else:
    cur.execute("""CREATE TABLE anime(
                Name TEXT PRIMARY KEY,
                StartDate TEXT,
                Time TEXT,
                Cinema TEXT,
                UpdateWeekDay INTEGER,
                UpdateTime TEXT,
                EpisodeNumber INTEGER,
                ViewStatus TEXT,
                Special TEXT,
                ViewPlatform TEXT,
                Ratings INTEGER,
                Notes TEXT
                )""")
conn.commit()
>>>>>>> Stashed changes

def action():
    action = typer.prompt("Enter Your Action (Change/Quit) ")
    action = action.strip()
    action = action.lower()
    if action == "change":
        print("[yellow]Change mode activated...[/yellow]")
    elif action == "quit":
        typer.Exit()
<<<<<<< Updated upstream

class archive():
    def __init__(self):
        table = Table(title="Archived Anime", box=box.ASCII2, safe_box=False, expand=True)
        table.add_column("No.")
        table.add_column("Name")
        table.add_column("Episode Number")
        table.add_column("View Status")
        table.add_column("Ratings")
        table.add_column("Notes")

        if table.columns:
            print(table)
=======

class anime():
    def __init__(self):
        cur.execute("""SELECT name, ViewStatus, Ratings, Notes FROM anime WHERE ViewStatus = "" """)
        self.output = cur.fetchall()
        self.name = [item[0] for item in self.output]
        self.ViewStatus = [item[1] for item in self.output]
    def paramBind(self):
        pass


    def print(self):
        print(self.output)

class archive():
    def __init__(self):
        self.table = Table(title="Archived Anime", box=box.ASCII2, safe_box=False, expand=True)
        self.table.add_column("No.")
        self.table.add_column("Name")
        self.table.add_column("View Status")
        self.table.add_column("Ratings")
        self.table.add_column("Notes")
        
    def printTable(self):
        if self.table.columns:
            print(self.table)
>>>>>>> Stashed changes
        else:
            print("[yellow i]Render Error, Please Restart")
        action()

if __name__ == "__main__":
    archive_list = archive()

