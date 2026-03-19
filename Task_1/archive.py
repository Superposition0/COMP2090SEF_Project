#Import Area
import os
import sqlite3
import typer
import datetime
from rich import print, box
from rich.text import Text
from rich.table import Table
from pathlib import Path
from abc import ABC, abstractmethod

#Database connection
dir_path = Path(os.path.dirname(__file__))
root = dir_path / "animate_tracker.db"
conn = sqlite3.connect(root)
cur = conn.cursor()
res = cur.execute("SELECT name From sqlite_master")
e = res.fetchone() is None
if not(e):
    cur.excute("""UPDATE anime SET ViewStatus = "" """)
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

def action():
    action = typer.prompt("Enter Your Action (Change/Quit) ")
    action = action.strip()
    action = action.lower()
    if action == "change":
        ...
    elif action == "quit":
        typer.Exit()
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
        else:
            print("[yellow i]Render Error, Please Restart")


if __name__ == "__main__":
    archive().printTable()
    print(anime().name)
    anime().print()
    action()
    conn.close()

