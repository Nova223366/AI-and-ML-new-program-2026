import sys
import time
import threading
import itertools

def animate():
    # Use a cycle of characters to create a spinning effect
    for char in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rLoading ' + char)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     \n')

done = False
# Start the animation in a background thread
t = threading.Thread(target=animate)
t.start()

# --- Your long-running process goes here ---
time.sleep(5) 

# Stop the animation
done = True
