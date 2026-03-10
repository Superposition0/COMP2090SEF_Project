import json

info_name=[]
info_status=[]
info_platform=[]
user_stat=True

def get_file():
    with open('User_Anime.json', 'r', encoding='utf-8') as file:
        data=json.load(file)
    info_name=[item['anime'] for item in data]
    info_status=[item['status'] for item in data]
    info_platform=[item['platform'] for item in data]
    return info_name, info_status, info_platform

class anime:
    def __init__(self, name, status, platform, num_slot):
        self.name=info_name[number-1]
        self.status=input_stat
        self.platform=input_platform
        self.num_slot=number
        info_status[num_slot-1]=self.status
        info_platform[num_slot-1]=self.platform
        with open('User_Anime.json', 'r') as file:
           data=json.load(file)
        data[number-1]['anime']=info_name[num_slot-1]
        data[number-1]['status']=info_status[num_slot-1]
        data[number-1]['platform']= info_platform[num_slot-1]
        with open('User_Anime.json', 'w', encoding='utf-8') as new_file:
           json.dump(data, new_file, indent=1, ensure_ascii=False)

print('Please select an anime to change status:\n\n')
info_name, info_status, info_platform=get_file()
for i in range(len(info_name)):
    print(f'{i+1}. Name: {info_name[i]}\n   Status: {info_status[i]}\n   Platform: {info_platform[i]}\n', end='\n')
number=int(input('Please enter an anime that you want to change status: '))
while number>len(info_name):
    number=int(input('Out of range, please enter again: '))
while user_stat==True:
    print(f'Change anime: {info_name[number-1]}\n\n')
    input_stat=str(input('Please type in the status (Watching / Completed / Abandoned): '))
    input_platform=input('Please enter a platform: ')
    change_info=anime(info_name[number-1], input_stat, input_platform, number)
    choice=input('Would you want to change another anime (Yes / No): ')
    if choice=='Yes':
        for i in range(len(info_name)):
           print(f'{i+1}. Name: {info_name[i]}\n   Status: {info_status[i]}\n   Platform: {info_platform[i]}\n', end='\n')
           number=int(input('Please enter an anime that you want to change status: '))
        while number+1>len(info_name):
           number=int(input('Out of range, please enter again: '))
        pass
    elif choice=='No':
        user_stat=False
print('Thank you for using!')