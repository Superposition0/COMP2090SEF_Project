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

try:
    json_skeleton = {"name": "",
        "startDate": "",
        "Time": "",
        "Cinema": "",
        "UpdateWeekDay": "",
        "UpdateTime": "",
        "EpisodeNumber": "",
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

table = Table(title="Archived Anime", box=box.ASCII2, safe_box=False, expand=True)
table.add_column()
