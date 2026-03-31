import typer
import sqlite3
<<<<<<< Updated upstream
=======
import os
>>>>>>> Stashed changes
from rich.console import Console

console = Console()
app = typer.Typer()

class anime:
    def __init__(self, name, StartDate):
        self.name = name
        self.StartDate = StartDate

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

<<<<<<< Updated upstream
=======
class AnimeMovie(anime): 
    def __init__(self, name, StartDate, ScreenTime, Cinema, ViewPlatform): 
        super().__init__(name, StartDate) 
        self.ScreenTime = ScreenTime 
        self.Cinema = Cinema 
        self.ViewPlatform = ViewPlatform 

>>>>>>> Stashed changes
#Create sqllite
DB_NAME = "anime_tracker.db"

def save_to_sqlite(obj):
    """Takes a WeeklyAnime object and saves it to the database"""
<<<<<<< Updated upstream
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
=======
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
>>>>>>> Stashed changes
    
    # Create table if it not here
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS anime_list (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            start_date TEXT,
            weekday TEXT,
            time TEXT,
            episodes TEXT,
            special TEXT,
            platform TEXT
        )
    """)
    
    # Insert data
<<<<<<< Updated upstream
    cursor.execute("""
        INSERT INTO anime_list (name, start_date, weekday, time, episodes, special, platform)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (obj.name, obj.StartDate, obj.UpdateWeekDay, obj.UpdateTime, obj.EpisodeNumber, obj.Special, obj.ViewPlatform))
    
    conn.commit()
    conn.close()
=======
    if isinstance(obj, WeeklyAnime):
        cursor.execute("""
                INSERT INTO anime_list (type, name, start_date, weekday, time, episodes, special, platform)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, ("Weekly", obj.name, obj.StartDate, obj.UpdateWeekDay, obj.UpdateTime, obj.EpisodeNumber, obj.Special, obj.ViewPlatform)) 
    elif isinstance(obj, AnimeMovie): 
            cursor.execute("""
                INSERT INTO anime_list (type, name, start_date, time, special, platform)
                VALUES (?, ?, ?, ?, ?, ?)
            """, ("Movie", obj.name, obj.StartDate, obj.ScreenTime, obj.Cinema, obj.ViewPlatform)) 

    conn.commit()
>>>>>>> Stashed changes

@app.command()
def create_entry():
    "Add logic"
    console.print("[bold cyan]Add New Entry[/bold cyan]")
    is_movie = typer.confirm("Is this a movie?")

    # 1. name
    name = typer.prompt("1. Name")
    # 2. start airing date
    start_date = typer.prompt("2. Start airing date (DD/MM/YYYY)")
    if not is_movie:
        # 3. update per ? day
        weekday = typer.prompt("3. Update per ? day (e.g., Monday)")
        # 4. update at ? time
        u_time = typer.prompt("4. Update at ? time (HH:MM)")
        # 5. episode number
        eps = typer.prompt("5. Episode number")
        # 6. special arrangements
        special = typer.prompt("6. Special arrangements", default="None")
        # 7. view platform
        platform = typer.prompt("7. View platform")
        new_obj = WeeklyAnime(name, start_date, weekday, u_time, eps, special, platform)
    else:
        u_time = typer.prompt("3. Screening time") 
        cinema = typer.prompt("4. Cinema location") 
        platform = typer.prompt("5. View platform") 
        new_obj = AnimeMovie(name, start_date, u_time, cinema, platform)

<<<<<<< Updated upstream
    new_anime_obj = WeeklyAnime(name, start_date, weekday, u_time, eps, special, platform)

    save_to_sqlite(new_anime_obj)
=======

    save_to_sqlite(new_obj)
>>>>>>> Stashed changes

    console.print(f"\n[bold green]Successfully created and saved: {name}![/bold green]")

if __name__ == "__main__":
    app()