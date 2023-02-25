import time

print("Press ENTER to start the stopwatch")
print("Press ENTER again to stop the stopwatch")
input()

start_time = time.time()
print("Stopwatch started!")

input()

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("Total time:", total_time, "seconds")