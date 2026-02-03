//  To test the Python script's robustness
//  randomly simulate three common I2C/Sensor failures:
//  CRC Mismatch: Sending garbled data.
//  Timeout: Not responding at all.
//  Bus Busy: Sending an "Error" string instead of temperatures.


#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>

Adafruit_BME280 bme;  // I2C

void setup() {
  Serial.begin(9600);

  // Initialize BME280
  // Note: Use 0x76 if 0x77 (default) doesn't work
  if (!bme.begin(0x76)) {
    Serial.println("ERR: BME280 NOT FOUND");
    while (1)
      ;
  }

  // Weather monitoring settings (Optimal for low power/stability)
  bme.setSampling(Adafruit_BME280::MODE_FORCED,
                  Adafruit_BME280::SAMPLING_X1,  // temperature
                  Adafruit_BME280::SAMPLING_X1,  // pressure
                  Adafruit_BME280::SAMPLING_X1,  // humidity
                  Adafruit_BME280::FILTER_OFF);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();

    if (command == 'S') {
      // Force a reading from the sensor

      int chaos = random(0, 100);  // Generate a random number 0-99

      if (chaos < 5) {          // 5% chance of a simulated I2C "Hang"
                                // Send nothing, forcing Python to handle a timeout
      } else if (chaos < 10) {  // 5% chance of corrupted data
        Serial.println("ERR-CORRUPT-BUS-HUNG");
      } else {

        bme.takeForcedMeasurement(); // MUST have this for forced mode!

        Serial.print(bme.readTemperature());
        Serial.print("-");
        Serial.print(bme.readHumidity());
        Serial.print("-");
        Serial.println(bme.readPressure() / 100.0F);


        // Normal sensor read logic here
        //Serial.println("24.5-25.1-23.9");
      }
    }
  }
}
