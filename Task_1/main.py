#Import Area
import os
import sqlite3
import typer
import datetime
from rich import print, box
from rich.text import Text
from rich.table import Table
from archive import main as aaa
from Change_Stat import main as csm
from create import create_entry as cm
from pathlib import Path

#Database connection
dir_path = Path(os.path.dirname(__file__))
root = dir_path / "animate_tracker.db"
conn = sqlite3.connect(root)
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
        action = typer.prompt("Enter Your Action (Add/Update/Archive/Quit) ")
        action = action.strip()
        action = action.lower()
        if action == "add":
            os.system("clear || cls")
            cm()
        elif action == "update":
            os.system("clear || cls")
            csm()
        elif action == "archive":
            os.system("clear || cls")
            aaa()
        elif action == "quit":
            os.system("clear || cls")
            typer.Exit()
        else:
            print("[red]Unsupported action, Please enter again.")
            return router()

currentDate = datetime.datetime.now()
#Episode Calculator
def epCalc(SD):
        CD = currentDate.strftime("%d/%m/%Y")
        CD = datetime.datetime.strptime(CD, "%d/%m/%Y").isocalendar()[1]
        SD = datetime.datetime.strptime(SD, "%d/%m/%Y").isocalendar()[1]
        diff = (abs(SD-CD))+1
        return diff

def weekNumCalc(SD):
    toBeProcess = datetime.datetime.strptime(SD, "%d/%m/%Y")
    processed = toBeProcess.strftime("%W")
    return processed

def main():
    #Date getter and formatter
    DisplayDate = currentDate.strftime("%d/%m/%Y, %A")
    SQLDate = currentDate.strftime("%d/%m/%Y")
    WeekNum = currentDate.strftime("%w")
    CurrWeekNum = currentDate.strftime("%W")


    #Welcome header
    welcomeMessage = Text(r''''
                                                                 ___
 \    / _  |  _  _  ._ _   _    _|_  _     /\  ._  o ._ _   _     | ._ _.  _ |   _  ._ |
  \/\/ (/_ | (_ (_) | | | (/_    |_ (_)   /--\ | | | | | | (/_    | | (_| (_ |< (/_ |  o
' ''')
    welcomeMessage.stylize("bold magenta")
    os.system("clear || cls")
    print(welcomeMessage)
    #Week view base template
    print(f"[green bold]Today is {DisplayDate}")
    table = Table(title="This Week Anime", box=box.ASCII2, safe_box=False, show_header=False, expand=True)

    #Monday
    tableMon = Table(box=box.SIMPLE, safe_box=False, expand=True, style="on steel_blue" if WeekNum=="1" else "")
    tableMon.add_column("Monday", justify="left")
    #SQL & fetch for weekly anime

    cur.execute("""SELECT Name, UpdateTime, StartDate, EpisodeNumber, ViewStatus, ViewPlatform FROM anime WHERE UpdateWeekDay = 1 AND ViewStatus = "" AND EpisodeNumber != "" ORDER BY UpdateTime""")
    output1 = cur.fetchall()
    cur.execute("""SELECT Name, StartDate, Time, Cinema, EpisodeNumber, UpdateWeekDay FROM anime WHERE
    UpdateWeekDay = 1 AND StartDate >= ? AND ViewStatus = "" AND EpisodeNumber = "" ORDER BY Time""", (SQLDate, ))
    output1c = cur.fetchall()

    #Fetched item unpack into list
    bMonName = [item[0] for item in output1]
    bMonUTime = [item[1] for item in output1]
    bMonStartDate = [item[2] for item in output1]
    bMonTotalEpisode = [item[3] for item in output1]
    bMonViewPlatform = [item[5] for item in output1]

    #Determine if the anime start date is on the same week or later of the current date
    MonWeekNum = list(map(weekNumCalc, bMonStartDate))
    MonWeekNumCompare = [True if x <= CurrWeekNum else False for x in MonWeekNum]
    MonName = []
    MonUTime = []
    MonStartDate = []
    MonTotalEpisode = []
    MonViewPlatform = []
    for i in range(len(MonWeekNumCompare)):
        if MonWeekNumCompare[i] == True:
            MonName.append(bMonName[i])
            MonUTime.append(bMonUTime[i])
            MonStartDate.append(bMonStartDate[i])
            MonTotalEpisode.append(bMonTotalEpisode[i])
            MonViewPlatform.append(bMonViewPlatform[i])

    #MonEPCurrent: calculate current episode of such anime with func epCalc; MonEPExceed: if current episode number>total episode number of the anime = not listed
    MonEPCurrent = list(map(epCalc, MonStartDate))
    MonEPExceed = [i>=j for i, j in zip(MonTotalEpisode, MonEPCurrent)]
    MonNameOnAir = []
    MonTimeOnAir = []
    MonEpisodeOnAir = []
    MonVPOnAir = []
    #Bind anime that should be listed into new lists
    for i in range(len(MonEPExceed)):
        if MonEPExceed[i] == True:
            MonNameOnAir.append(MonName[i])
            MonTimeOnAir.append(MonUTime[i])
            MonEpisodeOnAir.append(MonEPCurrent[i])
            MonVPOnAir.append(MonViewPlatform[i])
    #Data render
    for i,j,k,l in zip(MonNameOnAir, MonTimeOnAir, MonEpisodeOnAir,MonVPOnAir):
        tableMon.add_row("{} \n[green]{} [blue]ep.{} \n[purple]{}".format(i,j,k,l))
        tableMon.add_row("------")
    #Fetched item unpack into list(movie)
    MonCName = [item[0] for item in output1c]
    MonCTime = [item[2] for item in output1c]
    MonCCinema = [item[3] for item in output1c]
    #Data render
    for i,j,k in zip(MonCName, MonCTime, MonCCinema):
        tableMon.add_row("{} \n[green]{} \n[yellow]@ {}".format(i,j,k))
        tableMon.add_row("------")


    #Tuesday
    tableTue = Table(box=box.SIMPLE, safe_box=False, expand=True, style="on steel_blue" if WeekNum=="2" else "")
    tableTue.add_column("Tuesday", justify="left")
    #SQL & fetch for weekly anime

    cur.execute("""SELECT Name, UpdateTime, StartDate, EpisodeNumber, ViewStatus, ViewPlatform FROM anime WHERE UpdateWeekDay = 2 AND ViewStatus = "" AND EpisodeNumber != "" ORDER BY UpdateTime""")
    output2 = cur.fetchall()
    cur.execute("""SELECT Name, StartDate, Time, Cinema, EpisodeNumber, UpdateWeekDay FROM anime WHERE
    UpdateWeekDay = 2 AND StartDate >= ? AND ViewStatus = "" AND EpisodeNumber = "" ORDER BY Time""", (SQLDate, ))
    output2c = cur.fetchall()

    #Fetched item unpack into list
    bTueName = [item[0] for item in output2]
    bTueUTime = [item[1] for item in output2]
    bTueStartDate = [item[2] for item in output2]
    bTueTotalEpisode = [item[3] for item in output2]
    bTueViewPlatform = [item[5] for item in output2]

    #Determine if the anime start date is on the same week or later of the current date
    TueWeekNum = list(map(weekNumCalc, bTueStartDate))
    TueWeekNumCompare = [True if x <= CurrWeekNum else False for x in TueWeekNum]
    TueName = []
    TueUTime = []
    TueStartDate = []
    TueTotalEpisode = []
    TueViewPlatform = []
    for i in range(len(TueWeekNumCompare)):
        if TueWeekNumCompare[i] == True:
            TueName.append(bTueName[i])
            TueUTime.append(bTueUTime[i])
            TueStartDate.append(bTueStartDate[i])
            TueTotalEpisode.append(bTueTotalEpisode[i])
            TueViewPlatform.append(bTueViewPlatform[i])

    #TueEPCurrent: calculate current episode of such anime with func epCalc; TueEPExceed: if current episode number>total episode number of the anime = not listed
    TueEPCurrent = list(map(epCalc, TueStartDate))
    TueEPExceed = [i>=j for i, j in zip(TueTotalEpisode, TueEPCurrent)]
    TueNameOnAir = []
    TueTimeOnAir = []
    TueEpisodeOnAir = []
    TueVPOnAir = []
    #Bind anime that should be listed into new lists
    for i in range(len(TueEPExceed)):
        if TueEPExceed[i] == True:
            TueNameOnAir.append(TueName[i])
            TueTimeOnAir.append(TueUTime[i])
            TueEpisodeOnAir.append(TueEPCurrent[i])
            TueVPOnAir.append(TueViewPlatform[i])
    #Data render
    for i,j,k,l in zip(TueNameOnAir, TueTimeOnAir, TueEpisodeOnAir,TueVPOnAir):
        tableTue.add_row("{} \n[green]{} [blue]ep.{} \n[purple]{}".format(i,j,k,l))
        tableTue.add_row("------")
    #Fetched item unpack into list(movie)
    TueCName = [item[0] for item in output2c]
    TueCTime = [item[2] for item in output2c]
    TueCCinema = [item[3] for item in output2c]
    #Data render
    for i,j,k in zip(TueCName, TueCTime, TueCCinema):
        tableTue.add_row("{} \n[green]{} \n[yellow]@ {}".format(i,j,k))
        tableTue.add_row("------")


    #Wednesday
    tableWed = Table(box=box.SIMPLE, safe_box=False, expand=True, style="on steel_blue" if WeekNum=="3" else "")
    tableWed.add_column("Wednesday", justify="left")
    #SQL & fetch for weekly anime
    cur.execute("""SELECT Name, UpdateTime, StartDate, EpisodeNumber, ViewStatus, ViewPlatform FROM anime WHERE UpdateWeekDay = 3 AND ViewStatus = "" AND EpisodeNumber != "" ORDER BY UpdateTime""")
    output3 = cur.fetchall()
    cur.execute("""SELECT Name, StartDate, Time, Cinema, EpisodeNumber, UpdateWeekDay FROM anime WHERE
    UpdateWeekDay = 3 AND StartDate >= ? AND ViewStatus = "" AND EpisodeNumber = "" ORDER BY Time""", (SQLDate, ))
    output3c = cur.fetchall()

    #Fetched item unpack into list
    bWedName = [item[0] for item in output3]
    bWedUTime = [item[1] for item in output3]
    bWedStartDate = [item[2] for item in output3]
    bWedTotalEpisode = [item[3] for item in output3]
    bWedViewPlatform = [item[5] for item in output3]

    #Determine if the anime start date is on the same week or later of the current date
    WedWeekNum = list(map(weekNumCalc, bWedStartDate))
    WedWeekNumCompare = [True if x <= CurrWeekNum else False for x in WedWeekNum]
    WedName = []
    WedUTime = []
    WedStartDate = []
    WedTotalEpisode = []
    WedViewPlatform = []
    for i in range(len(WedWeekNumCompare)):
        if WedWeekNumCompare[i] == True:
            WedName.append(bWedName[i])
            WedUTime.append(bWedUTime[i])
            WedStartDate.append(bWedStartDate[i])
            WedTotalEpisode.append(bWedTotalEpisode[i])
            WedViewPlatform.append(bWedViewPlatform[i])

    #WedEPCurrent: calculate current episode of such anime with func epCalc; WedEPExceed: if current episode number>total episode number of the anime = not listed
    WedEPCurrent = list(map(epCalc, WedStartDate))
    WedEPExceed = [i>=j for i, j in zip(WedTotalEpisode, WedEPCurrent)]
    WedNameOnAir = []
    WedTimeOnAir = []
    WedEpisodeOnAir = []
    WedVPOnAir = []
    #Bind anime that should be listed into new lists
    for i in range(len(WedEPExceed)):
        if WedEPExceed[i] == True:
            WedNameOnAir.append(WedName[i])
            WedTimeOnAir.append(WedUTime[i])
            WedEpisodeOnAir.append(WedEPCurrent[i])
            WedVPOnAir.append(WedViewPlatform[i])
    #Data render
    for i,j,k,l in zip(WedNameOnAir, WedTimeOnAir, WedEpisodeOnAir,WedVPOnAir):
        tableWed.add_row("{} \n[green]{} [blue]ep.{} \n[purple]{}".format(i,j,k,l))
        tableWed.add_row("------")
    #Fetched item unpack into list(movie)
    WedCName = [item[0] for item in output3c]
    WedCTime = [item[2] for item in output3c]
    WedCCinema = [item[3] for item in output3c]
    #Data render
    for i,j,k in zip(WedCName, WedCTime, WedCCinema):
        tableWed.add_row("{} \n[green]{} \n[yellow]@ {}".format(i,j,k))
        tableWed.add_row("------")


    #Thursday
    tableThu = Table(box=box.SIMPLE, safe_box=False, expand=True, style="on steel_blue" if WeekNum=="4" else "")
    tableThu.add_column("Thursday", justify="left")
    #SQL & fetch for weekly anime

    cur.execute("""SELECT Name, UpdateTime, StartDate, EpisodeNumber, ViewStatus, ViewPlatform FROM anime WHERE UpdateWeekDay = 4 AND ViewStatus = "" AND EpisodeNumber != "" ORDER BY UpdateTime""")
    output4 = cur.fetchall()
    cur.execute("""SELECT Name, StartDate, Time, Cinema, EpisodeNumber, UpdateWeekDay FROM anime WHERE
    UpdateWeekDay = 4 AND StartDate >= ? AND ViewStatus = "" AND EpisodeNumber = "" ORDER BY Time""", (SQLDate, ))
    output4c = cur.fetchall()

    #Fetched item unpack into list
    bThuName = [item[0] for item in output4]
    bThuUTime = [item[1] for item in output4]
    bThuStartDate = [item[2] for item in output4]
    bThuTotalEpisode = [item[3] for item in output4]
    bThuViewPlatform = [item[5] for item in output4]

    #Determine if the anime start date is on the same week or later of the current date
    ThuWeekNum = list(map(weekNumCalc, bThuStartDate))
    ThuWeekNumCompare = [True if x <= CurrWeekNum else False for x in ThuWeekNum]
    ThuName = []
    ThuUTime = []
    ThuStartDate = []
    ThuTotalEpisode = []
    ThuViewPlatform = []
    for i in range(len(ThuWeekNumCompare)):
        if ThuWeekNumCompare[i] == True:
            ThuName.append(bThuName[i])
            ThuUTime.append(bThuUTime[i])
            ThuStartDate.append(bThuStartDate[i])
            ThuTotalEpisode.append(bThuTotalEpisode[i])
            ThuViewPlatform.append(bThuViewPlatform[i])

    #ThuEPCurrent: calculate current episode of such anime with func epCalc; ThuEPExceed: if current episode number>total episode number of the anime = not listed
    ThuEPCurrent = list(map(epCalc, ThuStartDate))
    ThuEPExceed = [i>=j for i, j in zip(ThuTotalEpisode, ThuEPCurrent)]
    ThuNameOnAir = []
    ThuTimeOnAir = []
    ThuEpisodeOnAir = []
    ThuVPOnAir = []
    #Bind anime that should be listed into new lists
    for i in range(len(ThuEPExceed)):
        if ThuEPExceed[i] == True:
            ThuNameOnAir.append(ThuName[i])
            ThuTimeOnAir.append(ThuUTime[i])
            ThuEpisodeOnAir.append(ThuEPCurrent[i])
            ThuVPOnAir.append(ThuViewPlatform[i])
    #Data render
    for i,j,k,l in zip(ThuNameOnAir, ThuTimeOnAir, ThuEpisodeOnAir,ThuVPOnAir):
        tableThu.add_row("{} \n[green]{} [blue]ep.{} \n[purple]{}".format(i,j,k,l))
        tableThu.add_row("------")
    #Fetched item unpack into list(movie)
    ThuCName = [item[0] for item in output4c]
    ThuCTime = [item[2] for item in output4c]
    ThuCCinema = [item[3] for item in output4c]
    #Data render
    for i,j,k in zip(ThuCName, ThuCTime, ThuCCinema):
        tableThu.add_row("{} \n[green]{} \n[yellow]@ {}".format(i,j,k))
        tableThu.add_row("------")


    #Friday
    tableFri = Table(box=box.SIMPLE, safe_box=False, expand=True, style="on steel_blue" if WeekNum=="5" else "")
    tableFri.add_column("Friday", justify="left")
    #SQL & fetch for weekly anime
    cur.execute("""SELECT Name, UpdateTime, StartDate, EpisodeNumber, ViewStatus, ViewPlatform FROM anime WHERE UpdateWeekDay = 5 AND ViewStatus = "" AND EpisodeNumber != "" ORDER BY UpdateTime""")
    output5 = cur.fetchall()
    cur.execute("""SELECT Name, StartDate, Time, Cinema, EpisodeNumber, UpdateWeekDay FROM anime WHERE
    UpdateWeekDay = 5 AND StartDate >= ? AND ViewStatus = "" AND EpisodeNumber = "" ORDER BY Time""", (SQLDate, ))
    output5c = cur.fetchall()

    #Fetched item unpack into list
    bFriName = [item[0] for item in output5]
    bFriUTime = [item[1] for item in output5]
    bFriStartDate = [item[2] for item in output5]
    bFriTotalEpisode = [item[3] for item in output5]
    bFriViewPlatform = [item[5] for item in output5]

    #Determine if the anime start date is on the same week or later of the current date
    FriWeekNum = list(map(weekNumCalc, bFriStartDate))
    FriWeekNumCompare = [True if x <= CurrWeekNum else False for x in FriWeekNum]
    FriName = []
    FriUTime = []
    FriStartDate = []
    FriTotalEpisode = []
    FriViewPlatform = []
    for i in range(len(FriWeekNumCompare)):
        if FriWeekNumCompare[i] == True:
            FriName.append(bFriName[i])
            FriUTime.append(bFriUTime[i])
            FriStartDate.append(bFriStartDate[i])
            FriTotalEpisode.append(bFriTotalEpisode[i])
            FriViewPlatform.append(bFriViewPlatform[i])

    #FriEPCurrent: calculate current episode of such anime with func epCalc; FriEPExceed: if current episode number>total episode number of the anime = not listed
    FriEPCurrent = list(map(epCalc, FriStartDate))
    FriEPExceed = [i>=j for i, j in zip(FriTotalEpisode, FriEPCurrent)]
    FriNameOnAir = []
    FriTimeOnAir = []
    FriEpisodeOnAir = []
    FriVPOnAir = []
    #Bind anime that should be listed into new lists
    for i in range(len(FriEPExceed)):
        if FriEPExceed[i] == True:
            FriNameOnAir.append(FriName[i])
            FriTimeOnAir.append(FriUTime[i])
            FriEpisodeOnAir.append(FriEPCurrent[i])
            FriVPOnAir.append(FriViewPlatform[i])
    #Data render
    for i,j,k,l in zip(FriNameOnAir, FriTimeOnAir, FriEpisodeOnAir,FriVPOnAir):
        tableFri.add_row("{} \n[green]{} [blue]ep.{} \n[purple]{}".format(i,j,k,l))
        tableFri.add_row("------")
    #Fetched item unpack into list(movie)
    FriCName = [item[0] for item in output5c]
    FriCTime = [item[2] for item in output5c]
    FriCCinema = [item[3] for item in output5c]
    #Data render
    for i,j,k in zip(FriCName, FriCTime, FriCCinema):
        tableFri.add_row("{} \n[green]{} \n[yellow]@ {}".format(i,j,k))
        tableFri.add_row("------")


    #Saturday
    tableSat = Table(box=box.SIMPLE, safe_box=False, expand=True, style="on steel_blue" if WeekNum=="6" else "")
    tableSat.add_column("Saturday", justify="left")
    #SQL & fetch for weekly anime
    cur.execute("""SELECT Name, UpdateTime, StartDate, EpisodeNumber, ViewStatus, ViewPlatform FROM anime WHERE UpdateWeekDay = 6 AND ViewStatus = "" AND EpisodeNumber != "" ORDER BY UpdateTime""")
    output6 = cur.fetchall()
    cur.execute("""SELECT Name, StartDate, Time, Cinema, EpisodeNumber, UpdateWeekDay FROM anime WHERE
    UpdateWeekDay = 6 AND StartDate >= ? AND ViewStatus = "" AND EpisodeNumber = "" ORDER BY Time""", (SQLDate, ))
    output6c = cur.fetchall()

    #Fetched item unpack into list
    bSatName = [item[0] for item in output6]
    bSatUTime = [item[1] for item in output6]
    bSatStartDate = [item[2] for item in output6]
    bSatTotalEpisode = [item[3] for item in output6]
    bSatViewPlatform = [item[5] for item in output6]

    #Determine if the anime start date is on the same week or later of the current date
    SatWeekNum = list(map(weekNumCalc, bSatStartDate))
    SatWeekNumCompare = [True if x <= CurrWeekNum else False for x in SatWeekNum]
    SatName = []
    SatUTime = []
    SatStartDate = []
    SatTotalEpisode = []
    SatViewPlatform = []
    for i in range(len(SatWeekNumCompare)):
        if SatWeekNumCompare[i] == True:
            SatName.append(bSatName[i])
            SatUTime.append(bSatUTime[i])
            SatStartDate.append(bSatStartDate[i])
            SatTotalEpisode.append(bSatTotalEpisode[i])
            SatViewPlatform.append(bSatViewPlatform[i])

    #SatEPCurrent: calculate current episode of such anime with func epCalc; SatEPExceed: if current episode number>total episode number of the anime = not listed
    SatEPCurrent = list(map(epCalc, SatStartDate))
    SatEPExceed = [i>=j for i, j in zip(SatTotalEpisode, SatEPCurrent)]
    SatNameOnAir = []
    SatTimeOnAir = []
    SatEpisodeOnAir = []
    SatVPOnAir = []
    #Bind anime that should be listed into new lists
    for i in range(len(SatEPExceed)):
        if SatEPExceed[i] == True:
            SatNameOnAir.append(SatName[i])
            SatTimeOnAir.append(SatUTime[i])
            SatEpisodeOnAir.append(SatEPCurrent[i])
            SatVPOnAir.append(SatViewPlatform[i])
    #Data render
    for i,j,k,l in zip(SatNameOnAir, SatTimeOnAir, SatEpisodeOnAir,SatVPOnAir):
        tableSat.add_row("{} \n[green]{} [blue]ep.{} \n[purple]{}".format(i,j,k,l))
        tableSat.add_row("------")
    #Fetched item unpack into list(movie)
    SatCName = [item[0] for item in output6c]
    SatCTime = [item[2] for item in output6c]
    SatCCinema = [item[3] for item in output6c]
    #Data render
    for i,j,k in zip(SatCName, SatCTime, SatCCinema):
        tableSat.add_row("{} \n[green]{} \n[yellow]@ {}".format(i,j,k))
        tableSat.add_row("------")

    #Sunday
    tableSun = Table(box=box.SIMPLE, safe_box=False, expand=True, style="on steel_blue" if WeekNum=="0" else "")
    tableSun.add_column("Sunday", justify="left")

    #SQL & fetch for weekly anime
    cur.execute("""SELECT Name, UpdateTime, StartDate, EpisodeNumber, ViewStatus, ViewPlatform FROM anime WHERE UpdateWeekDay = 0 AND ViewStatus = "" AND EpisodeNumber != "" ORDER BY UpdateTime""")
    output0 = cur.fetchall()
    cur.execute("""SELECT Name, StartDate, Time, Cinema, EpisodeNumber, UpdateWeekDay FROM anime WHERE
    UpdateWeekDay = 0 AND StartDate >= ? AND ViewStatus = "" AND EpisodeNumber = "" ORDER BY Time""", (SQLDate, ))
    output0c = cur.fetchall()
    #Fetched item unpack into list
    bSunName = [item[0] for item in output0]
    bSunUTime = [item[1] for item in output0]
    bSunStartDate = [item[2] for item in output0]
    bSunTotalEpisode = [item[3] for item in output0]
    bSunViewPlatform = [item[5] for item in output0]

    #Determine if the anime start date is on the same week or later of the current date
    SunWeekNum = list(map(weekNumCalc, bSunStartDate))
    SunWeekNumCompare = [True if x <= CurrWeekNum else False for x in SunWeekNum]
    SunName = []
    SunUTime = []
    SunStartDate = []
    SunTotalEpisode = []
    SunViewPlatform = []
    for i in range(len(SunWeekNumCompare)):
        if SunWeekNumCompare[i] == True:
            SunName.append(bSunName[i])
            SunUTime.append(bSunUTime[i])
            SunStartDate.append(bSunStartDate[i])
            SunTotalEpisode.append(bSunTotalEpisode[i])
            SunViewPlatform.append(bSunViewPlatform[i])

    #SunEPCurrent: calculate current episode of such anime with func epCalc; SunEPExceed: if current episode number>total episode number of the anime = not listed
    SunEPCurrent = list(map(epCalc, SunStartDate))
    SunEPExceed = [i>=j for i, j in zip(SunTotalEpisode, SunEPCurrent)]
    SunNameOnAir = []
    SunTimeOnAir = []
    SunEpisodeOnAir = []
    SunVPOnAir = []
    #Bind anime that should be listed into new lists
    for i in range(len(SunEPExceed)):
        if SunEPExceed[i] == True:
            SunNameOnAir.append(SunName[i])
            SunTimeOnAir.append(SunUTime[i])
            SunEpisodeOnAir.append(SunEPCurrent[i])
            SunVPOnAir.append(SunViewPlatform[i])
    #Data render
    for i,j,k,l in zip(SunNameOnAir, SunTimeOnAir, SunEpisodeOnAir,SunVPOnAir):
        tableSun.add_row("{} \n[green]{} [blue]ep.{} \n[purple]{}".format(i,j,k,l))
        tableSun.add_row("------")
    #Fetched item unpack into list(movie)
    SunCName = [item[0] for item in output0c]
    SunCTime = [item[2] for item in output0c]
    SunCCinema = [item[3] for item in output0c]
    #Data render
    for i,j,k in zip(SunCName, SunCTime, SunCCinema):
        tableSun.add_row("{} \n[green]{} \n[yellow]@ {}".format(i,j,k))
        tableSun.add_row("------")
    #conn.close()

    #Table printer
    for i in range(7):
        table.add_column()
    table.add_row(tableMon,tableTue,tableWed,tableThu,tableFri,tableSat,tableSun)
    if table.columns:
        print(table)
        intro = Text("Add - Add a new anime to the tracker\nUpdate - Update an anime's details\nArchive - Show archived anime with ratings and notes\nQuit - Quit this app")
        intro.stylize("light_steel_blue")
        print(intro)
        router()
    else:
        print("[red i]Render Error, Please Restart")



if __name__ == "__main__":
    typer.run(main)
