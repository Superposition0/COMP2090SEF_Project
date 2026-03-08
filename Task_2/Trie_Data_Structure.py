from pynput import keyboard
import threading
import time
import os

car_model=[]
temp=[]
running=True

def get_file():
    # This function is used for loading the datas of the csv file into the array.
    with open('gran_turismo_gt7.csv', 'r', encoding='utf-8') as file:
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
        result_list=car_result(query)
        display_list(query, result_list)
    except AttributeError:
        if key==keyboard.Key.space:
            temp.append(' ')
            query=''.join(temp)
            result_list=car_result(query)
            display_list(query, result_list)
        elif key==keyboard.Key.backspace:
            if temp:
                temp.pop()
                query=''.join(temp)
                result_list=car_result(query)
                display_list(query, result_list)

def car_result(query):
    # Comparing the typed string with the car models' names in the list.
    if not query:
        return []
    query_lower=query.lower()
    result_list=[car for car in car_model if query_lower in car.lower()]
    return result_list

def display_list(query, result_list):
     # Displaying the results in the terminal
     os.system('cls')
     print(f'Search: {query}\n')
     if result_list:
         print('Result(s):\n')
         for i in range(len(result_list)):
             print(f'{i+1}. {result_list[i]}')
     else:
         print('No results found.')
    
def start_listener():
    # Activating the keyboard listener, which links to every funciton in the code.
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

get_file()
listener_thread = threading.Thread(target=start_listener, daemon=True)
listener_thread.start()
print('Welcome to the car gallery!\n')
print('Type in any car you like!\n')
try:
    # time.sleep is used for continuely holding the thread, preventing the program from ending.
    while running:
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
print('Terminated searching process.')
