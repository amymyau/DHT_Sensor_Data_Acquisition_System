
# Start a background thread to handle printing the logger's output
# removed the emoji since the window prompt is using an older encoding that
# does not understand emojis, a "child" process often inherits a "dumb" terminal pipe
# that does not have the same capabilities as the main powershell window, casuing it
# to default back to the safest (but most restrictive) encoding
# use ASCII-based symbols instead

import subprocess
import time
import sys
import threading

# Configuration
TEST_DURATION_SECONDS = 100  # 1 Hour Test
TARGET_SCRIPT = "Python-Arduino-CSV-Logger-Signal-Handler_optimized_BME_chaotic.py"
COM_PORT = "COM3\n"  # Ensure this matches your setup


def stream_output(pipe):
    """Function to read from the pipe and print in real-time."""
    try:
        for line in iter(pipe.readline, ''):
            print(f">>> {line.strip()}")
    except Exception as e:
        print(f"Stream error: {e}")


print(f"--- I2C/Serial Stress Test Harness v2.0 ---")
print(f"Target: {TARGET_SCRIPT}")

start_time = time.time()

# Launch the logger with the -u flag for unbuffered output
process = subprocess.Popen(
    [sys.executable, "-u", TARGET_SCRIPT],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,  # Merges errors into the same stream
    text=True,
    bufsize=1
)

# 1. Automatically send the COM port to the logger
process.stdin.write(COM_PORT)
process.stdin.flush()

# 2. Start a background thread to handle printing the logger's output
output_thread = threading.Thread(target=stream_output, args=(process.stdout,), daemon=True)
output_thread.start()

try:
    while time.time() - start_time < TEST_DURATION_SECONDS:
        if process.poll() is not None:
            #print("Failure: Logger script crashed unexpectedly.")
            print("Failure: Logger script crashed unexpectedly.")
            break

        elapsed = int(time.time() - start_time)
        remaining = TEST_DURATION_SECONDS - elapsed
        # Use \r to update the progress line in place without flooding the screen
        sys.stdout.write(f"\r Test Progress: {elapsed}/{TEST_DURATION_SECONDS}s | Remaining: {remaining}s...")
        sys.stdout.flush()

        time.sleep(1)

except KeyboardInterrupt:
    print("\n Test manually aborted.")

finally:
    process.terminate()
    print("\n--- Test Complete. Check CSV for raw data. ---")