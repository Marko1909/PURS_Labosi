#include <Arduino.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

const char* SSID = "Lab1202";
const char* PASSWORD = "%Pr0j3ct2021%";

const char *serverName = "http://ip.jsontest.com";
HTTPClient http;


StaticJsonDocument<200> doc;


void setup5() {
    Serial.begin(9600);

    WiFi.begin(SSID, PASSWORD);
    Serial.print("Connecting to WiFi ..");
    while (WiFi.status() != WL_CONNECTED) {
        Serial.print('.');
        delay(500);
    }
    Serial.println(WiFi.localIP());
}

void loop5() {
    String temperatura = "22";
    doc["temperatura"] = temperatura;

    String json;
    serializeJson(doc, json);

    http.begin(serverName);
    http.addHeader("Content-Type", "application/json");

    int httpResponseCode = http.POST(json);

    Serial.print("Status code: ");
    Serial.println(httpResponseCode);
    Serial.println(http.getString());

    http.end();
    delay(10000);
}