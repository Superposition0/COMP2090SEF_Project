#Import Area
import os
import sqlite3
import typer
from rich import print, box
from rich.table import Table
from pathlib import Path

#Database connection
dir_path = Path(os.path.dirname(__file__))
root = dir_path / "animate_tracker.db"
conn = sqlite3.connect(root)
cur = conn.cursor()
res = cur.execute("SELECT name From sqlite_master")
e = res.fetchone() is None
if not(e):
    ...
else:
    print("[red i]Database Error! Please Restart")

class anime:
    def __init__(self):
        cur.execute("""SELECT Name, ViewStatus, Ratings, Notes FROM anime WHERE ViewStatus = "Abandoned" OR ViewStatus = "Finished" ORDER BY StartDate""")
        self.output = cur.fetchall()
        self.Name = [item[0] for item in self.output]
        self.ViewStatus = [item[1] for item in self.output]
        self.Ratings = [item[2] for item in self.output]
        self.Notes = [item[3] for item in self.output]
    def ratings_change(self, name):
        toBeChange = name
        flag = False
        while flag == False:
            rate = int(typer.prompt("Enter the rate (out of 10)"))
            while rate< 0 or rate> 10:
                rate = typer.prompt("Enter the rate (out of 10)")
            confirm = typer.prompt("Do you confirm this change?(Yes/No)")
            confirm = confirm.strip()
            confirm = confirm.lower()
            if confirm == "yes":
                flag = True
                cur.execute("UPDATE anime SET Ratings = ? WHERE Name = ?",(rate, toBeChange))
                print("Rated!")
                conn.commit()
                conn.close()
                typer.Exit()
            elif confirm == "no":
                ...
    def notes_change(self, name):
        toBeChange = name
        flag = False
        while flag == False:
            notes = str(typer.prompt("Enter the notes"))
            while len(notes) <= 0:
                notes = typer.prompt("Enter the notes")
            confirm = typer.prompt("Do you confirm this change?(Yes/No)")
            confirm = confirm.strip()
            confirm = confirm.lower()
            if confirm == "yes":
                flag = True
                cur.execute("UPDATE anime SET Notes = ? WHERE Name = ?",(notes, toBeChange))
                print("Noted!")
                conn.commit()
                conn.close()
                typer.Exit()
            elif confirm == "no":
                ...
    @property
    def name_get(self):
        return self.Name
    @property
    def VS_get(self):
        return list(self.ViewStatus)
    @property
    def ratings_get(self):
        return list(self.Ratings)
    @property
    def notes_get(self):
        return list(self.Notes)



def main():
    table = Table(title="Archived Anime", box=box.HEAVY, safe_box=False, expand=True, show_lines=True)
    table.add_column("No.")
    table.add_column("Name")
    table.add_column("View Status")
    table.add_column("Ratings")
    table.add_column("Notes")
    a = anime()
    Name = a.name_get
    ViewStatus = a.VS_get
    Ratings = a.ratings_get
    Notes = a.notes_get
    num = [n+1 for n in range(len(Name))]
    for n,i,j,k,l in zip(num,Name,ViewStatus,Ratings,Notes):
            table.add_row("[green b]{}".format(n),"{}".format(i), "{}".format(j), "{}".format(k), "{}".format(l))
    if table.columns:
        print(table)
        flag = False

        while flag == False:
            action = typer.prompt("Enter Your Action (Rate/Note/Quit) ")
            action = action.strip()
            action = action.lower()
            if action == "rate":
                flag =True
                rateNum = int(typer.prompt("Enter the no. of anime you want to rate"))
                os.system("clear || cls")
                print("[yellow i]Selected: ", Name[rateNum-1])
                a.ratings_change(Name[rateNum-1])
            elif action == "note":
                flag = True
                noteNum = int(typer.prompt("Enter the no. of anime you want to add note"))
                os.system("clear || cls")
                print("[yellow i]Selected: ", Name[noteNum-1])
                a.notes_change(Name[noteNum-1])
            elif action == "quit":
                flag = True
                os.system("clear || cls")
                typer.Exit()
            else:
                print("[red]Unsupported action, Please enter again.")

    else:
        print("[red i]Render Error, Please Restart")


if __name__ == "__main__":
    main()
    conn.close()

