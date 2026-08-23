import psutil
import time
import os

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("RAM Usage:", psutil.virtual_memory().percent, "%")
    time.sleep(1)