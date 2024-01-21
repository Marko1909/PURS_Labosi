#include <Arduino.h>

#define POT 32

#define PWM_PIN 22
#define PWM_CHANNEL 0
#define FREQUENCY 5000
#define RESOLUTION 12

void setup2() {
  Serial.begin(9600);

  ledcSetup(PWM_CHANNEL, FREQUENCY, RESOLUTION);
  ledcAttachPin(PWM_PIN, PWM_CHANNEL);
}

void loop2() {
    Serial.println(analogRead(POT));

    ledcWrite(PWM_CHANNEL, analogRead(POT));
    delay(10);
}
