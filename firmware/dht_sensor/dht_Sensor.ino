
#include "DHT.h"

#define DHTPIN 2     
#define DHTTYPE DHT11   

DHT dht(DHTPIN, DHTTYPE);

unsigned long previousMillis = 0;
unsigned long startMeasuringTime = 0; // Tracks when the 'S' was pressed
const long interval = 2000;           // Time between samples
const long timeoutLimit = 10000;      // 10 second total timeout

int readingCount = 0;
float totalTemp = 0.0;
bool isMeasuring = false;

void setup() {
  Serial.begin(9600);
  dht.begin();
  Serial.println(F("System Ready. Send 'S' for average."));
}

void loop() {
  // 1. Handle Serial Commands
  if (Serial.available() > 0) {
    char ReceivedByte = Serial.read();
    if (ReceivedByte == 'S' && !isMeasuring) {
      isMeasuring = true;
      readingCount = 0;
      totalTemp = 0.0;
      startMeasuringTime = millis(); // Mark the start time. we create a timer that allows the Arduino to keep looping while it waits for the next reading.
      previousMillis = millis();     // Trigger first read immediately
      Serial.println(F("Started. Expecting 3 samples in < 10s..."));
    }
  }

  // 2. Measurement Logic
  if (isMeasuring) {
    unsigned long currentMillis = millis();

    // GLOBAL TIMEOUT CHECK
    if (currentMillis - startMeasuringTime > timeoutLimit) {
      Serial.println(F("SYSTEM ERROR: Measurement timed out! Check wiring."));
      isMeasuring = false;
      return; 
    }

    // SAMPLE INTERVAL CHECK
    if (currentMillis - previousMillis >= interval) {
      previousMillis = currentMillis; 

      float currentRead = dht.readTemperature();

      if (!isnan(currentRead)) {
        readingCount++;
        totalTemp += currentRead;
        Serial.print(F("Sample #"));
        Serial.print(readingCount);
        Serial.print(F(": "));
        Serial.println(currentRead);
      }

      if (readingCount >= 3) {
        Serial.print(F("Success! Average: "));
        Serial.println(totalTemp / 3.0);
        isMeasuring = false; 
      }
    }
  }
}

  
  }
  
    
  
}
