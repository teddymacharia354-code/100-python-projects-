import time
from datetime import datetime

def display_digital_clock(use_12hour=False):
    """Display a live digital clock"""
    print("=" * 50)
    print("DIGITAL CLOCK")
    print("Press Ctrl+C to stop")
    print("=" * 50)
    
    try:
        while True:
            now = datetime.now()
            
            if use_12hour:
                time_str = now.strftime("%I:%M:%S %p")
            else:
                time_str = now.strftime("%H:%M:%S")
            
            date_str = now.strftime("%A, %B %d, %Y")
            
            # Clear screen effect
            print(f"\r{time_str} | {date_str}", end="", flush=True)
            time.sleep(1)
    
    except KeyboardInterrupt:
        print("Clock stopped.")

def display_alarm_clock(target_time):
    """Display clock until target time"""
    print("=" * 50)
    print(f"ALARM SET FOR {target_time}")
    print("Press Ctrl+C to cancel")
    print("=" * 50 )
    
    try:
        while True:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            
            if current_time == target_time:
                print("\n" + "🔔 " * 10)
                print("ALARM! TIME IS UP!")
                print("🔔 " * 10 )
                break
            
            print(f"\rCurrent: {current_time}", end="", flush=True)
            time.sleep(1)
    
    except KeyboardInterrupt:
        print("Alarm cancelled.")

def main():
    print("=" * 50)
    print("DIGITAL CLOCK")
    print("=" * 50)
    
    while True:
        print("\nOptions:")
        print("1. View current time")
        print("2. Live clock (24-hour)")
        print("3. Live clock (12-hour)")
        print("4. Set alarm")
        print("5. Exit")
        
        choice = input("Select option (1-5): ").strip()
        
        if choice == "1":
            now = datetime.now()
            print(f"Current time: {now.strftime('%H:%M:%S')}")
            print(f"Date: {now.strftime('%A, %B %d, %Y')}")
        
        elif choice == "2":
            display_digital_clock(use_12hour=False)
        
        elif choice == "3":
            display_digital_clock(use_12hour=True)
        
        elif choice == "4":
            time_input = input("Set alarm (HH:MM:SS): ")
            display_alarm_clock(time_input)
        
        elif choice == "5":
            print("Thank you for using Digital Clock!")
            break
        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()