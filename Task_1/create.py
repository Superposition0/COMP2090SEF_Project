import typer
import sqlite3
import os
import datetime
from rich.console import Console
from pathlib import Path

console = Console()
app = typer.Typer()

# Setup database path
dir_path = Path(os.path.dirname(__file__))
root = dir_path / "animate_tracker.db"
conn = sqlite3.connect(root)
cur = conn.cursor()

class Anime:
    def __init__(self, name, StartDate, view_status="", ratings="", notes=""):
        self.name = name
        self.StartDate = StartDate
        self.view_status = view_status
        self.ratings = ratings
        self.notes = notes

class WeeklyAnime(Anime):
    def __init__(self, name, StartDate, UpdateWeekDay, UpdateTime, EpisodeNumber, Special, ViewPlatform, **kwargs):
        super().__init__(name, StartDate, **kwargs)
        self.UpdateWeekDay = UpdateWeekDay
        self.UpdateTime = UpdateTime
        self.EpisodeNumber = EpisodeNumber
        self.Special = Special
        self.ViewPlatform = ViewPlatform

class AnimeMovie(Anime):
    def __init__(self, name, StartDate, ScreenTime, Cinema, **kwargs):
        super().__init__(name, StartDate, **kwargs)
        self.ScreenTime = ScreenTime
        self.Cinema = Cinema

def save_to_sqlite(obj):
    if isinstance(obj, WeeklyAnime):
        data = (
            obj.name, obj.StartDate, "", "", obj.UpdateWeekDay,
            obj.UpdateTime, obj.EpisodeNumber, obj.view_status,
            obj.Special, obj.ViewPlatform, obj.ratings, obj.notes
        )
    elif isinstance(obj, AnimeMovie):
        toBeProcessed = datetime.datetime.strptime(obj.StartDate, "%d/%m/%Y")
        processed = toBeProcessed.strftime("%w")
        data = (
            obj.name, obj.StartDate, obj.ScreenTime, obj.Cinema, processed,
            "", "", obj.view_status, "", "",
            obj.ratings, obj.notes
        )

    # Use REPLACE to handle updates to existing names
    cur.execute("INSERT OR REPLACE INTO anime VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
    conn.commit()

@app.command()
def create_entry():
    console.print("[bold cyan]Add New Entry[/bold cyan]")
    is_movie = typer.confirm("Is this a movie?")

    name = typer.prompt("1. Name")
    start_date = typer.prompt("2. Start date (DD/MM/YYYY)")

    if not is_movie:
        weekday = typer.prompt("3. Update weekday (0=Sun, 1=Mon, etc.)", type=int)
        u_time = typer.prompt("4. Update time (HH:MM)")
        eps = typer.prompt("5. Episode number", type=int)
        platform = typer.prompt("6. View platform")
        new_obj = WeeklyAnime(name, start_date, weekday, u_time, eps, "", platform)
    else:
        u_time = typer.prompt("3. Screening time (HH:MM)")
        cinema = typer.prompt("4. Cinema location")
        new_obj = AnimeMovie(name, start_date, u_time, cinema)

    save_to_sqlite(new_obj)
    console.print(f"\n[bold green]Successfully saved: {name}![/bold green]")

if __name__ == "__main__":
    try:
        app()
    finally:
        conn.close()
