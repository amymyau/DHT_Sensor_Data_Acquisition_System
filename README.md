=======

# added the run_stress_test.py python script which acts as the manager running the logger, captures the output and calculates the final grade of the hardware's stability

=======

# Now support both DHT and BME sensors

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
