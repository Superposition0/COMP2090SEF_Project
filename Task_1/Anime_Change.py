import json

anime_names=[]
anime_episodes=[]
anime_status=[]

def get_file():
    with open('Anime List.json', 'r', encoding='utf-8') as file:
        data=json.load(file)
    anime_names=[item['name'] for item in data]
    anime_episodes=[item['episodes'] for item in data]
    anime_status=[item['status'] for item in data]
    return anime_names, anime_episodes, anime_status

def change(number, name, epidsode, status):
    with open('Anime List.json', 'r') as file:
        data=json.load(file)
    data[number-1]['name']=name
    data[number-1]['episodes']=epidsode
    data[number-1]['status']=status
    with open('Anime List.json', 'w', encoding='utf-8') as new_file:
        json.dump(data, new_file, indent=1, ensure_ascii=False)

anime_names, anime_episodes, anime_status = get_file()
for i in range(len(anime_names)):
    print(f"{i+1}. {anime_names[i]}, {anime_episodes[i]}, {anime_status[i]}")
print(f'\n')
num=int(input('Please enter the row number: '))
new_name=input('New name: ')
new_episodes=int(input('New amount of episodes: '))
new_status=input('New status: ')
change(num, new_name, new_episodes, new_status)
print(f'Changes has been successfully made.')
