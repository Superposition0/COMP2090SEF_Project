# Add prompts
# Remove ratings and notes
# Change 'cls' to 'cls || clear'

import os
import sqlite3
import typer
from rich import print, box
from rich.table import Table
from pathlib import Path

temp_list=[]
anime_list=[]
anime_stat=[]
anime_plat=[]
anime_date=[]
anime_time=[]
anime_weekday=[]
anime_upTime=[]
anime_cinema=[]
anime_episode=[]
action_listTV=['name', 'start date', 'time', 'update weekday', 'update time', 'episodes', 'status', 'platform']
action_listCinema=['name', 'start date', 'time', 'update weekday', 'update time', 'cinema', 'status', 'platform']

def get_file():
    dir_path = Path(os.path.dirname(__file__))
    root = dir_path / "animate_tracker.db"
    file_conn=sqlite3.connect(root)
    file_cur=file_conn.cursor()
    file_cur.execute("SELECT Name FROM anime ORDER BY UpdateTime")
    list_input=file_cur.fetchall()
    for item in list_input:
        item_str=str(item)
        anime_list.append(item_str.replace(",", "").replace("('", "").replace("')", ""))
        temp_list.append(item_str.replace(",", "").replace("('", "").replace("')", ""))
    file_cur.execute("SELECT ViewStatus FROM anime ORDER BY UpdateTime")
    list_stat=file_cur.fetchall()
    for item in list_stat:
        item_str=str(item)
        anime_stat.append(item_str.replace(",", "").replace("('", "").replace("')", ""))
    file_cur.execute("SELECT ViewPlatform FROM anime ORDER BY UpdateTime")
    list_platform=file_cur.fetchall()
    for item in list_platform:
        item_str=str(item)
        anime_plat.append(item_str.replace(",", "").replace("('", "").replace("')", ""))
    file_cur.execute("SELECT StartDate FROM anime ORDER BY UpdateTime")
    list_date=file_cur.fetchall()
    for item in list_date:
        item_str=str(item)
        anime_date.append(item_str.replace(",", "").replace("('", "").replace("')", ""))
    file_cur.execute("SELECT Time FROM anime ORDER BY UpdateTime")
    list_time=file_cur.fetchall()
    for item in list_time:
        item_str=str(item)
        anime_time.append(item_str.replace(",", "").replace("('", "").replace("')", ""))
    file_cur.execute("SELECT UpdateWeekDay FROM anime ORDER BY UpdateTime")
    list_updateDay=file_cur.fetchall()
    for item in list_updateDay:
        item_str=str(item)
        anime_weekday.append(item_str.replace(",", "").replace("('", "").replace("')", "").replace('(', '').replace(')', ''))
    file_cur.execute("SELECT UpdateTime FROM anime ORDER BY UpdateTime")
    list_upTime=file_cur.fetchall()
    for item in list_upTime:
        item_str=str(item)
        anime_upTime.append(item_str.replace(",", "").replace("('", "").replace("')", ""))
    file_cur.execute("SELECT Cinema FROM anime ORDER BY UpdateTime")
    list_cinema=file_cur.fetchall()
    for item in list_cinema:
        item_str=str(item)
        anime_cinema.append(item_str.replace(",", "").replace("('", "").replace("')", ""))
    file_cur.execute("SELECT EpisodeNumber FROM anime ORDER BY UpdateTime")
    list_episode=file_cur.fetchall()
    for item in list_episode:
        item_str=str(item)
        anime_episode.append(item_str.replace(",", "").replace("('", "").replace("')", "").replace('(', '').replace(')', ''))

def info_display_movie(number):
    info_table=Table(title='Anime Movie', box=box.HEAVY)
    info_table.add_column('Anime Name', justify='center')
    info_table.add_column('Status', justify='center')
    info_table.add_column('Cinema', justify='center')
    info_table.add_column('Date', justify='center')
    info_table.add_column('Time', justify='center')
    info_table.add_column('Update Date', justify='center')
    info_table.add_column('Update Time', justify='center')
    info_table.add_column('Special', justify='center')
    info_table.add_column('Rating', justify='center')
    info_table.add_column('Notes', justify='center')

    info_table.add_row(anime_list[number], 
                       anime_stat[number], 
                       anime_cinema[number],
                       anime_date[number],
                       anime_time[number], 
                       anime_weekday[number],
                       anime_upTime[number])
    print(info_table, end='\n')

def info_display_TV(number):
    info_table=Table(title='TV Anime', box=box.HEAVY)
    info_table.add_column('Anime Name', justify='center')
    info_table.add_column('Status', justify='center')
    info_table.add_column('Platform', justify='center')
    info_table.add_column('Episodes', justify='center')
    info_table.add_column('Date', justify='center')
    info_table.add_column('Time', justify='center')
    info_table.add_column('Update Date', justify='center')
    info_table.add_column('Update Time', justify='center')

    info_table.add_row(anime_list[number], 
                       anime_stat[number], 
                       anime_plat[number], 
                       anime_episode[number], 
                       anime_date[number],
                       anime_time[number], 
                       anime_weekday[number],
                       anime_upTime[number])
    print(info_table, end='\n')

class Anime:
    def __init__(self, name, start, time, cinema, up_day, up_time, episodes, status, platform):
        self.name=name
        self.start=start
        self.time=time
        self.cinema=cinema
        self.up_day=up_day
        self.up_time=up_time
        self.episodes=episodes
        self.status=status
        self.platform=platform

    def input_change(self, number, in_action):
        self.in_action=in_action
        self.number=number
        if self.in_action.lower()=='name':
            print('[yellow]Enter the anime name:[/yellow]', end=' ')
            new_value=input()
            self.name=new_value

        elif self.in_action.lower()=='episodes':
            print('[yellow]Enter the episode number (Integer):[/yellow]', end=' ')
            new_value=input()
            self.episodes=new_value
 
        elif self.in_action.lower()=='cinema':
            print('[yellow]Enter the cinema:[/yellow]', end=' ')
            new_value=input()
            self.cinema=new_value

        elif self.in_action.lower()=='status':
            allow=False
            while allow==False:
                print('[yellow]Enter the status (Watching / Abandoned):[/yellow]', end=' ')
                new_value=input()
                if new_value.lower()=='watching' or new_value.lower()=='abandoned':
                    allow=True
                else:
                    print('[bold red]Invaild status.[/bold red]', end=' ')
            self.status=new_value.capitalize()

        elif self.in_action.lower()=='update weekday':
            print('[yellow]Enter the weekday:[/yellow]', end=' ')
            new_value=input()
            self.up_day=new_value

        elif self.in_action.lower()=='update time':
            print('[yellow]Enter the update time:[/yellow]', end=' ')
            new_value=input()
            self.up_time=new_value
            
        elif self.in_action.lower()=='start date':
            print('[yellow]Enter the date:[/yellow]', end=' ')
            new_value=input()
            self.start=new_value
            
        elif self.in_action.lower()=='platform':
            print('[yellow]Enter the platform:[/yellow]', end=' ')
            new_value=input()
            self.platform=new_value
            
        elif self.in_action.lower()=='time':
            print('[yellow]Enter the time:[/yellow]', end=' ')
            new_value=input()
            self.time=new_value

    def overview_TV(self):
        info_table=Table(title='TV Anime Change', box=box.HEAVY)
        info_table.add_column('Anime Name', justify='center')
        info_table.add_column('Status', justify='center')
        info_table.add_column('Platform', justify='center')
        info_table.add_column('Episodes', justify='center')
        info_table.add_column('Date', justify='center')
        info_table.add_column('Time', justify='center')
        info_table.add_column('Update Date', justify='center')
        info_table.add_column('Update Time', justify='center')

        info_table.add_row(self.name, 
                        self.status, 
                        self.platform, 
                        self.episodes, 
                        self.start,
                        self.time, 
                        self.up_day,
                        self.up_time)
        print(info_table, end='\n')

    def overview_cinema(self):
        info_table=Table(title='Anime Movie Change', box=box.HEAVY)
        info_table.add_column('Anime Name', justify='center')
        info_table.add_column('Status', justify='center')
        info_table.add_column('Cinema', justify='center')
        info_table.add_column('Date', justify='center')
        info_table.add_column('Time', justify='center')
        info_table.add_column('Update Date', justify='center')
        info_table.add_column('Update Time', justify='center')

        info_table.add_row(self.name, 
                        self.status, 
                        self.cinema, 
                        self.start,
                        self.time, 
                        self.up_day,
                        self.up_time)
        print(info_table, end='\n')

    def change_table(self):
        dir_path = Path(os.path.dirname(__file__))
        root = dir_path / "animate_tracker.db"
        file_conn=sqlite3.connect(root)
        file_cur=file_conn.cursor()

        if self.in_action.lower()=='name':
            file_cur.execute('UPDATE anime SET Name=? WHERE Name=?', (self.name, anime_list[self.number], ))
            anime_list[self.number]=self.name

        if self.in_action.lower()=='start date':
            file_cur.execute('UPDATE anime SET StartDate=? WHERE Name=?', (self.start, anime_list[self.number], ))
            anime_date[self.number]=self.start

        if self.in_action.lower()=='time':
            file_cur.execute('UPDATE anime SET Time=? WHERE Name=?', (self.time, anime_list[self.number], ))
            anime_time[self.number]=self.time

        if self.in_action.lower()=='cinema':
            file_cur.execute('UPDATE anime SET Cinema=? WHERE Name=?', (self.cinema, anime_list[self.number], ))
            anime_cinema[self.number]=self.cinema

        if self.in_action.lower()=='update weekday':
            file_cur.execute('UPDATE anime SET UpdateWeekday=? WHERE Name=?', (self.up_day, anime_list[self.number], ))
            anime_weekday[self.number]=self.up_day

        if self.in_action.lower()=='update time':
            file_cur.execute('UPDATE anime SET UpdateTime=? WHERE Name=?', (self.up_time, anime_list[self.number], ))
            anime_upTime[self.number]=self.up_time
        
        if self.in_action.lower()=='episodes':
            file_cur.execute('UPDATE anime SET EpisodeNumber=? WHERE Name=?', (self.episodes, anime_list[self.number], ))
            anime_episode[self.number]=self.episodes

        if self.in_action.lower()=='status':
            file_cur.execute('UPDATE anime SET ViewStatus=? WHERE Name=?', (self.status, anime_list[self.number], ))
            anime_stat[self.number]=self.status

        if self.in_action.lower()=='platform':
            file_cur.execute('UPDATE anime SET ViewPlatform=? WHERE Name=?', (self.platform, anime_list[self.number], ))
            anime_plat[self.number]=self.platform

        file_conn.commit()
        file_conn.close()

def main():
    get_file()
    program_run=True
    while program_run==True:
        os.system('cls || clear')
        print('[bold green]Type in the number of the anime to select change.[/bold green] :popcorn:')
        anime_table=Table(title='Anime List', box=box.HEAVY)
        anime_table.add_column('[bold green]No.[/bold green]', justify='left', style='green')
        anime_table.add_column('[bold blue]Anime Name[/bold blue]', justify='center', style='cyan')

        for i in range(len(anime_list)):
            num=str(i+1)
            anime_table.add_row(num, anime_list[i])
            anime_table.add_row('-')
        print(anime_table, end='\n')

        choice=int(input('Please enter the number: '))
        while choice>len(anime_list) or choice<-1:
            print('[bold red]Input is out of range.[/bold red]', end=' ')
            choice=int(input('Please enter again: '))

        if anime_cinema[choice-1]=='':
            anime_loop=True
            while anime_loop==True:
                os.system('cls || clear')
                info_display_TV(choice-1)
                print('[bold green]Please select the above attributes to change: [bold green]', end=' ')
                action=input()
                while action.lower() not in action_listTV:
                    print('[bold red]Invalid action, please try again:[/bold red]', end=' ')
                    action=input()
                anime=Anime(anime_list[choice-1], anime_date[choice-1], anime_time[choice-1], anime_cinema[choice-1], anime_weekday[choice-1], anime_upTime[choice-1], anime_episode[choice-1], anime_stat[choice-1], anime_plat[choice-1])
                anime.input_change(choice-1, action)
                os.system('cls || clear')
                anime.overview_TV()
                print('[yellow]Do you want to confirm your change(s) (Yes / No):[/yellow]', end=' ')
                confirm_choice=input()
                if confirm_choice.lower()=='yes':
                    anime.change_table()
                    anime_loop=False
                elif confirm_choice.lower()=='no':
                    anime_loop=True
            
        else:
            anime_loop=True
            while anime_loop==True:
                os.system('cls || clear')
                info_display_movie(choice-1)
                print('[bold green]Please select the above attributes to change: [bold green]', end=' ')
                action=input()
                while action.lower() not in action_listCinema:
                    print('[bold red]Invalid action, please try again:[/bold red]', end=' ')
                    action=input()
                anime=Anime(anime_list[choice-1], anime_date[choice-1], anime_time[choice-1], anime_cinema[choice-1], anime_weekday[choice-1], anime_upTime[choice-1], anime_episode[choice-1], anime_stat[choice-1], anime_plat[choice-1])
                anime.input_change(choice-1, action)
                os.system('cls || clear')
                anime.overview_cinema()
                print('[yellow]Do you want to confirm your change(s) (Yes / No):[/yellow]', end=' ')
                confirm_choice=input()
                if confirm_choice.lower()=='yes':
                    anime.change_table()
                    anime_loop=False

                elif confirm_choice.lower()=='no':
                    anime_loop=True

        os.system('cls || clear')
        print('[yellow]Would you like to continue on changing info(s) (Yes / No):[/yellow]', end=' ')
        confirm_choice=input()
        if confirm_choice.lower()=='yes':
                program_run=True

        elif confirm_choice.lower()=='no':
                program_run=False
                os.system('cls || clear')

if __name__ == "__main__":
    typer.run(main)
