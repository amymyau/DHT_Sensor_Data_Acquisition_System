
# since your Arduino is now intentionally acting "chaotic" (simulating real-world sensor glitches),
# the Python script needs to be smart enough to say, "Hey, that's not a valid reading," and
# keep running instead of crashing
# Adding "stress metrics"
# Tracking the Success Rate (Reliability) and Latency (how fast the Arduino responds).

import serial
import time
import csv

# Configuration
BAUDRATE = 9600
COM_PORT = input('Enter Serial Port Number (e.g., COM3) -> ')

# Metric Trackers
total_requests = 0
success_count = 0
start_program_time = time.time()

filename = time.strftime("BME280_Stress_Log_%d_%b_%Y.csv")

try:
    with serial.Serial(COM_PORT, BAUDRATE, timeout=5) as ser:
        print(f'Connected to {COM_PORT}. Waiting 3s for reset...')
        time.sleep(3)

        with open(filename, 'w', newline='') as csvfile:
            log_writer = csv.writer(csvfile)
            # Added "Response_Time" to CSV
            log_writer.writerow(['No', 'Time', 'Temp', 'Hum', 'Press', 'Latency_ms', 'Status'])

            print("\n" + "=" * 50)
            print("LOGGING STARTED - STRESS METRICS ENABLED")
            print("=" * 50)

            while True:
                total_requests += 1
                request_start = time.time()

                ser.write(b'S')  # Send request
                line = ser.readline().decode('utf-8').strip()

                request_end = time.time()
                latency = round((request_end - request_start) * 1000, 2)  # in milliseconds

                status = "UNKNOWN"

                if not line:
                    status = "TIMEOUT"
                    print(f"⚠️ [{total_requests}] TIMEOUT | Latency: {latency}ms")
                elif "ERR" in line:
                    status = "SENS_ERR"
                    print(f"❌ [{total_requests}] ARDUINO ERR: {line} | Latency: {latency}ms")
                else:
                    parts = line.split('-')
                    if len(parts) == 3:
                        success_count += 1
                        status = "SUCCESS"
                        temp, hum, press = parts

                        # Save to CSV
                        log_writer.writerow(
                            [total_requests, time.strftime("%H:%M:%S"), temp, hum, press, latency, status])
                        csvfile.flush()

                        # Print Stats
                        success_rate = (success_count / total_requests) * 100
                        print(f"✅ [{total_requests}] {temp}°C | {latency}ms | Reliability: {success_rate:.1f}%")
                    else:
                        status = "PARSE_ERR"
                        print(f"⚠️ [{total_requests}] MALFORMED DATA | Latency: {latency}ms")

                time.sleep(1)  # Short delay between requests

except KeyboardInterrupt:
    print('\n' + "=" * 50)
    print("SESSION SUMMARY")
    print(f"Total Requests: {total_requests}")
    print(f"Successful:     {success_count}")
    if total_requests > 0:
        print(f"Final Reliability: {(success_count / total_requests) * 100:.2f}%")
    print("=" * 50)