# Simulation of a searchbar using Trie data structure
from pynput import keyboard
import os
from pathlib import Path
import time

class TrieNode: # Creates a possible search route depending on the users input
    def __init__(self):
        self.children={}
        self.word_end=False

class Trie:
    def __init__(self): # Initialize TrieNode
        self.root=TrieNode()

    def insert(self, word): # Create child note: which is for the possible word the user is typing
        node=self.root
        for char in word.lower():
            if char not in node.children:
                node.children[char]=TrieNode()
            node=node.children[char]
        node.word_end=True

    def Prefix(self, prefix): # A function that appends all matching words or searches with the prefix string
        def collect(node, current, results):
            if node.word_end:
                results.append(current)
            for char, child_node in node.children.items():
                collect(child_node, current+char, results)
        prefix=prefix.lower()
        node=self.root
        for char in prefix:
            if char not in node.children: # Returns an empty list if the prefix string is not part of the child node
                return []
            node=node.children[char]
        results=[]
        collect(node, prefix, results)
        return results

trie=Trie()
temp=[]

def get_file():
    # This function is used for loading the datas of the csv file into the array.
    dir_path=Path(os.path.dirname(__file__))
    root=dir_path/'gran_turismo_gt7.csv'
    with open(root, 'r', encoding='utf-8') as file:
        for line in file:
            car_name=line.strip().split(',')[0]
            trie.insert(car_name)

def on_press(key):
    # Records the key that you are pressing and store them into the array.
    global running
    if key==keyboard.Key.esc:  # Press Esc key to exit the program.
        running=False
        return False
    try:
        # Record and append typed prefix letters into the array, including spcaes and backspaces.
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
    # Comparing the prefix string with the car models' names in the list.
    os.system('cls||clear')
    start=time.time()
    print(f'Search: {query}\n')
    if not query:
        print('Type in any car model you like!')
        return []
    result_list=trie.Prefix(query)
    if result_list:
        print('Search Result(s):\n')
        for i in range(len(result_list)):
            print(f'{i+1}) {result_list[i]}')
        end=time.time()
        print(f'\nTime used: {end-start}')
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
print('\nSearch bar program terminated.')