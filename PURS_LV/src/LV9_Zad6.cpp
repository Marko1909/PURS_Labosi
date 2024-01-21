#include <Arduino.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

#define LED 22

const char* SSID = "Lab1202";
const char* PASSWORD = "%Pr0j3ct2021%";

WiFiServer server(80);
WiFiClient client;

void setup() {
    Serial.begin(9600);

    WiFi.begin(SSID, PASSWORD);
    Serial.print("Connecting to WiFi ..");
    while (WiFi.status() != WL_CONNECTED) {
        Serial.print('.');
        delay(500);
    }

    server.begin();

    Serial.println(WiFi.localIP());
}


void loop() {
  if (client = server.available()){
    String zahtjev = client.readString();

    if (zahtjev.indexOf("POST") != -1 && zahtjev.indexOf("ON") != -1){
      digitalWrite(LED, HIGH);
      Serial.println("ON");
    }

    if (zahtjev.indexOf("POST") != -1 && zahtjev.indexOf("OFF") != -1){
      digitalWrite(LED, LOW);
      Serial.println("OFF");
    }

    client.println("HTTP/1.1 200 OK");
    client.println("Connection: close");
    client.println();
    client.stop();
  }
}