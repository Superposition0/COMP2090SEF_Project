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
                print("[red]Rate is not in the range (0-10)")
                rate = int(typer.prompt("Enter the rate (out of 10)"))
            confirm = typer.confirm("Do you confirm this change?")
            if confirm == True:
                flag = True
                cur.execute("UPDATE anime SET Ratings = ? WHERE Name = ?",(rate, toBeChange))
                print("Rated!")
                conn.commit()
                conn.close()
                return "done"
            elif confirm == False:
                ...

    #interface for changing notes
    def notes_change(self, name):
        toBeChange = name
        flag = False
        while flag == False:
            notes = str(typer.prompt("Enter the notes"))
            confirm = typer.confirm("Do you confirm this change?")
            if confirm == True:
                flag = True
                cur.execute("UPDATE anime SET Notes = ? WHERE Name = ?",(notes, toBeChange))
                print("Noted!")
                conn.commit()
                conn.close()
                return "done"
            elif confirm == False:
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

    #fetch data from object
    a = anime()
    Name = a.name_get
    ViewStatus = a.VS_get
    Ratings = a.ratings_get
    Notes = a.notes_get
    num = [n+1 for n in range(len(Name))] #number to show next to each entries

    #data render
    for n,i,j,k,l in zip(num,Name,ViewStatus,Ratings,Notes):
            table.add_row("[green b]{}".format(n),"{}".format(i), "{}".format(j), "{}".format(k), "{}".format(l))

    if table.columns:
        flag = False
        while flag == False:
            os.system("clear || cls")
            print(table)
            #prompt user to do action
            action = typer.prompt("Enter Your Action (Rate/Note/Quit) ")
            action = action.strip()
            action = action.lower()
            #if user want to rate
            if action == "rate":
                rateNum = int(typer.prompt("Enter the no. of anime you want to rate"))
                #check if the item exist
                if rateNum > num[-1]:
                    print("[red]Item not exist! Try again")
                    time.sleep(0.5)
                    continue
                #clear, show only selected anime and prompts
                os.system("clear || cls")
                print("[yellow i]Selected: ", Name[rateNum-1])
                if a.ratings_change(Name[rateNum-1]) == "done":
                    decision = typer.confirm("Want to do other changes?")
                    if decision == True:
                        continue
                    elif decision == False:
                        flag = True

            #if user want to note
            elif action == "note":
                noteNum = int(typer.prompt("Enter the no. of anime you want to add note"))
                #check if the item exist
                if noteNum > num[-1]:
                    print("[red]Item not exist! Try again")
                    time.sleep(0.5)
                    continue
                #clear, show only selected anime and prompts
                os.system("clear || cls")
                print("[yellow i]Selected: ", Name[noteNum-1])
                if a.notes_change(Name[noteNum-1]) == "done":
                    decision = typer.confirm("Want to do other changes?")
                    if decision == True:
                        continue
                    elif decision == False:
                        flag = True

            #if user want to quit
            elif action == "quit":
                flag = True
                os.system("clear || cls")
                typer.Exit()

            #if user enter other things
            else:
                print("[red]Unsupported action, Please enter again.")
                time.sleep(0.5)
    else:
        print("[red i]Render Error, Please Restart")

    conn.close()



if __name__ == "__main__":
    main()
    conn.close()

