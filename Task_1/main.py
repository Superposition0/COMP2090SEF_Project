#Import Area
import sqlite3
import typer
import datetime
from rich import print, box
from rich.text import Text
from rich.table import Table
from archive import archive

#Database connection
conn = sqlite3.connect("Task_1/animate_tracker.db")
cur = conn.cursor()
res = cur.execute("SELECT name From sqlite_master")
e = res.fetchone() is None
if not(e):
    pass
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
    #Welcome header
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

    #Sunday
    tableSun = Table(box=box.SIMPLE, safe_box=False, expand=True, style="on steel_blue" if WeekNum=="0" else "")
    tableSun.add_column("Sunday", justify="left")
    cur.execute("""
    SELECT name, UpdateTime, StartDate, EpisodeNumber FROM anime WHERE UpdateWeekDay = 0 ORDER BY UpdateTime
""")
    output0 = cur.fetchall()
    SunName = [item[0] for item in output0]
    SunTime = [item[1] for item in output0]
    for i,j in zip(SunName,SunTime):
        tableSun.add_row("{} [green]{}".format(i,j))
        tableSun.add_row("------")

    #Monday
    tableMon = Table(box=box.SIMPLE, safe_box=False, expand=True, style="on steel_blue" if WeekNum=="1" else "")
    tableMon.add_column("Monday", justify="left")
    cur.execute("""
    SELECT name, UpdateTime, StartDate, EpisodeNumber FROM anime WHERE UpdateWeekDay = 1 ORDER BY UpdateTime
""")
    output1 = cur.fetchall()
    MonName = [item[0] for item in output1]
    MonTime = [item[1] for item in output1]
    for i,j in zip(MonName,MonTime):
        tableMon.add_row("{} [green]{}".format(i,j))
        tableMon.add_row("------")

    #Tuesday
    tableTue = Table(box=box.SIMPLE, safe_box=False, expand=True, style="on steel_blue" if WeekNum=="2" else "")
    tableTue.add_column("Tuesday", justify="left")
    cur.execute("""
    SELECT name, UpdateTime, StartDate, EpisodeNumber FROM anime WHERE UpdateWeekDay = 2 ORDER BY UpdateTime
""")
    output2 = cur.fetchall()
    TueName = [item[0] for item in output2]
    TueTime = [item[1] for item in output2]
    for i,j in zip(TueName,TueTime):
        tableTue.add_row("{} [green]{}".format(i,j))
        tableTue.add_row("------")

    #Wednesday
    tableWed = Table(box=box.SIMPLE, safe_box=False, expand=True, style="on steel_blue" if WeekNum=="3" else "")
    tableWed.add_column("Wednesday", justify="left")
    cur.execute("""
    SELECT name, UpdateTime, StartDate, EpisodeNumber FROM anime WHERE UpdateWeekDay = 3 ORDER BY UpdateTime
""")
    output3 = cur.fetchall()
    WedName = [item[0] for item in output3]
    WedTime = [item[1] for item in output3]
    for i,j in zip(WedName,WedTime):
        tableWed.add_row("{} [green]{}".format(i,j))
        tableWed.add_row("------")

    #Thursday
    tableThu = Table(box=box.SIMPLE, safe_box=False, expand=True, style="on steel_blue" if WeekNum=="4" else "")
    tableThu.add_column("Thursday", justify="left")
    cur.execute("""
    SELECT name, UpdateTime, StartDate, EpisodeNumber FROM anime WHERE UpdateWeekDay = 4 ORDER BY UpdateTime
""")
    output4 = cur.fetchall()
    ThuName = [item[0] for item in output4]
    ThuTime = [item[1] for item in output4]
    for i,j in zip(ThuName,ThuTime):
        tableThu.add_row("{} [green]{}".format(i,j))
        tableThu.add_row("------")

    #Friday
    tableFri = Table(box=box.SIMPLE, safe_box=False, expand=True, style="on steel_blue" if WeekNum=="5" else "")
    tableFri.add_column("Friday", justify="left")
    cur.execute("""
    SELECT name, UpdateTime, StartDate, EpisodeNumber FROM anime WHERE UpdateWeekDay = 5 ORDER BY UpdateTime
""")
    output5 = cur.fetchall()
    FriName = [item[0] for item in output5]
    FriTime = [item[1] for item in output5]
    for i,j in zip(FriName,FriTime):
        tableFri.add_row("{} [green]{}".format(i,j))
        tableFri.add_row("------")

    #Saturday
    tableSat = Table(box=box.SIMPLE, safe_box=False, expand=True, style="on steel_blue" if WeekNum=="6" else "")
    tableSat.add_column("Saturday", justify="left")
    cur.execute("""
    SELECT name, UpdateTime, StartDate, EpisodeNumber FROM anime WHERE UpdateWeekDay = 6 ORDER BY UpdateTime
""")
    output6 = cur.fetchall()
    SatName = [item[0] for item in output6]
    SatTime = [item[1] for item in output6]
    for i,j in zip(SatName,SatTime):
        tableSat.add_row("{} [green]{}".format(i,j))
        tableSat.add_row("------")

    #Table printer
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

