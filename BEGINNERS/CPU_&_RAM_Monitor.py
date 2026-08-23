import time          # lets us pause for 1 second
import os            # lets us run system commands like "clear" or "cls"
import psutil        # lets us read CPU and RAM usage
import datetime      # lets us get the current time

psutil.cpu_percent()  # Prime the measurement. First call always returns 0.0, so we do it once

while True:  # loop forever until you press Ctrl+C
    # 1. CLEAR THE SCREEN
    # "cls" works on Windows, "clear" works on Mac/Linux
    os.system("cls" if os.name == "nt" else "clear")
    
    # 2. GET CURRENT TIME
    now = datetime.datetime.now()              # get current date and time
    current_time = now.strftime("%H:%M:%S")    # format as HH:MM:SS
    
    # 3. GET CPU AND RAM USAGE
    cpu_usage = psutil.cpu_percent(interval=0.5)  # measure CPU over 0.5 seconds
    ram_usage = psutil.virtual_memory().percent   # get RAM usage percentage
    
    # 4. PRINT EVERYTHING
    print("====== System Monitor ======")
    print("Time:", current_time)
    print("CPU Usage:", cpu_usage, "%")
    print("RAM Usage:", ram_usage, "%")
    print("============================")
    
    time.sleep(1)  # wait 1 second before updating again
