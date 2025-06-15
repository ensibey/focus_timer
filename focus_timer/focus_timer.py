import time
import json
import datetime
import os

DATA_FILE = "focus_data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def log_session(duration_minutes, session_type):
    data = load_data()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    data.append({"time": now, "duration": duration_minutes, "type": session_type})
    save_data(data)

def countdown(minutes):
    total_seconds = minutes * 60
    while total_seconds:
        mins, secs = divmod(total_seconds, 60)
        print(f"\r⏳ {mins:02d}:{secs:02d}", end="")
        time.sleep(1)
        total_seconds -= 1
    print()

def start_timer():
    print("Starting focus session (25 minutes)...")
    countdown(25)
    print("✅ Focus session complete!")
    log_session(25, "focus")

    print("Starting break (5 minutes)...")
    countdown(5)
    print("☕ Break finished!")
    log_session(5, "break")

def show_history():
    data = load_data()
    if not data:
        print("No session history found.")
        return

    print("\n📜 Session History:")
    for entry in data[-10:]:
        print(f"- {entry['time']} | {entry['type'].capitalize()} | {entry['duration']} min")

def main():
    print("=== Focus Timer (Pomodoro) ===")
    while True:
        print("\n1. Start Focus Session")
        print("2. Show History")
        print("3. Exit")
        choice = input(">> ").strip()
        if choice == "1":
            start_timer()
        elif choice == "2":
            show_history()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
