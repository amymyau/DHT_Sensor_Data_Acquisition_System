

"""
DHT Serial Logger - Optimized Version
-------------------------------------
Refactored: 2026-01-27
Optimizations:
    1. Persistent file handling (Reduced I/O overhead)
    2. CSV module integration (Data standardisation)
    3. KeyboardInterrupt handling (Clean termination)
    4. Data Flushing (Power-loss protection)
"""



import serial
import time
import csv
import platform

# Configuration
BAUDRATE = 9600
LOG_INTERVAL = 1
COM_PORT = input('Enter Serial Port Number -> ')

# Generate Filename
current_time = time.localtime()
filename = time.strftime("DHT_%d_%B_%Y_%Hh_%Mm_%Ss_temp_log.csv", current_time)

print(f"OS: {platform.system()}-{platform.release()}")
print(f"Logging to: {filename}\n")

try:
    # Open Serial Port
    with serial.Serial(COM_PORT, BAUDRATE, timeout=1) as ser:
        print('Waiting 3s for Arduino reset...')
        time.sleep(3)

        # Open file once outside the loop
        with open(filename, 'w', newline='') as csvfile:
            log_writer = csv.writer(csvfile)
            log_writer.writerow(['No', 'Date', 'Time', 'Temp1', 'Temp2', 'Temp3'])

            log_count = 1
            print("Logging started. Press CTRL+C to stop.")

            while True:
                # 1. Hardware Query
                ser.write(b'S')
                # Use a small timeout to let Arduino respond
                line = ser.readline().decode('utf-8').strip()

                if not line:
                    continue

                # 2. Data Processing
                temp_values = line.split('-')
                now = time.localtime()
                date_str = time.strftime("%d %B %Y", now)
                time_str = time.strftime("%H:%M:%S", now)

                # 3. Efficient Writing
                row = [log_count, date_str, time_str] + temp_values
                log_writer.writerow(row)
                csvfile.flush()  # Ensures data is written to disk without closing file

                print(f"Log {log_count}: {row}")

                log_count += 1
                time.sleep(LOG_INTERVAL)

except KeyboardInterrupt:
    print('\nCTRL+C detected. Closing safely...')
except Exception as e:
    print(f"Error: {e}")
finally:
    print('Data logging Terminated.')

