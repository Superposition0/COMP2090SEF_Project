# Simulation of a searchbar using Trie data structure
from pynput import keyboard
import os
from pathlib import Path

car_model=[]
temp=[]

def get_file():
    # This function is used for loading the datas of the csv file into the array.
    dir_path=Path(os.path.dirname(__file__))
    root=dir_path/'gran_turismo_gt7.csv'
    with open(root, 'r', encoding='utf-8') as file:
        for line in file:
            car_model.append(line.strip().split(',')[0])

def on_press(key):
    # Records the key that you are pressing and store them into the array.
    global running
    if key==keyboard.Key.esc:  # Press Esc key to exit the program.
        running=False
        return False
    try:
        # Record and append typed letters into the array, including spcaes and backspaces.
        temp.append(key.char)
        query=''.join(temp)
        car_result(query)
    except AttributeError:
        if key==keyboard.Key.space:
            temp.append(' ')
            query=''.join(temp)
            car_result(query)
        elif key==keyboard.Key.backspace:
            if temp:
                temp.pop()
                query=''.join(temp)
                car_result(query)

def car_result(query):
    # Comparing the typed string with the car models' names in the list.
    os.system('cls||clear')
    print(f'Search: {query}\n')
    if not query:
        print('Type in any car model you like!')
        return []
    query_lower=query.lower()
    result_list=[car for car in car_model if query_lower in car.lower()]
    if result_list:
        print('Search Result(s):\n')
        for i in range(len(result_list)):
            print(f'{i+1}) {result_list[i]}')
    else:
        print('No results found.')

os.system('cls||clear')
print('Welcome to the car gallery!\n')
print('Type in any car model you like!\n')
get_file()
# Activate keyboard listener and record the keys typed.
listener=keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
print('\nSearchbar program terminated.')