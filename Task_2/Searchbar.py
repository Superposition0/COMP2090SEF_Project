from pynput import keyboard
import threading
import time

anime_list = []
record = []
running = True           # flag used by main loop to determine when to exit

def load_anime():
    with open('anime.csv', 'r') as file:
        for line in file:
            # Extract the second column (corrected anime name)
            parts = line.strip().split(',')
            if len(parts) > 1:
                anime_list.append(parts[1])

def search_anime(query):
    """Search for anime names containing the query string (case-insensitive)"""
    if not query:
        return []
    query_lower = query.lower()
    results = [anime for anime in anime_list if query_lower in anime.lower()]
    return results

def display_results(query, results):
    """Clear screen and display search results"""
    print("\033[2J\033[H")  # Clear screen
    print(f"Search: {query}\n")
    if results:
        print(f"Found {len(results)} match(es):")
        for i, anime in enumerate(results[:10], 1):  # Show top 10 results
            print(f"  {i}. {anime}")
    else:
        print("No matches found.")

def on_press(key):
    global running

    # exit when Esc is pressed
    if key == keyboard.Key.esc:
        running = False
        return False               # stop listener

    try:
        record.append(key.char)
        query = ''.join(record)
        results = search_anime(query)
        display_results(query, results)
    except AttributeError:
        # Handle space key
        if key == keyboard.Key.space:
            record.append(' ')
            query = ''.join(record)
            results = search_anime(query)
            display_results(query, results)
        # Handle backspace
        elif key == keyboard.Key.backspace:
            if record:
                record.pop()
            query = ''.join(record)
            results = search_anime(query)
            display_results(query, results)

def start_listener():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# Load anime data
load_anime()

# Start listening in a background thread
listener_thread = threading.Thread(target=start_listener, daemon=True)
listener_thread.start()

print("Searchbar started! Start typing to search for anime names...")
print("Press Ctrl+C to exit.\n")

try:
    while running:
        time.sleep(0.1)
except KeyboardInterrupt:
    # we still catch Ctrl-C in case the user wants that fallback
    pass

print("\n\nSearchbar stopped.")
