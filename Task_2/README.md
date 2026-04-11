# Task 2
## Description(Data structure)
  Trie was selected to be our group's study topic.
  
  The demo contians a list of car models store in trie. User can search the car model they want by typing it. The list of matching car models will automatically update when you typing.
  
## Description(Algorithm)
Bucket sort was selected to be our group's study topic.

The demo would prompt user to enter the number of floating-point number they want to sort. A output will be printed with:
  1. The unsorted list of random floating-point number;
  2. The buckets and its contents;
  3. The sorted list of floating number

## Instruction to install and run (for both data structure and algorithm)
#### 1. !!!The data structure part will use `pynput` library's keyboard listener function. You might need to enable your terminal with sufficient permissions in order to try the demo 
#### 2. If you already installed the environment at task 1, you can skip the following part and directly run both demos with the environment activacted.
--- 
### Use Anaconda with enviroment file
  1. Download the whole `Task_2` folder
  2. Open Anaconda Navigator, click "Enviroments" and import the COMP2090SEF.yml
  3. After successful importation, open terminal(MacOS/Linux) or Anaconda prompt(Windows) and type
     ``` bash
     conda activate COMP2090SEF
     ```
  4. Open the terminal(MacOS/Linux) or powershell(Windows) at the directory of `Task_2` folder

### Download packages manually
  1. Python version >= 3.13 is recommended
  2. Open your terminal(MacOS/Linux) or powershell(Windows)
  3. Type the following command:
     ```bash
     pip install pynput
     ```
  4. Open the terminal(MacOS/Linux) or powershell(Windows) at the directory of `Task_2` folder
### Run the demos
  5. Run the following command to start up the app\
     **MacOS/Linux:**
     ```bash
     python3 Trie_Data_Structure.py
     ```
     OR
     ```bash
     python3 Bucket_Sort.py
     ```
     **Windows:**
     ```bash
     py Trie_Data_Structure.py
     ```
     OR
     ```bash
     py Bucket_Sort.py
     ```


