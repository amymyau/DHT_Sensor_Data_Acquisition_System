
// DNT sensor sketch for enabling DHT sensor

// REQUIRES the following Arduino libraries:
// - DHT Sensor Library: https://github.com/adafruit/DHT-sensor-library
// - Adafruit Unified Sensor Lib: https://github.com/adafruit/Adafruit_Sensor

#include "DHT.h"

#define DHTPIN 2     // Digital pin connected to the DHT sensor

#define DHTTYPE DHT11   // DHT 11  
//#define DHTTYPE DHT21   // DHT 21 

// Connect pin 1 (on the left) of the sensor to +5V
// Connect pin 2 of the sensor to Digital pin 2 of Arduino
// Connect pin 3 (on the right) of the sensor to GROUND (if your sensor has 3 pins)
// Connect pin 4 (on the right) of the sensor to GROUND and leave the pin 3 EMPTY (if your sensor has 4 pins)
// Connect a 10K resistor from pin 2 (data) to pin 1 (power) of the sensor

// Initialize DHT sensor.

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  
  // Reading temperature
    
  char ReceivedByte = "0"; 
  float SensorValue[3] = {0.0,0.0,0.0}; // Array to store 3 consecutive values 
  float temp1, temp2, temp3 = 0.0;              // Variable to store temperature in Celsius

  if (Serial.available() > 0) //Wait for data reception
  {  
    ReceivedByte = Serial.read(); //Read data from Arduino Serial UART buffer
    if (ReceivedByte == 'S') { //Check received byte is $
      
         // Make three consecutivereadings from the specified analog pin
          for(int i=0;i<3;i++)
          {
            SensorValue[i] =  dht.readTemperature(); //Read 3 consecutive analog  values and store it in array
            delay(10);
          }
        // Check if any reads failed and exit early (to try again).
          if (isnan(SensorValue[0]) || isnan(SensorValue[1]) || isnan(SensorValue[2])) {
              Serial.println(F("Failed to read from DHT sensor!"));
              return;
            }
          temp1 = SensorValue[0];
          temp2 = SensorValue[1];
          temp3 = SensorValue[2];
          Serial.print(temp1);
          Serial.print('-');
          Serial.print(temp2);
          Serial.print('-');
          Serial.print(temp3);
          Serial.println(); 
          
         
      } else {//end of if  
          
       Serial.println("INVALID");
       Serial.println("use S to start conversion");
      }   
  
  
  }
  
    
  
}
