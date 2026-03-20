import os
import sqlite3
import typer
from rich import print, box
from rich.text import Text
from rich.table import Table
from rich.layout import Layout
from typing import Annotated
from abc import ABC, abstractmethod
from archive import archive
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
anime_special=[]
anime_rating=[]
anime_note=[]
action_listTV=['name', 'start date', 'time', 'update weekday', 'update time', 'episodes', 'rating', 'notes', 'status', 'platform']
action_listCinema=['name', 'start date', 'time', 'update weekday', 'update time', 'rating', 'notes', 'cinema', 'status', 'platform']

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
    file_cur.execute("SELECT Special FROM anime ORDER BY UpdateTime")
    list_special=file_cur.fetchall()
    for item in list_special:
        item_str=str(item)
        anime_special.append(item_str.replace(",", "").replace("('", "").replace("')", ""))
    file_cur.execute("SELECT Ratings FROM anime ORDER BY UpdateTime")
    list_rating=file_cur.fetchall()
    for item in list_rating:
        item_str=str(item)
        anime_rating.append(item_str.replace(",", "").replace("('", "").replace("')", ""))
    file_cur.execute("SELECT Notes FROM anime ORDER BY UpdateTime")
    list_note=file_cur.fetchall()
    for item in list_note:
        item_str=str(item)
        anime_note.append(item_str.replace(",", "").replace("('", "").replace("')", ""))

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
                       anime_upTime[number],
                       anime_special[number],
                       anime_rating[number],
                       anime_note[number])
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
    info_table.add_column('Special', justify='center')
    info_table.add_column('Rating', justify='center')
    info_table.add_column('Notes', justify='center')
    
    info_table.add_row(anime_list[number], 
                       anime_stat[number], 
                       anime_plat[number], 
                       anime_episode[number], 
                       anime_date[number],
                       anime_time[number], 
                       anime_weekday[number],
                       anime_upTime[number],
                       anime_special[number],
                       anime_rating[number],
                       anime_note[number])
    print(info_table, end='\n')

class Anime:
    def __init__(self, name, start, time, cinema, up_day, up_time, episodes, status, platform, rate, note):
        self.name=name
        self.start=start
        self.time=time
        self.cinema=cinema
        self.up_day=up_day
        self.up_time=up_time
        self.episodes=episodes
        self.status=status
        self.platform=platform
        self.rate=rate
        self.note=note

    def input_change(self, in_action):
        self.in_action=in_action
        dir_path = Path(os.path.dirname(__file__))
        root = dir_path / "animate_tracker.db"
        file_conn=sqlite3.connect(root)
        file_cur=file_conn.cursor()
        if self.in_action.lower()=='name':
            print('[yellow]Enter the change:[/yellow]', end=' ')
            new_value=input()
            file_cur.execute('UPDATE anime SET Name=? WHERE Name=?', (new_value, self.name, ))
            self.name=new_value
            anime_list[choice-1]=self.name

        elif self.in_action=='episodes':
            print('[yellow]Enter the change:[/yellow]', end=' ')
            new_value=input()
            file_cur.execute('UPDATE anime SET EpisodeNumber=? WHERE Name=?', (new_value, self.name, ))
            self.episodes=new_value
            anime_episode[choice-1]=self.episodes
 
        elif self.in_action=='cinema':
            print('[yellow]Enter the change:[/yellow]', end=' ')
            new_value=input()
            file_cur.execute('UPDATE anime SET Cinema=? WHERE Name=?', (new_value, self.name, ))
            self.cinema=new_value
            anime_cinema[choice-1]=self.cinema

        elif self.in_action=='status':
            print('[yellow]Enter the change:[/yellow]', end=' ')
            new_value=input()
            file_cur.execute('UPDATE anime SET ViewStatus=? WHERE Name=?', (new_value, self.name, ))
            self.status=new_value
            anime_stat[choice-1]=self.status

        elif self.in_action=='update weekday':
            print('[yellow]Enter the change:[/yellow]', end=' ')
            new_value=input()
            file_cur.execute('UPDATE anime SET UpdateWeekDay=? WHERE Name=?', (new_value, self.name, ))
            self.up_day=new_value
            anime_weekday[choice-1]=self.up_day

        elif self.in_action=='update time':
            print('[yellow]Enter the change:[/yellow]', end=' ')
            new_value=input()
            file_cur.execute('UPDATE anime SET UpdateTime=? WHERE Name=?', (new_value, self.name, ))
            self.up_time=new_value
            anime_upTime[choice-1]=self.up_time

        elif self.in_action=='notes':
            print('[yellow]Enter the change:[/yellow]', end=' ')
            new_value=input()
            file_cur.execute('UPDATE anime SET Notes=? WHERE Name=?', (new_value, self.name, ))
            self.note=new_value
            anime_note[choice-1]=self.note

        elif self.in_action=='rating':
            print('[yellow]Enter the change:[/yellow]', end=' ')
            new_value=input()
            file_cur.execute('UPDATE anime SET Ratings=? WHERE Name=?', (new_value, self.name, ))
            self.rate=new_value
            anime_rating[choice-1]=self.rate
            
        elif self.in_action=='start date':
            print('[yellow]Enter the change:[/yellow]', end=' ')
            new_value=input()
            file_cur.execute('UPDATE anime SET StartDate=? WHERE Name=?', (new_value, self.name, ))
            self.start=new_value
            anime_date[choice-1]=self.start
            
        elif self.in_action=='platform':
            print('[yellow]Enter the change:[/yellow]', end=' ')
            new_value=input()
            file_cur.execute('UPDATE anime SET ViewPlatform=? WHERE Name=?', (new_value, self.name, ))
            self.platform=new_value
            anime_plat[choice-1]=self.platform
            
        elif self.in_action=='time':
            print('[yellow]Enter the change:[/yellow]', end=' ')
            new_value=input()
            file_cur.execute('UPDATE anime SET Time=? WHERE Name=?', (new_value, self.name, ))
            self.time=new_value
            anime_time[choice-1]=self.time

        file_conn.commit()
        file_conn.close()

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
        info_table.add_column('Rating', justify='center')
        info_table.add_column('Notes', justify='center')

        info_table.add_row(self.name, 
                        self.status, 
                        self.platform, 
                        self.episodes, 
                        self.start,
                        self.time, 
                        self.up_day,
                        self.up_time,
                        self.rate,
                        self.note)
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
        info_table.add_column('Rating', justify='center')
        info_table.add_column('Notes', justify='center')

        info_table.add_row(self.name, 
                        self.status, 
                        self.cinema, 
                        self.start,
                        self.time, 
                        self.up_day,
                        self.up_time,
                        self.rate,
                        self.note)
        print(info_table, end='\n')



get_file()
program_run=True
while program_run==True:
    os.system('cls')
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
            os.system('cls')
            info_display_TV(choice-1)
            print('[bold green]Please select the above attributes to change: [bold green]', end=' ')
            action=input()
            while action.lower() not in action_listTV:
                print('[bold red]Invalid action, please try again:[/bold red]', end=' ')
                action=input()
            anime=Anime(anime_list[choice-1], anime_date[choice-1], anime_time[choice-1], anime_cinema[choice-1], anime_weekday[choice-1], anime_upTime[choice-1], anime_episode[choice-1], anime_stat[choice-1], anime_plat[choice-1], anime_rating[choice-1], anime_note[choice-1])
            anime.input_change(action)
            os.system('cls')
            anime.overview_TV()
            print('[yellow]Do you want to confirm your change(s):[/yellow]', end=' ')
            confirm_choice=input()
            if confirm_choice.lower()=='yes':
                anime_loop=False
            elif confirm_choice.lower()=='no':
                anime_loop=True
        
    else:
        anime_loop=True
        while anime_loop==True:
            os.system('cls')
            info_display_movie(choice-1)
            print('[bold green]Please select the above attributes to change: [bold green]', end=' ')
            action=input()
            while action.lower() not in action_listCinema:
                print('[bold red]Invalid action, please try again:[/bold red]', end=' ')
                action=input()
            anime=Anime(anime_list[choice-1], anime_date[choice-1], anime_time[choice-1], anime_cinema[choice-1], anime_weekday[choice-1], anime_upTime[choice-1], anime_episode[choice-1], anime_stat[choice-1], anime_plat[choice-1], anime_rating[choice-1], anime_note[choice-1])
            anime.input_change(action)
            os.system('cls')
            anime.overview_cinema()
            print('[yellow]Do you want to confirm your change(s) (Yes / No):[/yellow]', end=' ')
            print(len(anime_list))
            confirm_choice=input()
            if confirm_choice.lower()=='yes':
                anime_loop=False
            elif confirm_choice.lower()=='no':
                anime_loop=True

    os.system('cls')
    print('[yellow]Would you like to continue on changing info(s) (Yes / No):[/yellow]', end=' ')
    confirm_choice=input()
    if confirm_choice.lower()=='yes':
            program_run=True

    elif confirm_choice.lower()=='no':
            program_run=False
            os.system('cls')