#include <Arduino.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>


const char* SSID = "Lab1202";
const char* PASSWORD = "%Pr0j3ct2021%";

const char *serverName = "http://ip.jsontest.com";
HTTPClient http;


StaticJsonDocument<200> doc;


void setup4() {
    Serial.begin(9600);

    WiFi.begin(SSID, PASSWORD);
    Serial.print("Connecting to WiFi ..");
    while (WiFi.status() != WL_CONNECTED) {
        Serial.print('.');
        delay(500);
    }
    Serial.println(WiFi.localIP());
}

void loop4() {
    http.begin(serverName);

    int httpResponseCode = http.GET();

    Serial.print("Status code: ");
    Serial.println(httpResponseCode);

    String json = http.getString();

    deserializeJson(doc, json);
    
    const char *ip = doc["ip"];
    Serial.print("Globalna ip adresa je: ");
    Serial.println(ip);

    http.end();
    delay(10000);
}