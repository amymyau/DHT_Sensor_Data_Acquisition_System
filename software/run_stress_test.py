

#This script acts as the "manager." It runs your logger, captures the output, and calculates the final grade of the hardware 's stability
import subprocess
import time
import sys

# Configuration
#TEST_DURATION_SECONDS = 3600  # 1 Hour Test
TEST_DURATION_SECONDS = 300  # 5 min Test
TARGET_SCRIPT = "Python-Arduino-CSV-Logger-Signal-Handler_optimized_BME_chaotic.py"

print(f"--- I2C/Serial Stress Test Harness v1.0 ---")
print(f"Target: {TARGET_SCRIPT}")
print(f"Duration: {TEST_DURATION_SECONDS} seconds")

start_time = time.time()

# Launch the logger as a subprocess
process = subprocess.Popen(
    [sys.executable, TARGET_SCRIPT],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

# Simulate entering the COM port automatically if needed
# process.stdin.write("COM3\n")
# process.stdin.flush()

try:
    while time.time() - start_time < TEST_DURATION_SECONDS:
        # Check if process is still alive
        if process.poll() is not None:
            print("❌ Failure: Logger script crashed unexpectedly.")
            break
        time.sleep(10)
        elapsed = int(time.time() - start_time)
        print(f"⏱️ Test Progress: {elapsed}/{TEST_DURATION_SECONDS}s...")

except KeyboardInterrupt:
    print("\n🛑 Test manually aborted.")

finally:
    process.terminate()
    print("--- Test Complete. Check CSV for raw data. ---")
