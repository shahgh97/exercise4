import time
import math
import sys
import multiprocessing

def get_integer_input(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                print(f"Please enter a number between {min_value} and {max_value}.")
            else:
                return value
        except ValueError:
            print("Please enter a valid integer.")

interval = get_integer_input("Please enter the interval in seconds: ", min_value=1)
load = get_integer_input("Please enter the desired CPU load (0-100%): ", min_value=1, max_value=99)

def generate_cpu_load(interval, load):
    start_time = time.time()
    while time.time() - start_time < interval:
        a = math.sqrt(64*64*64*64*64)
        time.sleep((1 - load / 100.0) * interval)

print(f"Generating {load}% CPU load for {interval} seconds. Please wait...")
processes = [multiprocessing.Process(target=generate_cpu_load, args=(interval, load)) for _ in range(multiprocessing.cpu_count())]
for process in processes:
    process.start()
try:
    for process in processes:
        process.join()
except KeyboardInterrupt:
    print("\nCPU load generation stopped.")
print("CPU load generation completed successfully!")