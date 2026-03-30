#Import Area
import os
import sqlite3
import typer
import time
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

#create class: anime
class anime:
    def __init__(self):
        #fetch data from database and bind them into lists
        cur.execute("""SELECT Name, ViewStatus, Ratings, Notes FROM anime WHERE ViewStatus = "Abandoned" OR ViewStatus = "Finished" ORDER BY StartDate""")
        self.output = cur.fetchall()
        self.Name = [item[0] for item in self.output]
        self.ViewStatus = [item[1] for item in self.output]
        self.Ratings = [item[2] for item in self.output]
        self.Notes = [item[3] for item in self.output]
    #interface for changing rate
    def ratings_change(self, name):
        toBeChange = name
        flag = False
        while flag == False:
            rate = int(typer.prompt("Enter the rate (out of 10)"))
            while rate< 0 or rate> 10:
                rate = int(typer.prompt("Enter the rate (out of 10)"))
            confirm = typer.prompt("Do you confirm this change?(Yes/No)")
            confirm = confirm.strip()
            confirm = confirm.lower()
            if confirm == "yes":
                flag = True
                cur.execute("UPDATE anime SET Ratings = ? WHERE Name = ?",(rate, toBeChange))
                print("Rated!")
                conn.commit()
                return "done"
            elif confirm == "no":
                ...
    #interface for changing notes
    def notes_change(self, name):
        toBeChange = name
        flag = False
        while flag == False:
            notes = str(typer.prompt("Enter the notes"))
            while len(notes) <= 0:
                notes = str(typer.prompt("Enter the notes"))
            confirm = typer.prompt("Do you confirm this change?(Yes/No)")
            confirm = confirm.strip()
            confirm = confirm.lower()
            if confirm == "yes":
                flag = True
                cur.execute("UPDATE anime SET Notes = ? WHERE Name = ?",(notes, toBeChange))
                print("Noted!")
                conn.commit()
                return "done"
            elif confirm == "no":
                ...
    #sql data lists getter
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
    #table setter
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
    num = [n+1 for n in range(len(Name))] #number to show next to each entries
    for n,i,j,k,l in zip(num,Name,ViewStatus,Ratings,Notes):
            table.add_row("[green b]{}".format(n),"{}".format(i), "{}".format(j), "{}".format(k), "{}".format(l))
    if table.columns:
        #prompt user to do action
        flag = False
        while flag == False:
            os.system("clear || cls")
            print(table)
            action = typer.prompt("Enter Your Action (Rate/Note/Quit) ")
            action = action.strip()
            action = action.lower()
            if action == "rate":
                rateNum = int(typer.prompt("Enter the no. of anime you want to rate"))
                if rateNum > num[-1]:
                    print("[red]Item not exist! Enter again")
                    continue
                os.system("clear || cls")
                print("[yellow i]Selected: ", Name[rateNum-1])
                if a.ratings_change(Name[rateNum-1]) == "done":
                    decision = typer.prompt("Want to do other changes? (Yes/No)")
                    decision = decision.strip()
                    decision = decision.lower()
                    if decision == "yes":
                        continue
                    elif decision == "no":
                        flag = True
                    else:
                        print("[red]Unsupported action, Please enter again.")
                        time.sleep(0.5)

            elif action == "note":
                noteNum = int(typer.prompt("Enter the no. of anime you want to add note"))
                if noteNum > num[-1]:
                    print("[red]Item not exist! Enter again")
                    continue
                os.system("clear || cls")
                print("[yellow i]Selected: ", Name[noteNum-1])
                if a.notes_change(Name[noteNum-1]) == "done":
                    decision = typer.prompt("Want to do other changes? (Yes/No)")
                    decision = decision.strip()
                    decision = decision.lower()
                    if decision == "yes":
                        continue
                    elif decision == "no":
                        flag = True
                    else:
                        print("[red]Unsupported action, Please enter again.")
                        time.sleep(0.5)

            elif action == "quit":
                flag = True
                os.system("clear || cls")
                typer.Exit()

            else:
                print("[red]Unsupported action, Please enter again.")
                time.sleep(0.5)
    else:
        print("[red i]Render Error, Please Restart")



if __name__ == "__main__":
    main()
    conn.close()

