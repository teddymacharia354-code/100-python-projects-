# First we import the tools we need
import psutil        # This lets us check RAM usage
import datetime      # This lets us show the current time
import time          # This lets us pause for 1 second
import os            # This lets us clear the screen

# Function to create a progress bar
def make_bar(percent):
    bar_length = 20                    # Total length of the bar
    filled_length = int(bar_length * percent / 100)  # How much should be filled
    bar = "█" * filled_length + "-" * (bar_length - filled_length)  # Build the bar
    return f"[{bar}] {percent}%"       # Return formatted bar

# Start the live monitor
while True:  
    # Clear the screen to keep it neat
    os.system("cls" if os.name == "nt" else "clear")
    
    # Get the current time
    now = datetime.datetime.now()           
    current_time = now.strftime("%H:%M:%S") 
    
    # Get RAM details from Android
    ram = psutil.virtual_memory()           
    ram_usage = ram.percent                 # Percentage of RAM used
    ram_used_gb = ram.used / (1024**3)      # Convert to GB
    ram_total_gb = ram.total / (1024**3)    # Total RAM in GB
    
    # Display everything on screen
    print("====== Android RAM Monitor ======")
    print("Time:", current_time)
    print()
    print("RAM Usage:")
    print(make_bar(ram_usage))              # Show the progress bar
    print(f"Used: {ram_used_gb:.2f} GB / {ram_total_gb:.2f} GB")
    print("=================================")
    
    # Wait 1 second then update again
    time.sleep(1)
