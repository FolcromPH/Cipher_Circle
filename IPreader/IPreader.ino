#include "ESPControl.h"
#include <Servo.h>  // Include the Servo library

const int maxValues = 10;  // Maximum number of integers to store
float values[maxValues];   // Array to store the integers
int valueCount = 0;        // Counter for the number of values stored

// Amplitude LED pins
const int ledPins[] = { D1, D2, D3, D6, D7 };
const int numLeds = 5;

// Variables
int percentage;
int percentage_prob;

// Servo setup
Servo myServo;
const int servoPin = D5;  // Servo connected to D5

void setup() {
  Serial.begin(9600);
  start("test", "bard1348");  // Initialize connection

  // Set up LED pins
  for (int i = 0; i < numLeds; i++) {
    pinMode(ledPins[i], OUTPUT);
    digitalWrite(ledPins[i], LOW);  // Start with LEDs off
  }

  // Attach the servo
  myServo.attach(servoPin);
  myServo.write(0);  // Initialize servo at 0°
}

void loop() {
  if (CheckNewReq() == 1) {   // Check for a new request
    String path = getPath();  // Retrieve the request path as a string
    path.remove(0, 1);        // Remove the leading slash if needed
    path.trim();              // Remove spaces or newlines

    // Reset storage before processing new data
    valueCount = 0;

    // Split and store multiple integers
    int startIndex = 0;
    int endIndex = path.indexOf(',');  // Find the first comma

    while (endIndex != -1 && valueCount < maxValues) {         // Process until no commas or max reached
      String valueStr = path.substring(startIndex, endIndex);  // Extract substring
      valueStr.trim();                                         // Remove any spaces
      values[valueCount] = valueStr.toInt();                   // Convert and store integer
      valueCount++;

      startIndex = endIndex + 1;
      endIndex = path.indexOf(',', startIndex);
    }

    // Process the last value (after the last comma)
    if (valueCount < maxValues) {
      String lastValueStr = path.substring(startIndex);
      lastValueStr.trim();
      values[valueCount] = lastValueStr.toInt();
      valueCount++;
    }

    // Print stored integers
    Serial.println("Stored values:");
    for (int i = 0; i < valueCount; i++) {
      Serial.print("Value ");
      Serial.print(i + 1);
      Serial.print(": ");
      Serial.println(values[i]);
    }

    // Compare prob_0 and prob_1 (index 1 and 2 in the array)
    if (valueCount >= 4) {
      int prob_0 = values[0];
      int prob_1 = values[1];

      Serial.print("Comparing prob_1 and prob_0: ");
      if (prob_0 > prob_1) {
        Serial.print("prob_0 is greater: ");
        Serial.println(prob_0);
        percentage = prob_0;
      } else if (prob_1 > prob_0) {
        Serial.print("prob_1 is greater: ");
        Serial.println(prob_1);
        percentage = prob_1;
      } else {
        Serial.print("Values are equal, showing prob_0: ");
        Serial.println(prob_0);
        percentage = prob_0;
      }

      // Control LEDs
      int ledsToLight = map(percentage, 0, 100, 0, numLeds);
      for (int i = 0; i < numLeds; i++) {
        if (i < ledsToLight) {
          digitalWrite(ledPins[i], HIGH);
        } else {
          digitalWrite(ledPins[i], LOW);
        }
      }

      // Compare prob_x and prob_y
      int prob_x = values[2];  // value3
      int prob_y = values[3];  // value4
      if (prob_x > prob_y) {
        percentage_prob = prob_x;  // Use the greater value
      } else if (prob_y > prob_x) {
        percentage_prob = prob_y;  // Use the greater value
      } else {
        percentage_prob = prob_x;  // If equal, use value3
      }

      // Servo control
      int servoAngle = map(percentage_prob, 0, 100, 0, 180);
      myServo.write(servoAngle);  // Move servo
      Serial.print("Servo angle: ");
      Serial.println(servoAngle);
    } else {
      Serial.println("Not enough values to process.");
    }
  }
}
