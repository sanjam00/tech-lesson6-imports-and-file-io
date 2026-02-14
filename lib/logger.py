from datetime import datetime
import os

LOG_PATH = "data/user_logs.txt"

def log_action(action):
    """Append a user action with a timestamp to the log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("user_logs.txt", "a") as file:
        file.write(f"[{timestamp}]{action}\n")

log_action("User logged in")
log_action("User updated profile")

def search_logs(keyword):
    """Search the log file for lines that match a keyword."""
    try:
        with open("user_logs.txt", "r") as file:
            for line in file:
                if keyword in line:
                    print(line.strip())
    except FileNotFoundError:
        print("Log file not found.")

search_logs("profile")