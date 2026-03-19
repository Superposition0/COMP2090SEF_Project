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
    print(anime_list[0])
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
    print(anime_cinema[0])
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
    row=0
    info_table=Table(title='Info List', box=box.HEAVY)
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
    row=0
    info_table=Table(title='Info List', box=box.HEAVY)
    info_table.add_column('Anime Name', justify='center')
    info_table.add_column('Status', justify='center')
    info_table.add_column('[bold blue]Platform[/bold blue]', justify='center', style='cyan')
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
    def input_change(self, number, in_action):
        self.number=choice
        self.in_action=action
        print(choice)
        if self.in_action.lower()=='name':
            print('[yellow]Enter the change:[/yellow]', end=' ')
            new_value=input()
            anime_list[self.number]=new_value
        elif self.in_action=='episodes':
            print('[yellow]Enter the change:[/yellow]', end=' ')
            new_value=input()
            anime_episode[self.number]=new_value
        elif self.in_action=='cinema':
            print('[yellow]Enter the change:[/yellow]', end=' ')
            new_value=input()
            anime_cinema[self.number]=new_value
        elif self.in_action=='status':
            print('[yellow]Enter the change:[/yellow]', end=' ')
            new_value=input()
            anime_stat[self.number]=new_value
        elif self.in_action=='update weekday':
            print('[yellow]Enter the change:[/yellow]', end=' ')
            new_value=input()
            anime_weekday[self.number]=new_value
        elif self.in_action=='update time':
            print('[yellow]Enter the change:[/yellow]', end=' ')
            new_value=input()
            anime_upTime[self.number]=new_value
        elif self.in_action=='notes':
            print('[yellow]Enter the change:[/yellow]', end=' ')
            new_value=input()
            anime_note[self.number]=new_value
        elif self.in_action=='rating':
            print('[yellow]Enter the change:[/yellow]', end=' ')
            new_value=input()
            anime_rating[self.number]=new_value
        elif self.in_action=='start date':
            print('[yellow]Enter the change:[/yellow]', end=' ')
            new_value=input()
            anime_date[self.number]=new_value
        elif self.in_action=='platform':
            print('[yellow]Enter the change:[/yellow]', end=' ')
            new_value=input()
            anime_plat[self.number]=new_value
        elif self.in_action=='time':
            print('[yellow]Enter the change:[/yellow]', end=' ')
            new_value=input()
            anime_time[self.number]=new_value


class AnimeChange:
    def __init__(self, name, start, time, cinema, up_day, up_time, episodes, status, platform, rate, note):
        self.name=anime_list
        self.start=anime_date
        self.time=anime_time
        self.cinema=anime_cinema
        self.up_day=anime_weekday
        self.up_time=anime_time
        self.episodes=anime_episode
        self.status=anime_stat
        self.platform=anime_plat
        self.rate=anime_rating
        self.note=anime_note

    def change_info(self, input):
        pass


row=0
os.system('cls')
get_file()
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
    os.system('cls')
    info_display_TV(choice-1)
    print('[bold green]Please select the above attributes to change: [bold green]', end=' ')
    action=input()
    while action.lower() not in action_listTV:
        print('[bold red]Invalid action, please try again:[/bold red]', end=' ')
        action=input()
    anime=Anime()
    anime.input_change(choice, action)
        
else:
    os.system('cls')
    info_display_movie(choice-1)
    print('[bold green]Please select the above attributes to change: [bold green]', end=' ')
    action=input()
    while action.lower() not in action_listCinema:
        print('[bold red]Invalid action, please try again:[/bold red]', end=' ')
        action=input()
    anime=Anime()
    print(anime.input_change(choice, action))


anime_change=AnimeChange(anime_list, anime_date, anime_time, anime_cinema, anime_weekday, anime_upTime, anime_episode, anime_stat, anime_plat, anime_rating, anime_note)

