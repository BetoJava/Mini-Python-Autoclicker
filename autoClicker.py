import time
import pyautogui
import json

def load_clicks_from_json(filename):
    with open(filename, 'r') as file:
        clicks = json.load(file)
    return clicks

def replay_clicks(clicks):
    for click in clicks:
        elapsed_time = click["time"]
        position = click["position"]
        print(f"Waiting {elapsed_time:.2f} secondes...")
        time.sleep(elapsed_time)
        pyautogui.click(position)

if __name__ == "__main__":
    filename = input("Json save file name : ")
    clicks = load_clicks_from_json(f"{filename}.json")
    for i in range(80):
        replay_clicks(clicks)
