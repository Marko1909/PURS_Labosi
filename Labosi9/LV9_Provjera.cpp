#include <Arduino.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

const char* SSID = "Lab1202";
const char* PASSWORD = "%Pr0j3ct2021%";

const char *serverName = "http://192.168.86.219/hocu_bod?id=202";
HTTPClient http;

StaticJsonDocument<200> doc;


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

void loop1() {
    WiFi.localIP();
    String ime = "Marko";
    String prezime = "Antolić";
    String ip = "193.198.206.131";
    doc["ime"] = ime;
    doc["prezime"] = prezime;
    doc["ip"] = ip;

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


void loop() {
    http.begin(serverName);

    int httpResponseCode = http.GET();

    Serial.print("Status code: ");
    Serial.println(httpResponseCode);

    String json = http.getString();

    Serial.print("Status code: ");
    Serial.println(httpResponseCode);
    Serial.println(http.getString());


    http.end();
    delay(10000);
}