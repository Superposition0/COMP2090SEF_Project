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

#Create
def save_data(data_list):
    "Save the data to json file"
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(data_list, f)

def create_entry():
    "Add logic"
    print("Add New Anime")
    # 1. name
    name = typer.prompt("1. Name")
    # 2. start airing date
    start_date = typer.prompt("2. Start airing date (DD/MM/YYYY)")
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

    #convert to jason
    entry_data = {
        "name": name,
        "startDate": start_date,
        "Time": "",             
        "Cinema": "",     
        "UpdateWeekDay": weekday,
        "UpdateTime": u_time,
        "EpisodeNumber": eps,
        "Special": special,
        "ViewPlatform": platform,
        "Ratings": "",          
        "Notes": ""           
    }

    AnimeTrack.append(entry_data)
    save_data(AnimeTrack)
    print(f"\n[green]Successfully created anime object: {name}![/green]")