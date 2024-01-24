#include <WiFi.h>
#include "PubSubClient.h"

const char *MQTT = "192.168.86.216";

const char* SSID = "Lab1202";
const char* PASSWORD = "%Pr0j3ct2021%";

WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
    Serial.begin(9600);
    
    WiFi.begin(SSID, PASSWORD);
    Serial.print("Connecting to WiFi ..");
    while (WiFi.status() != WL_CONNECTED) {
        Serial.print('.');
        delay(500);
    }

    client.setServer(MQTT, 1883);

    while (!client.connected()) {
        Serial.print("Attempting MQTT connection...");
        if (client.connect("ESP32Client")) {
            Serial.println("connected");
        }
        else{
            Serial.print("failed, rc=");
            Serial.print(client.state());
            Serial.println(" try again in 5 seconds");
            (5000);
        }
    }
}

void loop() {
    client.publish("LV10/Python", "Marko je najbolji!");
    delay(1000);
}