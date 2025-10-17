import threading   # For running multiple tasks sabay-sabay (concurrency)
import time        # For delay/sleep sa bawat step
import random      # Para sa random na galaw ng runners

# Function para sa bawat runner (tatakbo hanggang 100 meters)
def runner(name):
    distance = 0
    while distance < 100:
        step = random.randint(5, 15)  # Random run bawat turn
        distance += step
        print(f"{name} ran {step} meters (Total: {distance}m)")
        time.sleep(random.uniform(0.5, 1.5))  # Random delay para hindi sabay

    print(f"{name} reached the finish line!")

# Dalawang thread para sa dalawang runner
runner1 = threading.Thread(target=runner, args=("Runner 1",))
runner2 = threading.Thread(target=runner, args=("Runner 2",))

print("The race has started!\n")

# Start na ang dalawang threads (tatakbo sabay)
runner1.start()
runner2.start()

# Hihintayin natin pareho matapos bago mag-end ang program
runner1.join()
runner2.join()

print("\n Race finished! Let's see who was faster next time!")