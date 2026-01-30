import serial
import time
import csv
import platform
import re  # Added for easier number extraction

# Configuration
BAUDRATE = 9600
COM_PORT = input('Enter Serial Port Number (e.g., COM3) -> ')

# Generate Filename
current_time = time.localtime()
filename = time.strftime("DHT_Avg_Log_%d_%b_%Y_%Hh_%Mm.csv", current_time)

print(f"OS: {platform.system()}-{platform.release()}")
print(f"Logging to: {filename}\n")

try:
    with serial.Serial(COM_PORT, BAUDRATE, timeout=1) as ser:
        print('Waiting 3s for Arduino reset...')
        time.sleep(3)

        with open(filename, 'w', newline='') as csvfile:
            log_writer = csv.writer(csvfile)
            # Simplified Header
            log_writer.writerow(['No', 'Date', 'Time', 'Average_Celsius'])

            log_count = 1
            print("Logging started. Press CTRL+C to stop.")

            while True:
                ser.write(b'S')
                print("Request sent. Waiting for 3-sample average...")

                # Increase timeout loop because Arduino takes ~6 seconds to measure
                start_wait = time.time()
                while (time.time() - start_wait) < 12:  # 12s timeout
                    line = ser.readline().decode('utf-8').strip()

                    if "Average:" in line:
                        # Use Regex to find the number in "Success! Average: 24.50"
                        match = re.search(r"[-+]?\d*\.\d+|\d+", line)
                        if match:
                            avg_temp = match.group()

                            now = time.localtime()
                            date_str = time.strftime("%d %b %Y", now)
                            time_str = time.strftime("%H:%M:%S", now)

                            row = [log_count, date_str, time_str, avg_temp]
                            log_writer.writerow(row)
                            csvfile.flush()

                            print(f"Log {log_count} saved: {avg_temp} °C")
                            log_count += 1
                            break  # Move to the next log interval

                time.sleep(10)  # Wait before asking for the next average

except KeyboardInterrupt:
    print('\nCTRL+C detected. Closing safely...')
except Exception as e:
    print(f"Error: {e}")
finally:
    print('Data logging Terminated.')