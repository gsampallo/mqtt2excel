#include <ESP8266WiFi.h>
#include <PubSubClient.h>

//Change for your WiFi Credentials
const char* ssid = "SSID"; 
const char* password = "PASSWORD";

// Use broker.hivemq.com
const char* mqtt_server = "52.29.42.5";
const char* keyDevice = "SENSORGAS01";

WiFiClient espClient;
PubSubClient client(espClient);
long lastMsg = 0;
char msg[50];
int value = 0;

void setup() {

  Serial.begin(9600);
  Serial.setTimeout(15000);
  Serial.println("Iniciando");
  
  setup_wifi();

  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);


}
void callback(char* topic, byte* payload, unsigned int length) {
  Serial.println("Mensaje recibido");
}
void setup_wifi() {

  delay(10);
  Serial.begin(9600);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }
}

void reconnect() {

  while (!client.connected()) {

    if (client.connect(keyDevice)) {
      Serial.println("connected");
    } else {
      delay(5000);
    }
  }
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop(); 

  int valor = analogRead(0);
  Serial.println(valor);
  snprintf (msg, 75, "%ld", valor);
  
  client.publish("NIVELGAS",msg); 

  delay(500);


}