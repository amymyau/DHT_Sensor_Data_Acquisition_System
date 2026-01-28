## 🚀 Recent Improvements (Refactor 2026)

Following principles of **Efficient Python Programming**, I refactored the logging engine to improve system performance and data reliability.

### 🛠️ Key Optimizations
* **I/O Performance:** Moved file operations outside the `while` loop. Instead of the "Open-Write-Close" cycle (which is CPU-expensive), the file is now opened once, significantly reducing OS overhead.
* **Data Persistence:** Integrated `csvfile.flush()` to ensure data is written to disk in real-time. This protects against data loss during power failures—critical for long-term system validation.
* **Professional Serialization:** Replaced manual string concatenation with the standard `csv` library to ensure robust formatting and compatibility with data analysis tools like Pandas.
* **Improved Error Handling:** Transitioned from C-style signal handlers to a Pythonic `try/except KeyboardInterrupt` block for cleaner resource cleanup (closing ports and files).

---


# DHT_Sensor_Data_Acquisition_System
