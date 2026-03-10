import json

info_name=[]
info_status=[]
info_platform=[]

def get_file():
    with open('User_Anime.json', 'r', encoding='utf-8') as file:
        data=json.load(file)
    info_name=[item['anime'] for item in data]
    info_status=[item['status'] for item in data]
    info_platform=[item['platform'] for item in data]
    for i in range(len(info_name)):
        print(f'{i+1}. Name: {info_name[i]}\n   Status: {info_status[i]}\n   Platform: {info_platform[i]}\n', end='\n')

print("View user anime list\n")
get_file()
    
