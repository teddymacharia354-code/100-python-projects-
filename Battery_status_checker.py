# First we import the tools we need
import psutil  # This let's us check battery status

print("====== Battery Status Checker ======")

# Get battery details. NB- This returns "None" on devices without a battery (like desktops)
battery = psutil.sensors_battery()

if battery is None:
    print("No battery detected on this device.")
else:
    percent = battery.percent  # Current battery percentage
    plugged_in = battery.power_plugged  # True if charging, False if not

    print(f"Battery level: {percent}%")

    if plugged_in:
        print("Status: Charging")
    else:
        print("Status: Not charging")

        # secsleft is how many seconds of battery are left, if available
        if battery.secsleft != psutil.POWER_TIME_UNLIMITED and battery.secsleft > 0:
            minutes_left = battery.secsleft // 60  # "//" gives whole minutes only
            print(f"Estimated time remaining: {minutes_left} minutes")

    print("=" * 30)

    # Give a simple warning if the battery is getting low
    if percent <= 20 and not plugged_in:
        print("Warning: Battery is low. Consider plugging in your charger.")
