'''This uses `datetime` to check time and `playsound` to play an alarm sound.

#### **Step 1: Install the sound library**
Run this in terminal first:
```
pip install playsound
```
Download any mp3 sound file and put it in the same folder. Name it `alarm.mp3`
1.  Go to a free sound site: `soundbible.com` or `pixabay.com/sound-effects` 
2.  Search: `alarm clock`, `rooster`, `bell`
3.  Click `Download` → Choose `MP3`
4.  Rename the file to `alarm.mp3`
5.  Put it in the same folder as `alarm.py`'''

import time  # used to add delay
import datetime  # used to get current time
from playsound import playsound  # used to play the alarm sound

def set_alarm(alarm_time):
    """
    This function waits until the alarm time and then rings
    alarm_time should be in "HH:MM:SS" 24-hour format
    Example: "07:30:00"
    """
    print(f"Alarm set for {alarm_time}")
    print("Waiting...")

    # Keep checking the current time
    while True:
        # Get current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        
        # Print current time so user can see
        print("Current Time: ", current_time, end="\r")
        
        # Check if current time matches alarm time
        if current_time == alarm_time:
            print("\nWAKE UP! WAKE UP!")
            playsound('alarm.mp3')  # play the sound
            break  # stop the loop

        # Wait 1 second before checking again
        time.sleep(1)


def main():
    # Ask user to enter alarm time
    print("="*30)
    print("     PYTHON ALARM CLOCK")
    print("="*30)
    print("Enter time in 24-hour format HH:MM:SS")
    print("Example: 18:45:00 for 6:45 PM")

    alarm_input = input("Enter the alarm time: ")

    # Call the set_alarm function
    set_alarm(alarm_input)


# Run the program
if __name__ == "__main__":
    main()
'''Common error
If you get `playsound.PlaysoundException`, it means Python can't find `alarm.mp3`.  
Fix: Make sure the name is EXACTLY `alarm.mp3` and it's in the same folder.'''