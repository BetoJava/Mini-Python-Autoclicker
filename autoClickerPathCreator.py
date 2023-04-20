import time
import pyautogui
import threading
from pynput import mouse, keyboard
import json

clicks = []

def on_click(x, y, button, pressed):
    global start_time, clicks
    if pressed:
        if button == mouse.Button.left:
            elapsed_time = time.time() - start_time
            click = {"time": elapsed_time, "position": (x, y)}
            clicks.append(click)
            print(f'Time spent : {elapsed_time:.2f} s')
            print(f'Mouse position : ({x}, {y})')
            start_time = time.time()
        elif button == mouse.Button.right:
            save_clicks_to_json("clicks.json", clicks)
            print("Clicks saved in 'clicks.json'")
            return False

def monitor_mouse_clicks():
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

def on_press(key):
    if key == keyboard.Key.esc:
        return False

def monitor_keyboard():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def save_clicks_to_json(filename, clicks):
    with open(filename, 'w') as file:
        json.dump(clicks, file)
        
def load_clicks_from_json(filename):
    with open(filename, 'r') as file:
        clicks = json.load(file)
    return clicks


if __name__ == "__main__":
    start_time = time.time()
    mouse_monitor_thread = threading.Thread(target=monitor_mouse_clicks)
    keyboard_monitor_thread = threading.Thread(target=monitor_keyboard)
    mouse_monitor_thread.start()
    keyboard_monitor_thread.start()
