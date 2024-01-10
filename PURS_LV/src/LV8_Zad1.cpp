#include <Arduino.h>

#define GREEN_LED 21
#define BLUE_LED 22
#define BUTTON 32

void setup1() {
  Serial.begin(9600);
  pinMode(GREEN_LED, OUTPUT);
  pinMode(BLUE_LED, OUTPUT);
  pinMode(BUTTON, INPUT_PULLDOWN);
}

void loop1() {
  if(digitalRead(BUTTON) == LOW){
    digitalWrite(BLUE_LED, LOW);
    digitalWrite(GREEN_LED, HIGH);
    Serial.println("Uključena je zelena ledica, a plava isključena.");
  }
  else{
    digitalWrite(BLUE_LED, HIGH);
    digitalWrite(GREEN_LED, LOW);
    Serial.println("Uključena je plava ledica, a zelena isključena.");
  }
  delay(10);
}
