#include <Arduino.h>
#include <WiFi.h>
#include <HTTPClient.h>


const char* SSID = "Lab1202";
const char* PASSWORD = "%Pr0j3ct2021%";

const char *serverName = "http://ip.jsontest.com";
HTTPClient http;


void setup() {
    Serial.begin(9600);

    WiFi.begin(SSID, PASSWORD);
    Serial.print("Connecting to WiFi ..");
    while (WiFi.status() != WL_CONNECTED) {
        Serial.print('.');
        delay(500);
    }
    Serial.println(WiFi.localIP());
}

void loop() {
    http.begin(serverName);

    int httpResponseCode = http.GET();

    Serial.print("Status code: ");
    Serial.println(httpResponseCode);
    Serial.println(http.getString());

    http.end();
    delay(1000);
}