#include <Arduino.h>

#define GREEN_LED 21
#define BLUE_LED 22

#define POT 32

void setup3() {
  pinMode(GREEN_LED, OUTPUT);
  pinMode(BLUE_LED, OUTPUT);
}

void loop3() {
    int delaytime;

    if(analogRead(POT) > 2000){
        delaytime = 1000;
    }
    else{
        delaytime = 500;
    }
    
    digitalWrite(BLUE_LED, LOW);
    digitalWrite(GREEN_LED, HIGH);
    delay(delaytime);

    digitalWrite(BLUE_LED, HIGH);
    digitalWrite(GREEN_LED, LOW);
    delay(delaytime);
    
}
