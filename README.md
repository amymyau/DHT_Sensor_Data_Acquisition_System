============

### High-Reliability Sensor Data Acquisition System
### I engineered a full-stack validation suite to bridge the gap between embedded hardware 
### and PC side analytics. To ensure 24/7 mission-critical stability, I implemented a 
### 'Chaos Monkey' fault-injection firmware to simulate I2C bus contention and NACK errors
### I complemented this with an automated Python test harness that calculated real-time
### reliability metrics over 12-hour soak tests. By integrating CI/CD pipelines via GitHub 
### Actions and developing a post-processing data-cleaning engine, I created a scalable 
### framework that ensures data integrity while significantly reducing manual auditing time


===========

### Start a background thread to handle printing the logger's output
### Removed the emoji since the window prompt is using an older encoding that
### does not understand emojis, the "child" process often inherits a "dumb" terminal pipe
### that does not have the same capabilities as the main PowerShell window, causing it
### to default back to the safest (but most restrictive) encoding
### used ASCII-based symbols instead



=======

### added the run_stress_test.py python script which acts as the manager running the logger, captures the output and calculates the final grade of the hardware's stability

=======

### Now support both DHT and BME sensors

=======
# DHT Sensor Data Acquisition System

A robust Arduino-based system for reading temperature data from a DHT11 sensor.

## Key Features
* **Averaging Logic:** Takes 3 consecutive samples and calculates the average for better data accuracy.
* **Non-Blocking Code:** Uses `millis()` instead of `delay()`, allowing the Arduino to remain responsive during measurement intervals.
* **Safety Timeout:** Includes a 10-second watchdog timer that resets the system if the sensor fails to provide 3 samples.
* **Serial Trigger:** Measurements are initiated by sending the character 'S' through the Serial Monitor.

## How to Use
1. Connect the DHT11 to Digital Pin 2.
2. Open the Serial Monitor at 9600 baud.
3. Send 'S' to begin a measurement cycle.

## 🚀 Recent Improvements (Refactor 2026)

Following principles of **Efficient Python Programming**, I refactored the logging engine to improve system performance and data reliability.

### 🛠️ Key Optimizations
* **I/O Performance:** Moved file operations outside the `while` loop. Instead of the "Open-Write-Close" cycle (which is CPU-expensive), the file is now opened once, significantly reducing OS overhead.
* **Data Persistence:** Integrated `csvfile.flush()` to ensure data is written to disk in real-time. This protects against data loss during power failures—critical for long-term system validation.
* **Professional Serialization:** Replaced manual string concatenation with the standard `csv` library to ensure robust formatting and compatibility with data analysis tools like Pandas.
* **Improved Error Handling:** Transitioned from C-style signal handlers to a Pythonic `try/except KeyboardInterrupt` block for cleaner resource cleanup (closing ports and files).

---


# DHT_Sensor_Data_Acquisition_System
