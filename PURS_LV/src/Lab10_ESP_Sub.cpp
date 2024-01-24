#include <WiFi.h>
#include "PubSubClient.h"

const char *MQTT = "192.168.86.216";

const char* SSID = "Lab1202";
const char* PASSWORD = "%Pr0j3ct2021%";

WiFiClient espClient;
PubSubClient client(espClient);

void callback(char* topic, byte* payload, unsigned int length);

void setup() {
    Serial.begin(9600);
    
    WiFi.begin(SSID, PASSWORD);
    Serial.print("Connecting to WiFi ..");
    while (WiFi.status() != WL_CONNECTED) {
        Serial.print('.');
        delay(500);
    }

    client.setServer(MQTT, 1883);
    client.setCallback(callback);

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

    client.subscribe("LV10/Python");
    }
}

void loop() {
    client.loop();
}


void callback(char* topic, byte* payload, unsigned int length) {
    Serial.print("Message arrived [");
    Serial.print(topic);
    Serial.print("] ");
    for (int i=0;i<length;i++) {
        Serial.print((char)payload[i]);
    }
    Serial.println();
}