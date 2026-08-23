# First we import the tools we need
import time  # This let's us track how much time has passed

print("====== Simple Stopwatch ======")
print("Press Enter to start...")
input()  # Waits here until the user presses Enter

start_time = time.time()  # Records the exact moment we started, in seconds
print("Stopwatch running. Press Enter to stop.")
input()  # Waits here until the user presses Enter again

end_time = time.time()  # Records the moment we stopped

elapsed = end_time - start_time  # How much time passed between start and stop

print("=" * 30)
print(f"Time elapsed: {elapsed:.2f} seconds")  # ":.2f" rounds to 2 decimal places
